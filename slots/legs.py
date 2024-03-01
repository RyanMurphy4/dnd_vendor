class Legs:
    max_stats = {
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
    }

    move_stats = [
        'Additional Move Speed',
        'Move Speed Bonus',
    ]

    health_stats = [
        'Max Health',
        'Max Health Bonus',
    ]
    
    physical_stats = [
        'Physical Power',
        'Physical Damage Bonus',
    ]

    magical_stats = [
        'Magical Damage Bonus',
        'Magical Power',
    ]

    def __init__(self, item_stats: dict, item_name: str=None):
        self.item_name = item_name
        self.item_stats = item_stats
        self.random_stats = item_stats.get('random_stats')
        self.num_random_stats = len(item_stats.get('random_stats', ''))
        self.static_stats = item_stats.get('static_stats')
        self.num_static_stats = len(item_stats.get('static_stats', ''))
        self.account_for_leather_legs()

    def account_for_leather_legs(self) -> None:
        if 'wolf hunter leggings' in self.item_stats:
            self.item_name = 'wolf hunter leggings'
        elif 'demonclad leggings' in self.item_stats:
            self.item_name = 'demonclad leggings'
    
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

    def buy_cobalt_trousers(self) -> bool:
        num_move_stats, move_stats = self.check_stats(self.move_stats, 0, .3)
        num_health_stats, health_stats = self.check_stats(self.health_stats, 0, .4)
        num_phys_stats, phys_stats = self.check_stats(self.physical_stats, 0, .5)
        num_mag_stats, magic_stats = self.check_stats(self.magical_stats, 0, .5)

        
        add_move = True if 'Additional Move Speed' in move_stats else False
        phys_power = True if 'Physical Power' in phys_stats else False
        mag_power = True if 'Magical Power' in magic_stats else False
        max_health = True if 'Max Health' in health_stats else False

        
        if add_move:
            if phys_power or max_health or mag_power:
                return True

        if num_move_stats == 2:
            return True
        
        if num_move_stats and num_phys_stats:
            return True
            
        return False


    # 2 dex, 5 move speed
    # 3.4% phys, 5 move speed
    def buy_wolf_hunter(self) -> bool:
        num_move_stats, move_stats = self.check_stats(self.move_stats, 0, .3)
        num_phys_stats, phys_stats = self.check_stats(self.physical_stats, 0, .5)
        num_health_stats, health_stats = self.check_stats(self.health_stats, 0, .4)
        dex, _ = self.check_stats(['Dexterity'], 0, 0)
        add_move = True if 'Additional Move Speed' in move_stats else False
        phys_power = True if 'Physical Power' in phys_stats else False
        max_health = True if 'Max Health' in health_stats else False

        if add_move and (dex or phys_power or max_health):
            return True
        if num_move_stats and num_phys_stats:
            return True
        if num_move_stats and num_health_stats:
            return True
        
        return False    
    
    def buy_demonclad(self) -> bool:
        ...

    def worth_buying(self) -> bool:
        if self.item_name == 'cobalt trousers':
            if self.buy_cobalt_trousers():
                return True
        if self.item_name == 'wolf hunter leggings':
            if self.buy_wolf_hunter():
                return True
        if self.item_name == 'demonclad leggings':
            if self.buy_demonclad():
                return True
    
    def __repr__(self) -> str:
        return f"{self.random_stats}"