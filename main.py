from datetime import datetime
import keyboard
import easyocr
import time
import cv2 as cv
from comp_vision.window_capture import Screencap
import pyautogui
from all_stats import stats, categories
from testing.create_item import create_item
import os
from slots.ring import Ring
from slots.legs import Legs
from comp_vision.item_finder import find_item

def click_service(duration: int=1) -> None:
    # x, y = 299, 146
    time.sleep(.3)
    pyautogui.moveTo(x=299, y=146, duration=duration)
    time.sleep(.2)
    pyautogui.click()

def browse_merchant(merchant_name: str, text_locations: dict) -> None:
    merchant = text_locations[merchant_name][0]
    merch_x = merchant[0]
    merch_y = merchant[1]

    time.sleep(1)
    pyautogui.moveTo(x=merch_x, y=merch_y, duration=.3)
    time.sleep(1)
    pyautogui.click()

def jiggle_mouse(iterations: int) -> None:
    for _ in range(iterations):
        pyautogui.moveRel(1,1)
        time.sleep(.01)
        pyautogui.moveRel(-1, -1)
        time.sleep(.01)
        
def move_mouse_from_items() -> None:
    pyautogui.moveTo(0,0)

def get_log_dir() -> str:
    seen_items_dir = "seen_items/"
    current_date = datetime.now().strftime('%Y-%m-%d')
    if os.path.isdir(seen_items_dir):
        print("Directory Already exists")
    else:
        print("Directory containing items encountered doesn't exist")
        print(f"Creating directory '{seen_items_dir}' now.")
        os.mkdir(seen_items_dir)
        print("Directory Created.")
    
    if os.path.isdir(f"seen_items/{current_date}/"):
        print(f"Directory for '{current_date}' has already been created.")
    else:
        os.mkdir(f"seen_items/{current_date}/")
    
    return f"{seen_items_dir}{current_date}/"

def get_nums_from_time()-> str:
    current_time = time.time()
    after_dec = str(current_time).split('.')[-1]
    
    return after_dec

def get_image_name(slots_item, dir_path: str) -> str:
    images = os.listdir(dir_path)
    item_name = slots_item.item_name
    same_type_images = [image for image in images if item_name in image]
    highest = 0 if same_type_images else None

    
    if highest != None:
        for image in same_type_images:
            try:
                num = int("".join([c for c in image if c.isdigit()]))
                if num > highest:
                    highest = num
            except Exception as e:
                print(f"An error occured parsing image number: {e}")
        highest += 1
    elif highest == None:
        highest = 0

    return f"{dir_path}{item_name}-{highest}.png"

def save_item():
    legs = create_item('legs', 'demonclad leggings', 2)
    x = get_image_name(legs, get_log_dir())
    with open(f"{x}.txt", 'w') as f:
        f.write('Yo!')

    print(x)

def save_to_log(image):
    ...

service = (299, 146)

# Screencap object take and interact with screenshots.
screen_manager = Screencap()

# Reader to read text in images.
reader = easyocr.Reader(lang_list=['en'],
                        detector='dbnet18')


save_item()