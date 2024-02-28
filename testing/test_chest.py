from time import perf_counter
import random
import os
import sys
# sys.path.insert(1, 'Users\\mur819\\Desktop\\dnd_stats\\slots')
sys.path.append("../")
from slots.chest import Chest

def create_random_chest(num_stats, item_name) -> Chest:
    stats = {
        "random_stats": {},
        "static_stats": {},
    }
    max_stats = Chest.max_stats
    i = 0   
    if item_name == "tri-pelt doublet":
        health_bonus = round(random.uniform(3.0, 5), 1)
        stats['static_stats']['Max Health Bonus'] = health_bonus

    while i != num_stats:        
        chosen_stat = random.choice(list(max_stats.keys()))
        if item_name == 'tri-pelt doublet':
            if chosen_stat == 'Max Health Bonus':
                continue

        if chosen_stat in stats:
            continue
        else:
            max_stat_value = max_stats.get(chosen_stat)
            if isinstance(max_stat_value, float):
                rand_stat_value = round(random.uniform(.1, max_stat_value), 1)
                stats['random_stats'][chosen_stat] = rand_stat_value
            else:
                rand_stat_value = random.randint(1, max_stat_value)
                stats['random_stats'][chosen_stat] = rand_stat_value
        i += 1
    
    return Chest(item_stats=stats, item_name=item_name)

def test_worth_buying(num_stats: int, item_name: str) -> Chest:
    count = 0
    finished = False
    while not finished:
        doublet = create_random_chest(num_stats, item_name)
        if doublet.worth_buying():
            finished = True
        count += 1
    print(f"Created {count:,} {item_name}'s before one was worth buying.")
    return doublet

start = perf_counter()
for _ in range(19):
    result = test_worth_buying(2, 'tri-pelt doublet')
    print(result)
print(f"This took {perf_counter() - start}")

start = perf_counter()
for _ in range(19):
    res = test_worth_buying(3, 'rubysilver doublet')
    print(res)
    print("\n")
print(f"This took {perf_counter() - start}")
