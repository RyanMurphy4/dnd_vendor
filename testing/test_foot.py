import sys
sys.path.append("../")
from slots.foot import Foot


def create_random_foot(num_stats: int, item_name: str) -> Foot:
    stats = {
        "random_stats": {},
        "static_stats": {}
    }
    max_stats = Foot.max_stats
    if item_name == 'rubysilver adventure boots':
        stats['static_stats']['Dexterity'] = 5
    

def test_worth_buying(num_stats: int, item_name: str) -> Foot:
    ...
