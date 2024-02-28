import sys
sys.path.append("../")
from typing import Tuple
import os
import time
import keyboard
from comp_vision.window_capture import Screencap

capper = Screencap()

def test_image(image_name: str) -> Tuple[str, int]:
    '''
    image_name: file name. Example: 'grimsile.png'
    '''
    start = .99
    found = False

    while not found:
        results = capper.get_single_item_location(image_name, threshold=start)
        if results:
            img_count = len(results.get(image_name, ' '))
            print(results)
        else:
            start -= .01 
            continue

        if img_count > 0:
            print(results)
            found = True
            break

        start -= .01
        
        if start <= .3:
            print("Very low thresholds often cause crashes.")
            print(f"Exiting... Threshold: {start}")
            break
    return image_name, start

image_name = 'cobalt leather gloves.png' # Item to be tested.
name, thresh = test_image(image_name)
# thresh = .95 # Overwrite determined threshold with specific threshold to test.

print(f"Item: {image_name} should have a threshold of {thresh:2f}")
print("\n")

def test_threshold(image: str, threshold: float) -> None:
    stop_condition = False
    while not stop_condition:
        if keyboard.is_pressed('q'):
            stop_condition = True
            time.sleep(.01)
        results = capper.get_single_item_location(image, threshold=threshold)
        num_items = len(results.get(image, ""))
        print(f"Number of matches: {num_items} at threshold {threshold}")
        time.sleep(.01)

test_threshold(image_name, thresh)