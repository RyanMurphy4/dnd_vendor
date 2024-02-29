import random
import sys
sys.path.append("../")
from slots.foot import Foot


def create_random_foot(num_stats: int, item_name: str) -> Foot:
    stats = {
        "random_stats": {},
        "static_stats": {},
    }
    max_stats = Foot.max_stats
    i = 0

    while i != num_stats:
        chosen_stat = random.choice(list(max_stats.keys()))
        if item_name == 'rubysilver adventure boots':
            if chosen_stat == 'Dexterity':
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
    
    return Foot(stats, item_name=item_name)

def test_worth_buying(num_stats: int, item_name: str) -> Foot:
    count = 0
    finished = False
    while not finished:
        boots = create_random_foot(num_stats, item_name)
        if boots.worth_buying():
            finished = True
        count += 1

    print(f"Created: {count:,}")
    print(f"Item: {boots}")
    return boots

for _ in range(10):
    test_worth_buying(3, 'rubysilver adventure boots')
    print('\n')
