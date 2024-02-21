class Chest:
    max_stats = {
        "Max Health" : 6,
        "Armor Rating" : 10,
        "Physical Power": 5,
        "Magical Power": 5,
        "Magical Damage Bonus": 5.0,
        "Physical Damage Bonus": 5.0,
        "Physical Damage Reduction": 1.5,
        "Action Speed": 2.0,
        "Max Health Bonus": 3.0,

        "Vigor": 2,
        "Dexterity": 2,
        "Knowledge": 2,
        "Strength": 2,
        "Agility": 2,
        "Will": 2,
        "Resourcefulness": 2,

        # "Additional Physical Damage": 0,
        # "True Physical Damage": 0,
        # "Armor Penetration": 0,
        # "Additional Move Speed": 0,
        # "Move Speed Bonus": 0,  
        # "Additional Magical Damage": 0, 
        # "True Magical Damage": 0,
    }
    required_physical_stats = [
        'Max Health',
        'Max Health Bonus',
        'Physical Power',
        
    ]

    
    
    def __init__(self, item_stats: dict=None):
        self.item_stats = item_stats
        self.num_stats = len(item_stats) if item_stats else 0

    