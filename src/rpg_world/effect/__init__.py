# rpg_world/effect/__init__.py

from .base_effect import BaseEffect
from .spell_effect import SpellEffect
from .effect_formulas import simple_change, multi_effect_target_example, multi_effect_recipient_example

# By including this, users can import characters like this:
# from rpg_world.base_effect import BaseEffect
