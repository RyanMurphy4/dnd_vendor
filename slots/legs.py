class Legs:
    def __init__(self, item_stats: dict):
        self.item_stats = item_stats

        self.max_stats = {
            "Max Health" : 6,
            "Armor Rating" : 10,
            "Additional Move Speed": 5,
            "Move Speed Bonus": 1.5,
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
            "Additional Physical Damage": 0,
            "True Physical Damage": 0,
            "Additional Magical Damage": 0,
            "True Magical Damage": 0,
            "Armor Penetration": 0,            
        }
    
    def __repr__(self) -> str:
        return f"{self.item_stats}"