class EventManager:
    def __init__(self):
        """
        Initialize the EventManager with a list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the manager.

        Args:
            event (Event): The event to be added to the manager.
        """
        self.events.append(event)

    def check_events(self, game_state, **kwargs):
        """
        Check all registered events against the current game state.

        Args:
            game_state (object): The current state of the game.
            **kwargs: Additional arguments passed to the trigger conditions and actions.
        """
        for event in self.events:
            if event.check_trigger(game_state, **kwargs):
                event.execute_action(game_state, **kwargs)
