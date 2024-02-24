import os
import sys
# sys.path.insert(1, 'Users\\mur819\\Desktop\\dnd_stats\\slots')
sys.path.append("../")
from slots.back import Back
from slots.chest import Chest
from slots.foot import Foot
from slots.hands import Hands
from slots.head import Head
from slots.legs import Legs
from slots.necklace import Necklace
from slots.ring import Ring
import random
import keyboard
import time
import easyocr
from comp_vision.window_capture import Screencap
from all_stats import stats


stats = {
    "Magical Damage Bonus": 2.7,
    "Additional Physical Damage": 2,
    # "Additional Magical Damage": 1,
    "Additional Move Speed": 3
    # 'Magical Power': 3,
    # "Physical Power": 1,
}


def generate_random_ring(num_stats) -> Ring:
    max_stats = Ring.max_stats
    primary_damage_stats = Ring.primary_damage_stats
    stats = {}
    i = 0
    has_2_damage = False
    while i != num_stats:
        chosen_stat = random.choice(list(max_stats.keys()))
        if chosen_stat in stats.keys():
            continue
        if chosen_stat in primary_damage_stats:
            if has_2_damage:
                continue
            else:
                has_2_damage = True
        chosen_stat_max = max_stats.get(chosen_stat)
        if isinstance(chosen_stat_max, float):
            generated_stat_value = round(random.uniform(0.1, chosen_stat_max), 1)
            
        else:
            generated_stat_value = random.randint(1, chosen_stat_max)
        stats[chosen_stat] = generated_stat_value
        i += 1
    return Ring(stats, "Doesn't matter")


def test_rings(num_rings: int, verbose=False) -> int:
    '''
    num_rings: Number of rings that will be created and checked.

    Returns number of rings that satisfy purchase requirements
    '''
    worth = 0 
    for _ in range(num_rings):
        temp_ring = generate_random_ring(3)
        if temp_ring.worth_buying():
            if verbose:
                print(f"{temp_ring=}")
                print("\n")
            worth += 1
    if verbose:
        print(f"Total rings purchased: {worth}/{num_rings}")
    return worth


def test_get_stats_dict(reader):
    sc = Screencap()
    while True:
        if keyboard.is_pressed('k'):
            os.system('clear')
            screenshot = sc.take_screenshot()

            stats_dict = sc.ensure_stats_dict(screenshot, reader, stats)
            
            if stats_dict.get('random_stats') and stats_dict.get('static_stats'):
                print(stats_dict.get('item_name') + '\n')
                print(f"Random_stats: {stats_dict['random_stats']}")
                print('\n')
                print(f"static_stats: {stats_dict['static_stats']}")

        if keyboard.is_pressed('q'):
            exit()

        time.sleep(.02)




if __name__ == "__main__":
    reader = easyocr.Reader(lang_list=['en'],
                            detector='dbnet18')
    test_get_stats_dict(reader=reader)