class Event:
    def __init__(self, name, trigger_condition, action):
        """
        Initialize an Event in the game world.

        Args:
            name (str): The name of the event.
            trigger_condition (callable): A function or condition that triggers the event.
            action (callable): A function representing the action to be performed when the event is triggered.
        """
        self.name = name
        self.trigger_condition = trigger_condition
        self.action = action

    def check_trigger(self, **kwargs):
        """
        Check if the event's trigger condition is met.

        Args:
            **kwargs: Additional arguments passed to the trigger condition.

        Returns:
            bool: True if the event is triggered, False otherwise.
        """
        return self.trigger_condition(**kwargs)

    def execute_action(self, **kwargs):
        """
        Execute the event's action.

        Args:
            **kwargs: Additional arguments passed to the action function.
        """
        self.action(**kwargs)


# Example trigger and action functions
def sample_trigger(player):
    """A sample trigger condition that activates when the player's health is below 50."""
    return player.get_attribute("health") < 50

def sample_action(player):
    """A sample action function that heals the player."""
    player.set_attribute("health", 100)
    print(f"{player.name} has been healed to full health!")
