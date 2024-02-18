import os
from slots.back import Back
from slots.chest import Chest
from slots.foot import Foot
from slots.hands import Hands
from slots.head import Head
from slots.legs import Legs
from slots.necklace import Necklace
from slots.ring import Ring
import random


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
                print("-- Ring already has a primary damage stat! --")
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
    return Ring(stats)

os.system('clear')
for _ in range(100):
    temp_ring = generate_random_ring(3)
    if temp_ring.worth_buying():
        print(f"{temp_ring=}")
        print("\n")


