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
from typing import Union


TOP_LEFT_X, TOP_LEFT_Y = 55,246
BOTTOM_RIGHT_X, BOTTOM_RIGHT_Y = 552, 991

class Screencap:
    def __init__(self):
        self.trader_inventory_TL = (55, 246)
        self.trader_inventory_BR = (552, 991)
        # self.item_names = os.listdir('images')
        # self.item_images = {image.split('.')[0] : cv.imread(f"images/{image}") \
        #                     for image in self.item_names}

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
    def get_item_stats_img(self, screenshot: np.array, index: int=1) -> np.array:
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

        x, y, w, h = cv.boundingRect(contours[index]) #May need to be adjusted 
        region = screenshot[y: y + h, x: x + w]

        return region

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
    
    def get_single_item_location(self, item_image_name: str, threshold: float) -> dict:
        '''
        item_image_name: image name from images/... Example --  "grimsmile.png"
        game_ss: Screenshot of trader inventory
        threshold: Threshold for sensitivity of template matching.
        '''
        item_locations = {}
        tl_x = self.trader_inventory_TL[0]
        tl_y = self.trader_inventory_TL[1]
        abs_imgs_path = 'C:/Users/mur819/Desktop/dnd_stats/images/'
        rel_imgs_path = 'images/'
        image = cv.imread(f"{abs_imgs_path}{item_image_name}")
        # image = cv.imread(f"images/{item_image_name}")

        results = find_item(self.capture_trader_inventory(), image, threshold=threshold)
                
        if results:
            adjusted_coords = []
            for result in results:
                x, y = result[0] + tl_x, result[1] + tl_y
                adjusted_coords.append((x,y))
            item_locations[item_image_name] = adjusted_coords
    
        return item_locations
    
    # Get a list of (x,y) coordinates for text on screen.
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
        
    # Filters out blue stats (random stats)
    # Performing OCR on image without cropping works just fine.
        # This function is mainly intended for logging items seen.
    def get_uncommon_stat_img(self, screenshot: np.array) -> np.array:
        '''
        Filter out blue colored to text in the image
        return the numpy array for OCR.
        '''
        hsv_image = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)
        # lower_blue = np.array([99, 55, 55])
        # upper_blue = np.array([130, 255, 255])
        lower_blue = np.array([55, 55, 55])
        upper_blue = np.array([130, 255, 255])

        mask = cv.inRange(hsv_image, lower_blue, upper_blue)
        result = cv.bitwise_and(screenshot, screenshot, mask=mask)

        return result 

    # Remove all characters except for integers.
    @staticmethod
    def filter_stat_value(string: str) -> Union[int, float, None]:
        stat_value = "".join([c for c in string if c.isnumeric() or c == '.'])
        if stat_value and '.' in stat_value:
            try:
                return float(stat_value)
            except Exception as e:
                # print(f"Unable to convert '{stat_value}' to float. {e}")
                pass
        else:
            try:
                return int(stat_value)
            except Exception as e:
                # print(f"Unable to convert '{stat_value}' to integer {e}")
                pass
        
        return None
    
    # Returns only characters, with leading/trailing white space removed.
    @staticmethod    
    def filter_stat_name(string: str) -> Union[str, None]:
        stat_name = "".join([c for c in string if c.isalpha() or c == " "]).strip()
        if stat_name:
            return stat_name
        return None
    
    def create_stats_dict(self, image: np.array, reader, all_stats: list[str]) -> dict:
        stats = {
            "random_stats" : {},
            "static_stats": {},
        }
        # start = time.perf_counter()
        # image = cv.fastNlMeansDenoising(image)
        # print(f"Denoising took: {time.perf_counter() - start}")
        results = reader.readtext(image, detail=False, paragraph=False, height_ths=.8, width_ths=.8)

        # Wolf hunter / demonclad legs share the same image. 
        if any('wolf hunter leggings' == item.lower() for item in results):
            stats['wolf hunter leggings'] = True
        elif any('demonclad leggings' == item.lower() for item in results):
            stats['demonclad leggings'] = True

        for line in results:
            random = False
            if "+" in line:
                random = True
            stat_name = self.filter_stat_name(line)
            stat_value = self.filter_stat_value(line)
            if stat_name and stat_name in all_stats:    
                if random:
                    stats['random_stats'][stat_name] = stat_value
                else:
                    stats['static_stats'][stat_name] = stat_value
        return stats
    
    def ensure_stats_dict(self, image: np.array, reader, all_stats: list[str]) -> dict:
        i = -1
        while True:
            i += 1
            if i == 10:
                return {}
            
            none_value = False
            stats_image = self.get_item_stats_img(image, i)
            stats_dict = self.create_stats_dict(stats_image, reader, all_stats)
            random_stats = stats_dict['random_stats'].values()
            static_stats = stats_dict['static_stats'].values()

            none_value = None in random_stats or None in static_stats
            if not none_value:
                print(f"Success: {i+1}/10 attempts.")
                return stats_dict
                
    def can_afford(self) -> bool:
        screenshot = self.take_screenshot()
        if screenshot[995][999][0] == 53:
            return True
        return False