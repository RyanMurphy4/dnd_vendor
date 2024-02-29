class Head:
    max_stats = {
    "Max Health" : 4,
    "Armor Rating" : 5,
    "Additional Magical Damage": 2,
    "True Magical Damage": 2,
    "Physical Power": 3,
    "Magical Power": 3,
    "Magical Damage Bonus": 3.0,
    "Armor Penetration": 2.0,
    "Physical Damage Bonus": 3.0,
    "Physical Damage Reduction": 1.0,
    "Action Speed": 1.0,
    "Max Health Bonus": 2.0,
    "Vigor": 2,
    "Dexterity": 2,
    "Knowledge": 2,
    "Strength": 2,
    "Agility": 2,
    "Will": 2,
    "Resourcefulness": 2,
    }

    primary_magical_stats = [
        'Additional Magical Damage',
        'True Magical Damage',
    ]

    secondary_magical_stats = [
        'Magical Damage Bonus',
        'Magical Power',
    ]

    magical_attributes = [
        'Knowledge',
    ]

    health_stats = [
        'Max Health Bonus',
        'Max Health',
    ]

    comp_magical_stats = [
        'Agility',
    ]
    
    physical_stats = [
        'Physical Damage Bonus',
        'Physical Power',
    ]

    physical_attributes = [
        'Dexterity',
        'Action Speed',
    ]


    def __init__(self, item_stats: dict, item_name: str=None):
        self.item_name = item_name
        self.random_stats = item_stats.get('random_stats', None)
        self.num_random_stats = len(item_stats.get('random_stats', ''))
        self.static_stats = item_stats.get('static_stats', None)
        self.num_static_stats = len(item_stats.get('static_stats', ''))
        self.kuma_potential = False

    def check_stats(self, stat_list: list[str], threshold: int, f_threshold: float) -> int:
        '''
        stat_list: A list of stats that will be checked against max stats for that item type.
        threshold: Maximum difference allowed between stats that are type integer. Example: Physical Power
        f_threshold: Maximum difference allowed between stats that are type float. Example: Max Health Bonus
        
        returns: Number of stats that are within the threshold.
        '''
        num_stats = 0
        chosen_stats = []
        for stat, value in self.random_stats.items():  
            if stat in stat_list:
                if isinstance(value, float):
                    if (self.max_stats.get(stat) - value) <= f_threshold:
                        num_stats += 1
                        chosen_stats.append(stat)
                    
                elif (self.max_stats.get(stat) - value) <= threshold:
                    num_stats += 1
                    chosen_stats.append(stat)
        return num_stats, chosen_stats
    
    def buy_golden_hounskull(self) -> bool:
        num_prim_mag_stats, _= self.check_stats(self.primary_magical_stats, 0, 0)
        num_sec_mag_stats, sec_mag_stats = self.check_stats(self.secondary_magical_stats, 0, .5)
        num_mag_attrib, _ = self.check_stats(self.magical_attributes, 0, 0)
        num_health_stats, _= self.check_stats(self.health_stats, 1, .4)
        num_comp_mag_stats, _ = self.check_stats(self.comp_magical_stats, 0, 0)

        num_phys_stats, phys_stats = self.check_stats(self.physical_stats,  0, .5)
        num_phys_attrib, _ = self.check_stats(self.physical_attributes, 0, .3)
    
        # For now skip completely if it doesn't have ANY additional health
        if not num_health_stats:
            return False
        
        # Good for Kumas
        if num_prim_mag_stats: 
            if num_phys_stats:
                if num_phys_attrib == 1:
                    print(f"GOOD FOR KUMAS: {self.random_stats}\n")
                    return True
        
        # Good for cleric
        if num_prim_mag_stats: # Add/True magical damage
            if num_mag_attrib: # Knowledge
                if num_comp_mag_stats or num_sec_mag_stats: # Agility or magic power/ magic damage
                    print(f"GOOD FOR CLERIC: {self.random_stats}\n")
                    return True
    
        return False

    def worth_buying(self) -> bool:
        if self.item_name == 'golden hounskull':
            if self.buy_golden_hounskull():
                return True
            
        return False
    def __repr__(self):
        return f"static_stats: {self.static_stats}\nrandom_stats: {self.random_stats}"