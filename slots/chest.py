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
        "Magical Healing": 3,

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

    # Won't be used until gold, mystic vestments isn't worth.
    required_magical_stats = [
        'Max Health',
        'Max Health Bonus',
        'Magical Power',
        "Magical Damage Bonus"
    ]

    comp_physical_stats = [
        "Action Speed",
    ]
    
    acceptable_physical_stats = [
        'Vigor',
        'Dexterity',
        'Strength',
    ]
    
    def __init__(self, item_stats: dict=None, item_name: str=None):
        self.item_name = item_name
        self.item_stats = item_stats.get('random_stats', None)
        self.num_stats = len(item_stats.get('random_stats', ''))
        self.static_stats = item_stats.get('static_stats', None)
        self.num_static_stats = len(item_stats.get('static_stats'), '')
         
    def check_primary_stats(self):
        num_prim_stats = 0
        for stat, value in self.item_stats.items():
            if stat in self.required_physical_stats:
                if (self.max_stats.get(stat) - value) < .5:
                    num_prim_stats += 1
        return num_prim_stats
    
    def check_static_stats(self):
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
    
    def check_acceptable_physical_stats(self):
        acceptable_phys_stats = 0
        for stat, value in self.item_stats.items():
            if stat in self.acceptable_physical_stats:
                if (self.max_stats.get(stat) - value) == 0:
                    acceptable_phys_stats += 1

        return acceptable_phys_stats

    def worth_buying(self):
        ...
        

        
        
    def __repr__(self) -> str:
        return f"{self.item_stats}"

    
