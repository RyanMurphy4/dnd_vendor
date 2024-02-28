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


def click_service(duration: int=1) -> None:
    # x = 299
    # y = 146

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


# Threshold for grimstone ring ~70
# Threshold for armorer .98
service = (299, 146)

# Screencap object take and interact with screenshots.
screen_manager = Screencap()

# Reader to read text in images.
reader = easyocr.Reader(lang_list=['en'],
                        detector='dbnet18')

# img_name = "tri-pelt doublet.png"
# img_path = f"images/{img_name}"

# item_locations = screen_manager.get_single_item_location(img_name, .8)

# for key, value in item_locations.items():
#     item_name = key
#     coordinates = value[0]
#     pyautogui.moveTo(x=coordinates[0], y=coordinates[1], duration=.8)
#     time.sleep(.01)
#     pyautogui.moveRel(1,1)
#     time.sleep(1)
#     current_screen = screen_manager.take_screenshot()
#     stats_dict = screen_manager.ensure_stats_dict(current_screen, reader, stats)

#     created_item = create_item(key, stats_dict, categories)
#     print(created_item.num_stats)


directory = "images/"
image_names = os.listdir(directory)

screenshot = screen_manager.take_screenshot()
results = reader.readtext(screenshot, detail=True, paragraph=False)
text_locations = screen_manager.get_text_locs(results)

skip_for_now = [
    'rubysilver hood.png',
    'rubysilver vestments.png',
]
merchants_to_browse = [ 
    'alchemist', 
    'tailor'
]

for merch in merchants_to_browse:
    browse_merchant(merch, text_locations)
    time.sleep(.3)
    click_service(.2)
    
    for image in image_names:
        if isinstance(categories.get(image), tuple):
            thresh = categories.get(image)[1]
        else:
            continue
        
        # Template matching to find image inside of traders inventory.
        item_locations = screen_manager.get_single_item_location(image, thresh)

        for key, value in item_locations.items():
            if key in skip_for_now:
                print(f"Skipping item {key} until .worth_buying() is implemented.\n")
                time.sleep(.5)
                continue

            coordinates = value[0]
            pyautogui.moveTo(x=coordinates[0], y=coordinates[1], duration=.4)
            time.sleep(.1)
            pyautogui.moveRel(1,1)
            pyautogui.moveRel(1,1)
            pyautogui.moveRel(1,1)
            time.sleep(1)
            current_screen = screen_manager.take_screenshot()
            stats_dict = screen_manager.ensure_stats_dict(current_screen, reader=reader, all_stats=stats)

            item = create_item(key, stats_dict, categories)
            print("\n")
            print(f"Created Item: {item}")
            print(f"This time is worth buying: {item.worth_buying()}")
            print('\n')
            time.sleep(1)
            pyautogui.moveTo(x=999, y=995)
            time.sleep(1)


    print(f"Finished with {merch}")
    time.sleep(1)
    keyboard.press('escape')
    time.sleep(.1)
    keyboard.release('escape')
    time.sleep(1)



