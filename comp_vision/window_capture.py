import time
import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import numpy as np
import cv2 as cv
import os 
from .item_finder import find_item
import pyautogui

TOP_LEFT_X, TOP_LEFT_Y = 55,246
BOTTOM_RIGHT_X, BOTTOM_RIGHT_Y = 552, 991

class Screencap:
    def __init__(self):
        self.trader_inventory_TL = (55, 246)
        self.trader_inventory_BR = (552, 991)
        self.item_names = os.listdir('images')
        self.item_images = {image.split('.')[0] : cv.imread(f"images/{image}") \
                            for image in self.item_names}

        # self.DAD = pyautogui.getWindowsWithTitle('Dark and Darker  ')[0]
        # self.DAD.activate()


    @staticmethod
    def take_screenshot():

        hwnd = win32gui.FindWindow(None, 'Dark and Darker  ')
        

        if not hwnd:
            print("error")

        left, top, right, bot = win32gui.GetWindowRect(hwnd)
        w = right - left
        h = bot - top

        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

        saveDC.SelectObject(saveBitMap)

        result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 3)

        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'RGBA', 0, 1)

        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)


        image = np.array(im, dtype=np.uint8)
        image = image[:, :, :3]
        
        return np.array(image, dtype=np.uint8)
        # return im

    # Crops out the trader's inventory.
    def capture_trader_inventory(self) -> np.array:
        '''
        Crops the image, and returns a region containing only
        the traders inventory.
        '''
        current_screenshot = self.take_screenshot()
        trader_inventory = current_screenshot[self.trader_inventory_TL[1]:self.trader_inventory_BR[1], self.trader_inventory_TL[0]:self.trader_inventory_BR[0]]

        return trader_inventory
    
    # Crops out the rectangle containing the items stats
    def get_item_stats_img(self, screenshot: np.array) -> np.array:
        '''
        Applies adaptive thresholding to the image to crop the image
        capturing the items stats.
        '''
        screenshot_gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        adapt = cv.adaptiveThreshold(screenshot_gray, maxValue=32, 
                             adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                             thresholdType=cv.THRESH_BINARY,
                             blockSize=3,
                             C=0)
        contours, _ = cv.findContours(adapt, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)
        x, y, w, h = cv.boundingRect(contours[1]) #May need to be adjusted 
        region = screenshot[y: y + h, x: x + w]

        return region 
    
    def contains_green_item(self, region: np.array) -> bool:
        '''
        Checks if the image contains the color green.
        This indicates if we've found the item that is uncommon. 
        '''
        green = np.array([7, 168, 104])
        contains_green = np.any(np.all(region == green, axis=-1))

        return contains_green
    
    # If threshold is set < .98 golden/ruby/cobalt armor items get detected multiple times.
    def get_relevant_coords(self, thresh: float=.98) -> dict:
        '''
        Uses template matching to determine the location (x, y)
        of each item in '/images' in the traders inventory.
        '''
        image_coords = {}
        tl_x = self.trader_inventory_TL[0]
        tl_y = self.trader_inventory_TL[1]
        for item_name, item_image in self.item_images.items():
            ##TODO Adjust threshold for detection
            results = find_item(self.capture_trader_inventory(), item_image, thresh)
            if results:
                adjusted_coords = []
                for result in results:
                    x, y = result[0] + tl_x, result[1] + tl_y
                    adjusted_coords.append((x,y))
                image_coords[item_name] = adjusted_coords
        
        return image_coords
    
    def get_text_locs(self, ocr_results: list) -> dict:
        '''
        Takes a list of results from easyocr and populates a 
        dictionary with the text as a key, and a list of
        (x, y) for the center of the text location
        e.g. 'tailor' : [(123,123)]
        '''
        if len(ocr_results):
            results_dict = {}
            for result in ocr_results:
                word = result[1].lower()
                tl_x, tl_y = result[0][0]
                br_x, br_y = result[0][2]
                x = tl_x + ((br_x - tl_x) / 2).__round__() # Round for future use.
                y = tl_y + ((br_y - tl_y) / 2 ).__round__()
                
                if word in results_dict:
                    results_dict[word].append((x,y))
                else:
                    results_dict[word] = [(x,y)]

            return results_dict
        
    def find_uncommon_item(self):
        #Capture Trader inventory.
        trader_inventory = self.capture_trader_inventory()

        #Check for items in the merchant inventory.
        located_items = self.get_relevant_coords()

        for coords in located_items.values():
            for coord in coords:
                item_name = [k for k, v in located_items.items() if coord[0] in v[0]]
                x = coord[0]
                y = coord[1]
                pyautogui.moveTo(x, y, duration=.5)
                time.sleep(1)
                item_stats = self.get_item_stats_img(self.take_screenshot())

                if self.contains_green_item(item_stats):
                    print(f"{item_name} is uncommon")
                    uncommon_item = self.get_item_stats_img(self.take_screenshot())
                    return uncommon_item
    
    # Filters out blue stats (random stats)
    def get_uncommon_stat_img(self, screenshot: np.array) -> np.array:
        '''
        Filter out blue colored to text in the image
        return the numpy array for OCR.
        '''
        hsv_image = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)
        lower_blue = np.array([99, 55, 55])
        upper_blue = np.array([130, 255, 255])
        mask = cv.inRange(hsv_image, lower_blue, upper_blue)
        result = cv.bitwise_and(screenshot, screenshot, mask=mask)

        return result 
    
    def get_static_stat_img(self, screenshot: np.array) -> np.array:
        gray_screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        thresh = cv.threshold(gray_screenshot, 20, 255, type=1)
        return thresh[1]
    