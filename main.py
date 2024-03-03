from datetime import datetime
import keyboard
import easyocr
import time
import cv2 as cv
from comp_vision.window_capture import Screencap
import pyautogui
from all_stats import stats, categories, create_item
# from testing.create_item import create_item
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

    time.sleep(.5)
    pyautogui.moveTo(x=merch_x, y=merch_y, duration=.3)
    time.sleep(1)
    pyautogui.click()

def jiggle_mouse(iterations: int) -> None:
    for _ in range(iterations):
        pyautogui.moveRel(1,1)
        time.sleep(.01)
        pyautogui.moveRel(-1, -1)
        time.sleep(.2)
        
def move_mouse_from_items() -> None:
    time.sleep(.1)
    pyautogui.moveTo(100,100)
    time.sleep(.1)

def get_log_dir() -> str:
    seen_items_dir = "seen_items/"
    current_date = datetime.now().strftime('%Y-%m-%d')
    if not os.path.isdir(seen_items_dir):
        print("Directory containing items encountered doesn't exist")
        print(f"Creating directory '{seen_items_dir}' now.")
        os.mkdir(seen_items_dir)
        print("Directory Created.")
    
    if not os.path.isdir(f"seen_items/{current_date}/"):
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

def save_to_log(item, image):
    img_name = get_image_name(item, get_log_dir())
    cv.imwrite(img_name, image)
    print(f"{img_name} saved to log.")

service = (299, 146)
# Screencap object take and interact with screenshots.
screen_manager = Screencap()

# Reader to read text in images.
reader = easyocr.Reader(lang_list=['en'],
                        detector='dbnet18')

merchants = [
    'Alchemist',
    'Armourer',
    'Leathersmith',
    'Tailor'
]
images = os.listdir('images/')
screenshot = screen_manager.take_screenshot()
results = reader.readtext(screenshot)
merchant_locations = screen_manager.get_text_locs(results)

for merchant in merchants:
    browse_merchant(merchant.lower(), merchant_locations)
    click_service(.1)
    for image_name in images:
        if categories.get(image_name) is None:
            continue
        item_type, image_thresh = categories.get(image_name)
        item_locations = screen_manager.get_single_item_location(image_name,
                                                                image_thresh)
        # Will have to check here for demonclad/wolfhunter and handle it.
        if item_locations:
            x, y = item_locations.get(image_name)[0]
            pyautogui.moveTo(x, y, duration=.3)
            jiggle_mouse(3)
            screenshot = screen_manager.take_screenshot()
            stats_dict, stats_image = screen_manager.ensure_stats_dict(
                                                          screenshot,
                                                          reader,
                                                          stats)

            created_item = create_item(image_name, stats_dict, categories)
            save_to_log(created_item, stats_image)
            worth = created_item.worth_buying()
            print(f"{image_name} worth buying? {worth}")
            print("\n")
            print(created_item)
            move_mouse_from_items()
            time.sleep(.5)
            # ADD LOGIC TO PURCHASE ITEM
    keyboard.press('escape')
    time.sleep(.01)
    keyboard.release('escape')
    time.sleep(.1)