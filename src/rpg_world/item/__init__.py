# rpg_world/item/__init__.py

from .base_item import BaseItem
from .equipment import Equipment
from .consumable import Consumable
from .inventory import Inventory

# By including this, users can import characters like this:
# from rpg_world.base_item import BaseItem
