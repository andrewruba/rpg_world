# rpg_world/__init__.py

# Version of the package
from .__version__ import __version__

# Exposing core classes and functions
from .character.base_character import BaseCharacter
from .character.mage import Mage
from .character.character_stats import CharacterStats
from .ability.base_ability import BaseAbility
from .ability.spell import Spell
from .combat.base_effect import BaseEffect
from .combat.spell_effect import SpellEffect
from .combat.effect_formulas import simple_change, multi_effect_target_example, multi_effect_recipient_example
from .game.game import Game

# Any other core imports or package-wide initialization can go here.
