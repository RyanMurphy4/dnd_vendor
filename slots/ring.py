class Ring:
    def __init__(self, item_stats: dict):
        self.item_stats = item_stats
        self.num_stats = len(item_stats)
        self.max_stats = {
            "Max Health" : 4,
            "Armor Rating" : 5,
            "Additional Move Speed": 3,
            "Move Speed Bonus": 1.0,
            "Additional Physical Damage": 2,
            "True Physical Damage": 2,
            "Additional Magical Damage": 2,
            "True Magical Damage": 2,
            "Armor Penetration": 1.5,
            "Physical Power": 3,
            "Magical Power": 3,
            "Magical Damage Bonus": 3.0,
            "Physical Damage Bonus": 3.0,
            "Physical Damage Reduction": 1.0,
            "Action Speed": 1.0,
            "Max Health Bonus": 2.0,
            "Vigor": 0,
            "Dexterity": 0,
            "Knowledge": 0,
            "Strength": 0,
            "Agility": 0,
            "Will": 0,
            "Resourcefulness": 0, 
        }

        self.magical_stats = [
            'Additional Magical Damage',
            'True Magical Damage',
            'Magical Power',
            'Magical Damage Bonus'
        ]

        self.physical_stats = [
            'Additional Physical Damage',
            'True Physical Damage',
            'Physical Power',
            'Physical Damage Bonus'
        ]

    def compare_stats(self):
        magic = self.is_magic_ring()
        physical = self.is_physical_ring()
        if magic or physical:
            diff = 0
            for stat, value in self.item_stats.items():
                diff += self.max_stats.get(stat) - value
                print(diff)
                if diff > .5:
                    return False
        return True
                


            

    def __repr__(self) -> str:
        return f"{self.item_stats}"
    
    def is_magic_ring(self):
        for stat in self.item_stats.keys():
            if stat not in self.magical_stats:
                return False
        return True
    
    def is_physical_ring(self):
        for stat in self.item_stats.keys():
            if stat not in self.physical_stats:
                return False
        return True



