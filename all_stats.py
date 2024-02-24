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
    "cobal leather gloves.png": Hands,
    "cobalt lightfoot boots.png": Foot,
    "demon grip gloves.png": Hands,
    "golden armet.png": Head,
    "golden gauntlets.png": Hands,
    "golden gjermundbu.png": Head,
    "golden hounskull.png": Head,
    "golden plate boots.png": Foot,
    "golden plate pants.png": Legs,
    "golden plate.png": Chest,
    "grimsmile.png": Ring,
    "heavy leather leggings.png": Legs,
    "rubysilver adventurer boots.png": Foot,
    "rubysilver barbuta helm.png": Head,
    "rubysilver cap.png": Head,
    "rubysilver doublet.png": Chest,
    "rubysilver gauntlets.png": Hands,
    "rubysilver hood.png": Head,
    "rubysilver leggings.png": Legs,
    "rubysilver plate boots.png": Foot,
    "rubysilver plate pants.png": Legs,
    "rubysilver plate.png": Chest,
    "rubysilver rawhide gloves.png": Hands,
    "rubysilver vestments.png": Chest,
    "tri-pelt doublet.png": Chest,
    }

def create_item(img_name: str, stats: dict, categories: dict) -> Union[Back, Chest, Foot, Hands, Head, Legs, Necklace, Ring]:

    item_type = categories[img_name]
    return item_type(stats)

    
