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

    physical_stats = [
        'Physical Power',
        'Physical Damage Bonus',
    ]

    health_stats = [
        'Max Health',
        'Max Health Bonus',
    ]

    comp_stats_tripelt = [
        'Dexterity',
        'Action Speed',
    ]

    comp_stats_rubysilver = [
        'Action Speed',
        'Vigor'
    ]
    def __init__(self, item_stats: dict=None, item_name: str=None):
        self.item_name = item_name
        self.random_stats = item_stats.get('random_stats', None)
        self.num_random_stats = len(item_stats.get('random_stats', ''))
        self.static_stats = item_stats.get('static_stats', None)
        self.num_static_stats = len(item_stats.get('static_stats', ''))
         
    def check_static_health(self, threshold) -> bool:
        health_value = self.static_stats.get('Max Health Bonus')
        if not health_value:
            return False
    
        max_value = 5.0

        if (max_value - health_value) <= threshold:
            return True
        return False
    
    def check_stats(self, stat_list: list[str], threshold: int, f_threshold: float) -> int:
        '''
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
    
    def buy_tripelt(self) -> bool:
        if not self.check_static_health(1.2):
            return False
        
        num_phys_stats, phys_stats = self.check_stats(self.physical_stats, 0, .5)
        num_health_stats, phys_stats = self.check_stats(self.health_stats, 1, 0)
        num_comp_stats, comp_stats = self.check_stats(self.comp_stats_tripelt, 0, .2)

        if num_phys_stats == 2: # Phys damage AND Phys power
            return True
        if num_phys_stats + num_health_stats == 2: # (phys damage OR phys power) AND (max health)
            return True
        if (num_phys_stats == 1 or num_health_stats == 1) and num_comp_stats == 1: # (Phys damage or Phys power) or (max health) AND (dex OR action speed)
            return True
        return False
    
    def buy_ruby_doublet(self) -> bool:
        num_phys_stats, phys_stats = self.check_stats(self.physical_stats, 0, .5)
        num_health_stats, health_stats = self.check_stats(self.health_stats, 1, .5)
        num_comp_stats , comp_stats = self.check_stats(self.comp_stats_rubysilver, 0, .3)

        total = sum([num_phys_stats, num_health_stats, num_comp_stats])
        if total:
            if not total % 3:
                print("stopped at sum")
                return True
        
        if num_phys_stats == 2: 
            if num_health_stats or num_comp_stats:
                print("Stopped at num_phys_stats")
                return True
        if num_health_stats == 2:
            if num_phys_stats or num_comp_stats:
                print("Stopped at num_health_stats")
                return True
        
        return False
         
    def worth_buying(self):
        if self.item_name == 'tri-pelt doublet':
            return self.buy_tripelt()
            
        elif self.item_name == 'rubysilver doublet':
            return self.buy_ruby_doublet()
        
        return False
            
    def __repr__(self) -> str:
        return f"Name: {self.item_name}\nrandom_stats={self.random_stats}\nstatic_stats={self.static_stats}"

    
