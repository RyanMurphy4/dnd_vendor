import keyboard
import easyocr
import time
import cv2 as cv
from comp_vision.window_capture import Screencap
import pyautogui
from all_stats import stats
import os
from slots.ring import Ring

# Threshold for grimstone ring ~70
# Threshold for armorer .98

##TODO
# Fix problem capturing grimsmile ring stats.
    # Either move mouse slightly, then try again
    # iterate through the list of contours in screencap.get_item_stats()

# Function for testing template matching in various vendor environments
def test_template_matching(threshold: float) -> dict:
    '''
    - threshold (float): Determines the sensitivity of the template matching algorithm.
    Lower values make the algorithm more sensitive.
    '''
    screen_manager = Screencap()

    res = screen_manager.get_relevant_coords(threshold)
    items_found = 0
    for item, coord in res.items():
        
        for point in coord:
            x = point[0]
            y = point[1]
            pyautogui.moveTo(x,y, .1)
            time.sleep(1)
            print(item)
            items_found += 1
    print(f"Items found: {items_found}")

    return res

# Test OCR on results from screencap.get_item_stats()
    # resizing to (500, 500) solves the problem in detecting "+1"
    # height_ths=.9
    # width_ths.9

def test_ocr(image, display: bool=None) -> None:
    comp_vision = Screencap()
    results = reader.readtext(image, detail=False, paragraph=False, height_ths=.9, width_ths=.9)

    if display:
        cv.imshow('Your Image.', image)
        cv.waitKey(0)
    return results

sc = Screencap()
reader = easyocr.Reader(lang_list=['en'],
                        detector='dbnet18')


