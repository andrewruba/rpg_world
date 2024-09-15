# rpg_world/__init__.py

# Version of the package
from .__version__ import __version__

# Exposing core classes and functions
from .character.base_character import BaseCharacter
from .character.mage import Mage
from .character.character_stats import CharacterStats
from .ability.base_ability import BaseAbility
from .ability.spell import Spell
from .effect.base_effect import BaseEffect
from .effect.spell_effect import SpellEffect
from .formula.base_formula import BaseFormula
from .formula.effect_formula import SimpleChangeFormula, MultiEffectTargetFormula, MultiEffectRecipientFormula
from .game.game import Game

# Any other core imports or package-wide initialization can go here.
