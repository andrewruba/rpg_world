from ..utils.logger import Logger

class EventManager:
    def __init__(self):
        """
        Initialize the EventManager with a list of events.
        """
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
        Check all registered events against the current game state.

        Args:
            game_state (object): The current state of the game.
        """
        for event in self.events:
            if not event.triggered:
                event.check_trigger(game_state)
