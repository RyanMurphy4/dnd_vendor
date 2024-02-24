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
    }
    required_physical_stats = [
        'Max Health',
        'Physical Power',
        'Max Health Bonus',
        'Physical Damage Bonus',
    ]

    comp_physical_stats = [
        "Action Speed",

    ]
    
    def __init__(self, item_stats: dict=None):
        self.item_stats = item_stats.get('random_stats', None)
        self.num_stats = len(item_stats.get('random_stats', ''))
        self.static_stats = item_stats.get('static_stats', None)
        
        
    def has_primary_stat(self):
        num_prim_stats = 0
        for stat, value in self.item_stats.items():
            if stat in self.required_physical_stats:
                if (self.max_stats.get(stat) - value) < .5:
                    num_prim_stats += 1
        return num_prim_stats
    
    def check_static_stat(self):
        num_static_stats = 0
        for stat, value in self.static_stats.items():
            if stat == 'Max Health Bonus': # Max health is the only static stat that changes.
                highest = 5.0
                if (highest - value) <= 1.2:
                    num_static_stats += 1
            else:
                num_static_stats += 1
        return num_static_stats

    def check_comp_physical_stats(self):
        comp_phys_stats = 0
        for stat, value in self.item_stats.items():
            if stat in self.comp_physical_stats:
                if (self.max_stats.get(stat) - value) <= .3:
                    comp_phys_stats += 1
        return comp_phys_stats

    def worth_buying():
        ...
        
    def __repr__(self) -> str:
        return f"{self.item_stats}"

    
