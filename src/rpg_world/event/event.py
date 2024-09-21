from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, name, description, triggers):
        """
        Initialize a Event in the game world.

        Args:
            name (str): The name of the event.
            triggers (list of Trigger): A list of Trigger objects that determine when the event is triggered.
        """
        self.name = name
        self.description = description
        self.triggers = triggers  # List of triggers
        self.triggered = False    # Flag to track if the event has been triggered

    def check_triggers(self, game_state):
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
            if not trigger.evaluate(game_state):
                return False

        # If all triggers are satisfied, mark the event as triggered and execute action
        self.triggered = True
        self.execute_action(game_state)
        return True

    @abstractmethod
    def execute_action(self, game_state):
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


class HealEvent(Event):
    def __init__(self, name, description, triggers, character_id):
        """
        Initialize the HealEvent with a name and triggers.

        Args:
            name (str): The name of the event.
            triggers (list of Trigger): A list of Trigger objects.
        """
        super().__init__(name, description, triggers)
        self.character_id = character_id

    def execute_action(self, game_state):
        """
        Heal the player if all triggers are satisfied.

        Args:
            game_state (object): The current state of the game.
        """
        if self.triggered:
            character = game_state.characters[self.character_id]
            character.health = character.max_health
