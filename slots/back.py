class Back:
    max_stats = {
    "Max Health" : 4,
    "Armor Rating" : 5,
    "Armor Penetration": 2.5,
    "Physical Power": 3,
    "Magical Power": 3,
    "Magical Damage Bonus": 3.0,
    "Physical Damage Bonus": 3.0,
    "Physical Damage Reduction": 1.0,
    "Action Speed": 2.0,
    "Max Health Bonus": 2.0,
    "Additional Move Speed": 3,
    "Move Speed Bonus": 1.0,  
    "Additional Physical Damage": 2,
    "True Physical Damage": 2,
    "Additional Magical Damage": 2, 
    "True Magical Damage": 2,
    "Vigor": 0,
    "Dexterity": 0,
    "Knowledge": 0,
    "Strength": 0,
    "Agility": 0,
    "Will": 0,
    "Resourcefulness": 0,
    }

    def __init__(self, item_stats: dict=None, item_name: str=None):
        self.item_name = item_name
        self.item_stats = item_stats
