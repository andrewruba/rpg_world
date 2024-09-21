from ..utils.logger import Logger

class EventManager:
    """
    Manages a collection of events and checks their triggers during the game.
    """

    def __init__(self, id=None, name=None, description=None):
        """
        Initialize the EventManager with optional metadata and an empty list of events.

        Args:
            id (str, optional): The unique identifier for the event manager. Defaults to None.
            name (str, optional): The name of the event manager. Defaults to None.
            description (str, optional): A description of the event manager. Defaults to None.
        """
        self.id = id
        self.name = name
        self.description = description
        self.events = []
        self.logger = Logger("EventManager")

    def add_event(self, event):
        """
        Add an event to the manager.

        Args:
            event (Event): The event to be added to the manager.
        """
        self.events.append(event)
        self.logger.info(f"Event '{event.name}' added to the manager.")

    def remove_event(self, event):
        """
        Remove an event from the manager.

        Args:
            event (Event): The event to be removed from the manager.
        """
        if event in self.events:
            self.events.remove(event)
            self.logger.info(f"Event '{event.name}' removed from the manager.")

    def check_events(self, game_state):
        """
        Check all registered events against the current game state to see if their triggers are satisfied.

        Args:
            game_state (object): The current state of the game used to evaluate the event triggers.
        """
        for event in self.events:
            if not event.triggered:
                event.check_triggers(game_state)
