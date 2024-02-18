class Ring:
    max_stats = {
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
        
    }
    primary_physical_stat = [
        'Additional Physical Damage',
        'True Physical Damage',
    ]

    secondary_physical_stat = [
        'Physical Damage Bonus',
        'Physical Power',
    ]

    primary_magical_stat = [
        'Additional Magical Damage',
        'True Magical Damage',
    ]

    secondary_magical_stat = [
        'Magical Power',
        'Magical Damage Bonus'
    ]
    physical_stats = primary_physical_stat + secondary_physical_stat
    magical_stats = primary_magical_stat + secondary_magical_stat
    primary_damage_stats = primary_physical_stat + primary_magical_stat

    movement_speed_stats = [
        'Additional Move Speed',
        'Movement Speed Bonus',
    ]
    def __init__(self, item_stats: dict=None):
        self.item_stats = item_stats
        self.num_stats = len(item_stats)
            # "Vigor": 0,
            # "Dexterity": 0,
            # "Knowledge": 0,
            # "Strength": 0,
            # "Agility": 0,
            # "Will": 0,
            # "Resourcefulness": 0, 

    
    def has_max_move_speed(self) -> bool:
        for stat, value in self.item_stats.items():
            if stat in self.movement_speed_stats:
                if (self.max_stats.get(stat) - value) <= .1:
                    # print("Has max move speed!")
                    return True
        return False

    def has_max_primary_stat(self) -> bool:
        for stat, value in self.item_stats.items():
            if stat in self.primary_physical_stat or \
            stat in self.primary_magical_stat:
                
                if not (self.max_stats.get(stat) - value):
                    # print("Has max primary stat!")
                    return True
        return False
    
    def has_max_secondary_stat(self) -> bool:
        for stat, value in self.item_stats.items():
            if stat in self.secondary_physical_stat or \
            stat in self.secondary_magical_stat:
                
                if (self.max_stats.get(stat) - value) <= .3:
                    # print("Has max Secondary Stat!")
                    return True
        return False
    
    def worth_buying(self):
        return all([
            self.has_max_primary_stat(),
            self.has_max_move_speed(),
            self.has_max_secondary_stat()
        ])
    

    
    def __repr__(self) -> str:
        return f"{self.item_stats}"

'''
Best ring: Physical power, physical damage bonus, additional physical
Good ring: +2 phys/mag DAMAGW, +3 mag/phys POWER, +3/+0.9% Move speed/move speed bonus
For now, skip all other rings.

interaction speed/ action speed/ health/

Can you get +2 healing, +2 mag damage, +3 movement speed?
'''