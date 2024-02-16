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
    "Magical Damage Bonus": 2.5,
    "Additional Magical Damage": 2,
    'Magical Power': 3,
    # "Additional Physical Damage": 1,
    # "Physical Power": 1,
    
}

new_ring = Ring(stats)
decision = new_ring.compare_stats()

if decision:
    print("Buy the ring")
else:
    print("don't buy the ring")




