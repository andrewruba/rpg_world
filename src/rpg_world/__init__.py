# rpg_world/__init__.py

# Version of the package
from .__version__ import __version__

# Exposing core classes and functions
from .character.base_character import BaseCharacter
from .character.mage import Mage
from .stats.base_stats import BaseStats
from .stats.character_stats import CharacterStats
from .ability.base_ability import BaseAbility
from .ability.spell import Spell
from .effect.base_effect import BaseEffect
from .effect.spell_effect import SpellEffect
from .formula.base_formula import BaseFormula
from .formula.effect_formula import SimpleChangeFormula, MultiEffectTargetFormula, MultiEffectRecipientFormula, SimpleChangeFormulaWithStatLimits
from .utils.logger import Logger
from .game.game import Game
from .place.place import Place
from .place.world import World
from .place.location import Location
from .place.position import Position
from .item.base_item import BaseItem
from .item.equipment import Equipment
from .item.consumable import Consumable
from .item.inventory import Inventory

# Any other core imports or package-wide initialization can go here.
