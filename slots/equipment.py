class Equipment:

    def __init__(self, item_stats: dict, max_stats: dict,):
        self.item_stats = item_stats
        self.max_stats = max_stats

    def compare_stats(self):
        total_diff = 0 # THE LOWER THE BETTER
        
        
        for stat, value in self.item_stats.items():
            diff = self.max_stats.get(stat, 1000) - value
            print(type(diff))
            if isinstance(diff, float) and diff <= .5:
                total_diff += diff
                print("Made it here once")
            else:
                print("Ring sucks")
                return False

        # best_stats = ['Additional Magical Damage',
        #               'Magical Damage Bonus',
        #               'True Magical Damage',
        #               'Magical Power',
        #               'Additional Physical Damage',
        #               'Physical Damage Bonus',
        #               'True Physical Damage',
        #               'Physical Power',
        #             ]