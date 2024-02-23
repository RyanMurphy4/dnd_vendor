class Necklace:
    max_stats = {
    "Max Health" : 6,
    "Armor Rating" : 10,
    "Additional Move Speed": 3,
    "Move Speed Bonus": 1.0,
    "Additional Physical Damage": 3,
    "True Physical Damage": 3,
    "Additional Magical Damage": 3,
    "True Magical Damage": 3,
    "All Attributes": 1,
    "Armor Penetration": 2.5,
    "Physical Power": 5,
    "Magical Power": 5,
    "Magical Damage Bonus": 5.0,
    "Physical Damage Bonus": 5.0,
    "Physical Damage Reduction": 1.5,
    "Action Speed": 2.0,
    "Max Health Bonus": 3.0,
    "Vigor": 0,
    "Dexterity": 0,
    "Knowledge": 0,
    "Strength": 0,
    "Agility": 0,
    "Will": 0,
    "Resourcefulness": 0,            
    }

    def __init__(self, item_stats: dict):
        self.item_stats = item_stats

