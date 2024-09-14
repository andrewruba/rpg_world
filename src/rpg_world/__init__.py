# rpg_world/__init__.py

# Version of the package
from .__version__ import __version__

# Exposing core classes and functions
from .character.base_character import BaseCharacter
from .character.mage import Mage
from .ability.base_ability import BaseAbility
from .ability.spell import Spell
from .combat.effect_calculation import EffectCalculation
from .game.game import Game

# Any other core imports or package-wide initialization can go here.
