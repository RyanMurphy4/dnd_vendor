class Foot:
    max_stats = {
    "Max Health" : 4,
    "Armor Rating" : 5,
    "Magical Power": 3,
    "Physical Power": 3,
    "Physical Damage Bonus": 3.0,
    "Magical Damage Bonus": 3.0,
    "Physical Damage Reduction": 1.0,
    "Max Health Bonus": 2.0,
    "Vigor": 2,
    "Knowledge": 2,
    "Strength": 2,
    "Agility": 2,
    "Will": 2,
    "Dexterity": 2, # CAN'T BE ON RUBYSILVER ADVENTURE BOOTS!
    "Resourcefulness": 2,
    "Additional Move Speed": 5,
    "Move Speed Bonus": 1.5,  
    }   

    physical_stats = [
        'Physical Damage Bonus',
        'Physical Power',
    ]

    health_stats = [
        'Max Health',
        'Max Health Bonus',
    ]

    movement_stats = [ 
        'Additional Move Speed',
        'Move Speed Bonus',
    ]
    ruby_comp_stats = [
        'Vigor',
        'Strength',
    ]

    gold_comp_stats = [
        'Vigor',
        'Strength',
        'Dexterity',
        'Will',
    ]

    def __init__(self, item_stats: dict, item_name: str=None):
        self.item_name = item_name
        self.random_stats = item_stats.get('random_stats', None)
        self.num_random_stats = len(item_stats.get('random_stats', ''))
        self.static_stats = item_stats.get('static_stats', None)
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
    
    def buy_ruby_boots(self) -> bool:
        num_phys_stats, phys_stats = self.check_stats(self.physical_stats, 0, .5)
        num_health_stats, health_stats = self.check_stats(self.health_stats, 0, .4)
        num_move_stats, move_stats = self.check_stats(self.movement_stats, 0, .5)
        num_comp_stats, comp_stats = self.check_stats(self.ruby_comp_stats, 0, 0)

        total_stat_count = sum([
            num_phys_stats,
            num_health_stats,
            num_move_stats,
            num_comp_stats
        ])

        if num_comp_stats == 2:
            return False

        if num_phys_stats == 2:
            if not total_stat_count % 3:
                return True
        
        if num_health_stats == 2:
            if not total_stat_count % 3:
                return True
            
        if num_move_stats == 2:
            if not total_stat_count % 3:
                return True
    
        return False
    
    def buy_cobalt_boots(self) -> bool:        
        num_phys_stats, phys_stats = self.check_stats(self.physical_stats, 0, .5)
        num_health_stats, health_stats = self.check_stats(self.health_stats, 0, .4)
        num_move_stats, move_stats = self.check_stats(self.movement_stats, 0, .5)
        
        stats = [num_health_stats,
                 num_move_stats,
                 num_phys_stats]
        
        # Only take double stas on these.
        if any(stat == 2 for stat in stats):
            return True
        
    def buy_golden_plate_boots(self) -> bool:
        ...

    def worth_buying(self) -> bool:
        if self.item_name == 'rubysilver adventure boots':
            if self.buy_ruby_boots():
                return True
        if self.item_name == 'cobalt lightfoot boots':
            if self.buy_cobalt_boots():
                return True
        if self.item_name == 'golden plate boots':
            if self.buy_golden_plate_boots():
                return True            
        return False
    
    def __repr__(self):
        return f"static_stats: {self.static_stats}\nrandom_stats: {self.random_stats}"