class Event:
    def __init__(self, name, trigger_condition, action):
        """
        Initialize an Event in the game world.

        Args:
            name (str): The name of the event.
            trigger_condition (callable): A function or condition that determines when the event is triggered.
            action (callable): A function representing the action to be performed when the event is triggered.
        """
        self.name = name
        self.trigger_condition = trigger_condition
        self.action = action

    def check_trigger(self, game_state, **kwargs):
        """
        Check if the event's trigger condition is met based on the current game state.

        Args:
            game_state (object): The current state of the game passed to evaluate the trigger.
            **kwargs: Additional arguments passed to the trigger condition.

        Returns:
            bool: True if the event is triggered, False otherwise.
        """
        return self.trigger_condition(game_state, **kwargs)

    def execute_action(self, game_state, **kwargs):
        """
        Execute the event's action if triggered.

        Args:
            game_state (object): The current state of the game passed to execute the action.
            **kwargs: Additional arguments passed to the action function.
        """
        self.action(game_state, **kwargs)
