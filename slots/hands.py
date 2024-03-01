class Hands:
    max_stats = {
    "Max Health" : 4,
    "Armor Rating" : 5,
    "Additional Physical Damage": 2,
    "True Physical Damage": 2,
    "Armor Penetration": 2.0,
    "Physical Power": 3,
    "Magical Power": 3,
    "Magical Damage Bonus": 3.0,
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
    
    primary_physical_stats = [
        "Additional Physical Damage",
        "True Physical Damage",
    ]

    secondary_physical_stats = [
        "Physical Power",
        "Physical Damage Bonus"
    ]

    comp_physical_stats = [
        "Action Speed"
    ]

    health_stats = [
        "Max Health Bonus",
        "Max Health"
    ]

    magical_stats = [
        "Magical Damage Bonus",
        "Magical Power"
    ]

    def __init__(self, item_stats: dict, item_name: str=None):
        self.item_name = item_name
        self.random_stats = item_stats.get('random_stats')
        self.num_random_stats = len(item_stats.get('random_stats', ''))
        self.static_stats = item_stats.get('static_stats')
        self.num_static_stats = len(item_stats.get('static_stats', ''))

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
        
    def buy_cobalt_gloves(self) -> bool:
        num_prim_phys_stats, _ = self.check_stats(self.primary_physical_stats, 0, 0)
        num_sec_phys_stats, _ = self.check_stats(self.secondary_physical_stats, 0, .2)
        num_health_stats, _ = self.check_stats(self.health_stats, 0, .3)

        if not num_prim_phys_stats:
            return False
        else:
            if num_sec_phys_stats:
                return True
            if num_health_stats:
                return True
            return False

    def buy_rubysilver_gloves(self) -> bool:
        num_magical_stats, _ = self.check_stats(self.magical_stats, 0, .3)
        num_health_stats, _ = self.check_stats(self.health_stats, 1, .3)
        has_vigor, _ = self.check_stats(['Vigor'], 0, 0)
        total = num_magical_stats + num_health_stats + has_vigor

        if num_health_stats + has_vigor == 3:
            return True
        
        if num_magical_stats:
            pass
        if total == 3:
            return True
        else:
            return False
        
    def buy_demon_gloves(self) -> bool:
        if self.static_stats.get('Magical Healing') != 3:
            return False
        num_mag_stats, magic_stats = self.check_stats(self.magical_stats, 0, .3)
        num_health_stats, health_stats = self.check_stats(self.health_stats, 0, .3)
        knowledge, _ = self.check_stats(['Knowledge'], 0, 0)
        vigor, _ = self.check_stats(['Vigor'], 0, 0)
        total = num_mag_stats + num_health_stats + knowledge

        if 'Max Health' in health_stats:
            if vigor:
                return True
        
        if total == 2:
            return True
        return False

    def worth_buying(self) -> bool:
        if self.item_name == 'cobalt leather gloves':
            if self.buy_cobalt_gloves():
                return True
            
        if self.item_name == 'rubysilver rawhide gloves':
            if self.buy_rubysilver_gloves():
                return True
            
        if self.item_name == 'demon grip gloves':
            if self.buy_demon_gloves():
                return True
        return False
    
    def __repr__(self) -> str:
        return f"random_stats: {self.random_stats}"