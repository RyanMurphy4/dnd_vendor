from slots.back import Back
from slots.chest import Chest
from slots.foot import Foot
from slots.hands import Hands
from slots.head import Head
from slots.legs import Legs
from slots.necklace import Necklace
from slots.ring import Ring
from typing import Union
import os

stats = [
    'Action Speed',
    'Agility',
    'All Attributes',
    'Armor Penetration',
    'Armor Rating',
    'Buff Duration Bonus',
    'Debuff Duration Bonus',
    'Dexterity',
    'Knowledge',
    'Magic Penetration',
    'Magic Resistance',
    'Additional Magical Damage',
    'Magical Damage',
    'Magical Damage Bonus',
    'Magical Damage Reduction',
    'True Magical Damage',
    'Magical Healing',
    'Magical Interaction Speed',
    'Magical Power',
    'Max Health',
    'Max Health Bonus',
    'Additional Memory Capacity',
    'Memory Capacity Bonus',
    'Additional Move Speed',
    'Move Speed Bonus',
    'Additional Physical Damage',
    'Physical Damage Bonus',
    'Physical Damage Reduction',
    'True Physical Damage',
    'Physical Healing',
    'Physical Power',
    'Weapon Damage',
    'Projectile Damage Reduction',
    'Regular Interaction Speed',
    'Resourcefulness',
    'Spell Casting Speed',
    'Strength',
    'Vigor',
    'Will',
    'Move Speed',
    'Luck',
]

# Maybe make tuple to hold threshold also?
categories = {
    "cobal leather gloves.png": (Hands, .87),
    "cobalt lightfoot boots.png": (Foot, .69),
    "cobalt trousers.png": (Legs, .81),
    "demon grip gloves.png": (Hands, .99),
    # "golden armet.png": (Head, .0),
    # "golden gauntlets.png": (Hands, .0),
    "golden gjermundbu.png": (Head, .99),
    "golden hounskull.png": (Head, .99),
    "golden plate boots.png": (Foot, .99),
    "golden plate pants.png": (Legs, .99),
    "golden plate.png": (Chest, .99),
    "grimsmile.png": (Ring, .81),
    "heavy leather leggings.png": (Legs, .99), # NEED A WAY TO DIFFERENTIATE BETWEEN BOTH LEGS.
    "rubysilver adventurer boots.png": (Foot, .99),
    "rubysilver barbuta helm.png": (Head, .99),
    "rubysilver cap.png": (Head, .99),
    "rubysilver doublet.png": (Chest, .98),
    # "rubysilver gauntlets.png": Hands,
    # "rubysilver hood.png": Head, # Would maybe be worth it if gold isn't available.
    # "rubysilver leggings.png": Legs,
    # "rubysilver plate boots.png": Foot,
    # "rubysilver plate pants.png": Legs,
    # "rubysilver plate.png": Chest,
    "rubysilver rawhide gloves.png": (Hands, .81), # Cannot differentiate between leather and rubysilver leather
    # "rubysilver vestments.png": Chest, # Not Currently worth buying??
    "tri-pelt doublet.png" : (Chest, .95), # Can't even mouse over item or it won't detect it.
    }

def create_item(img_name: str, stats: dict, categories: dict) -> Union[Back, Chest, Foot, Hands, Head, Legs, Necklace, Ring]:
    item_name = img_name.replace('.png', '')
    item_type = categories[img_name][0]
    return item_type(stats, item_name)

    
