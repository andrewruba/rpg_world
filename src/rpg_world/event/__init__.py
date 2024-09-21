# rpg_world/even/__init__.py

from .trigger import (
    Trigger,
    HealthBelowThresholdTrigger,
    PlayerInLocationTrigger,
    QuestCompletedTrigger
)
from .event import Event, HealEvent
from .event_manager import EventManager

# By including this, users can import characters like this:
# from rpg_world.event import Event
