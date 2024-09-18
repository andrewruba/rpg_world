# rpg_world/__init__.py

# Version of the package
from .__version__ import __version__

# Exposing core classes and functions
from .character.character import Character
from .character.mage import Mage
from .stats.stats import Stats
from .stats.character_stats import CharacterStats
from .ability.ability import Ability
from .ability.spell import Spell
from .effect.effect import Effect
from .effect.spell_effect import SpellEffect
from .formula.formula import Formula
from .formula.effect_formula import SimpleChangeFormula, MultiEffectTargetFormula, MultiEffectRecipientFormula, SimpleChangeFormulaWithStatLimits
from .utils.logger import Logger
from .game.game import Game
from .game.game_state import GameState
from .place.place import Place
from .place.world import World
from .place.location import Location
from .place.position import Position
from .item.item import Item
from .item.equipment import Equipment
from .item.consumable import Consumable
from .item.inventory import Inventory
from .quest.quest import Quest
from .event.trigger import Trigger, HealthBelowThresholdTrigger, PlayerInLocationTrigger, QuestCompletedTrigger
from .event.event import Event, HealEvent
from .event.event_manager import EventManager

# Any other core imports or package-wide initialization can go here.
