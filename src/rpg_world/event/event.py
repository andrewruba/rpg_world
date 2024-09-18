from abc import ABC, abstractmethod

class BaseEvent(ABC):
    def __init__(self, name, triggers):
        """
        Initialize a BaseEvent in the game world.

        Args:
            name (str): The name of the event.
            triggers (list of Trigger): A list of Trigger objects that determine when the event is triggered.
        """
        self.name = name
        self.triggers = triggers  # List of triggers
        self.triggered = False    # Flag to track if the event has been triggered

    def check_triggers(self, game_state, **kwargs):
        """
        Check if all the event's triggers are met based on the current game state.

        Args:
            game_state (object): The current state of the game passed to evaluate the triggers.
            **kwargs: Additional arguments passed to the triggers' evaluate function.

        Returns:
            bool: True if all the triggers are met, False otherwise.
        """
        # If the event has already been triggered, do not re-check the triggers
        if self.triggered:
            return False

        for trigger in self.triggers:
            if not trigger.evaluate(game_state, **kwargs):
                return False

        # If all triggers are satisfied, mark the event as triggered
        self.triggered = True
        return True

    @abstractmethod
    def execute_action(self, game_state, **kwargs):
        """
        Abstract method for executing the event's action. 
        Must be implemented by subclasses.

        Args:
            game_state (object): The current state of the game passed to execute the action.
            **kwargs: Additional arguments passed to the action function.
        """
        pass

    def reset(self):
        """
        Reset the triggered flag so the event can be triggered again.
        """
        self.triggered = False


class HealEvent(BaseEvent):
    def __init__(self, name, triggers):
        """
        Initialize the HealEvent with a name and triggers.

        Args:
            name (str): The name of the event.
            triggers (list of Trigger): A list of Trigger objects.
        """
        super().__init__(name, triggers)

    def execute_action(self, game_state, **kwargs):
        """
        Heal the player if all triggers are satisfied.

        Args:
            game_state (object): The current state of the game.
        """
        if self.check_triggers(game_state, **kwargs):
            player = game_state.get_player("Hero")
            player.set_attribute("health", player.get_attribute("max_health"))
            print(f"{player.name} has been healed to full health.")
        else:
            print(f"Event '{self.name}' not triggered. Conditions not met.")
