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
        "Magical Healing": 2
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

    comp_physical_stats = [
        'Max Health',
        'Max Health Bonus',
        'Additional Movement Speed',
        'Move Speed Bonus',
        'Armor Rating', 
    ]

    comp_magical_stats = [
        'Max Health',
        'Max Health Bonus',
        'Additional Movement Speed',
        'Move Speed Bonus',
        'Magical Healing',
    ]
    physical_stats = primary_physical_stat + secondary_physical_stat
    magical_stats = primary_magical_stat + secondary_magical_stat
    primary_damage_stats = primary_physical_stat + primary_magical_stat

    def __init__(self, item_stats: dict=None, item_name: str=None):
        self.item_name = item_name
        self.item_stats = item_stats.get('random_stats')
        self.num_stats = len(item_stats.get('random_stats'))
        self.magical_ring = False
        self.physical_ring = False

    def has_max_primary_stat(self) -> bool:
        for stat, value in self.item_stats.items():
            if stat in self.primary_physical_stat:
                if self.max_stats.get(stat) - value == 0:
                    self.physical_ring = True
                    return True
            elif stat in self.primary_magical_stat:
                if self.max_stats.get(stat) - value == 0:
                    self.magical_ring = True
                    return True
        return False
    
    #TODO Refactor to similar style to other slot classes.
    def has_related_secondary_stat(self) -> int:
        '''
        Returns amount of secondary damage stats the ring contains.

        Note: 'has_max_primary_stat' must be called before this function to set
        maigcal_ring or phyiscal_ring
        '''
        related_stats = 0
        secondary_stats = self.secondary_magical_stat if self.magical_ring else self.secondary_physical_stat

        for stat, value in self.item_stats.items():
            if stat in secondary_stats:
                if (self.max_stats.get(stat) - value) <= .5:
                    related_stats += 1

        return related_stats
    
    def has_related_comp_stat(self) -> int:
        '''
        Returns amount of secondary damage stats the ring contains.

        Note: 'has_max_primary_stat' must be called before this function to set
        maigcal_ring or phyiscal_ring
        '''
        related_stats = 0
        comp_stats = self.comp_magical_stats if self.magical_ring else self.comp_physical_stats
        
        for stat, value in self.item_stats.items():
            if stat in comp_stats:
                if (self.max_stats.get(stat) - value) <= .5:
                    related_stats += 1
                    
        return related_stats
        
    def worth_buying(self) -> bool:
        if not self.has_max_primary_stat():
            return False

        num_sec_stats = self.has_related_secondary_stat()
        num_comp_stats = self.has_related_comp_stat()
        total = num_sec_stats + num_comp_stats

        if total and total % 2 == 0:
            return True
        return False

    def __repr__(self) -> str:
        return f"{self.item_stats}"

