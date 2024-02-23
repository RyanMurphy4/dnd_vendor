class Foot:
    max_stats = {
    "Max Health" : 4,
    "Armor Rating" : 5,
    "Additional Physical Damage": 0,
    "True Physical Damage": 0,
    "Armor Penetration": 0,
    "Magical Power": 3,
    "Physical Power": 3,
    "Physical Damage Bonus": 3.0,
    "Magical Damage Bonus": 3.0,
    "Physical Damage Reduction": 1.0,
    "Action Speed": 0,
    "Max Health Bonus": 2.0,
    "Vigor": 2,
    "Dexterity": 2,
    "Knowledge": 2,
    "Strength": 2,
    "Agility": 2,
    "Will": 2,
    "Resourcefulness": 2,
    "Additional Move Speed": 5,
    "Move Speed Bonus": 1.5,  
    "Additional Magical Damage": 0, 
    "True Magical Damage": 0, 
    }   

    def __init__(self, item_stats: dict):
        self.item_stats = item_stats

