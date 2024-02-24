import keyboard
import easyocr
import time
import cv2 as cv
from comp_vision.window_capture import Screencap
import pyautogui
from all_stats import stats, categories, create_item 
import os
from slots.ring import Ring
from comp_vision.item_finder import find_item


# Threshold for grimstone ring ~70
# Threshold for armorer .98


# Screencap object take and interact with screenshots.
screen_manager = Screencap()

# Reader to read text in images.
reader = easyocr.Reader(lang_list=['en'],
                        detector='dbnet18')

img_name = "tri-pelt doublet.png"
img_path = f"images/{img_name}"

item_locations = screen_manager.get_single_item_location(img_name, .8)

for key, value in item_locations.items():
    item_name = key
    coordinates = value[0]
    pyautogui.moveTo(x=coordinates[0], y=coordinates[1], duration=.8)
    time.sleep(.01)
    pyautogui.moveRel(1,1)
    time.sleep(1)
    current_screen = screen_manager.take_screenshot()
    stats_dict = screen_manager.ensure_stats_dict(current_screen, reader, stats)

    created_item = create_item(key, stats_dict, categories)
    print(created_item.num_stats)
    

