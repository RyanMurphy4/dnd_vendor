import sys 
sys.path.append("../")
from typing import Union
from slots.back import Back
from slots.chest import Chest
from slots.foot import Foot
from slots.hands import Hands
from slots.head import Head
from slots.legs import Legs
from slots.necklace import Necklace
from slots.ring import Ring
import random

item_types = {
    "back": Back,
    "chest": Chest,
    "foot": Foot,
    "hands": Hands,
    "head": Head,
    "legs": Legs,
    "necklace": Necklace,
    "ring": Ring,
}



def create_item(item_type: str, item_name: str, num_stats: int) -> Union[Back,
                                                                         Chest,
                                                                         Foot,
                                                                         Hands,
                                                                         Head,
                                                                         Legs,
                                                                         Necklace,
                                                                         Ring]:
    '''
    item_type (str): Type of 'slot' item to create. Example: 'back'

    item_name (str): Name of item being created. Example: 'rubysilver doublet'

    num_stats (int): Number of stats the required item will have.
    '''

    class_type = item_type.lower()
    stats = {
    "random_stats": {},
    "static_stats": {},
    }

    class_type = item_types.get(class_type)
    max_stats = class_type.max_stats
    i = 0

    if item_name == 'tri-pelt doublet':
        health_bonus = round(random.uniform(3.0, 5), 1)
        stats['static_stats']['Max Health Bonus']= health_bonus

    while i != num_stats:
        chosen_stat = random.choice(list(max_stats.keys()))

        # Ignore static stat, since you can't roll existing static stats as random stats.
        if item_name == 'rubysilver adventure boots' or item_name == 'rubysilver doublet':
            if chosen_stat == 'Dexterity':
                continue
        if item_name == 'tri-pelt doublet':
            if chosen_stat == 'Max Health Bonus':
                continue
        if item_name == 'golden hounskull':
            if chosen_stat == 'Vigor':
                continue
        if chosen_stat in stats['random_stats']:
            continue
        
        chosen_stat_max = max_stats.get(chosen_stat)
        if isinstance(chosen_stat_max, float):
            stat_value = round(random.uniform(.1, chosen_stat_max), 1)
            stats['random_stats'][chosen_stat] = stat_value
        else:
            stat_value = random.randint(1, chosen_stat_max)
            stats['random_stats'][chosen_stat] = stat_value
        
        i += 1

    return class_type(stats, item_name=item_name)

def test_worth_buying(item_type: str, item_name: str, num_stats: int) -> None:

    '''
    item_type (str): Slot that item belongs to Example: 'chest'

    item_name (str): Name of item being created. Example: 'rubysilver doublet'

    num_stats (int): Number of stats the required item will have.
    '''
    count = 0
    stop_condition = False

    while not stop_condition:
        temp_item = create_item(item_type, item_name, num_stats)
        
        if temp_item.worth_buying():
            stop_condition = True

        count += 1
    
    print(f"Created: {count} {item_name}'s before one was worth buying.")
    print(f"{item_name}: {temp_item}")
    print('\n')
    

# golden gjermundbu
    
    
# cobalt leather gloves
#test_worth_buying('hands', 'cobalt leather gloves', 2)

for _ in range(10):
    test_worth_buying('hands', 'cobalt leather gloves', 2)



