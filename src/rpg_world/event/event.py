from abc import ABC, abstractmethod

class Event(ABC):
    """
    Represents an abstract event in the game world, with specific triggers and an action.
    """

    def __init__(self, name, description, triggers):
        """
        Initialize an Event with a name, description, and a set of triggers.

        Args:
            name (str): The name of the event.
            description (str): A brief description of the event.
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

        Returns:
            bool: True if all the triggers are met, False otherwise.
        """
        # If the event has already been triggered, do not re-check the triggers
        if self.triggered:
            return False

        # Check all triggers
        for trigger in self.triggers:
            if not trigger.evaluate(game_state):
                return False

        # If all triggers are satisfied, mark the event as triggered and execute its action
        self.triggered = True
        self.execute_action(game_state)
        return True

    @abstractmethod
    def execute_action(self, game_state):
        """
        Abstract method for executing the event's action. 
        This must be implemented by subclasses to define specific event behavior.

        Args:
            game_state (object): The current state of the game passed to execute the action.
        """
        pass

    def reset(self):
        """
        Reset the event's triggered status so it can be triggered again.
        """
        self.triggered = False


class HealEvent(Event):
    """
    Represents a healing event that restores a character's health when triggered.
    """

    def __init__(self, name, description, triggers, character_id):
        """
        Initialize the HealEvent with a name, description, triggers, and a target character to heal.

        Args:
            name (str): The name of the heal event.
            description (str): A description of the heal event.
            triggers (list of Trigger): A list of Trigger objects that determine when the event is triggered.
            character_id (str): The ID of the character to be healed when the event is triggered.
        """
        super().__init__(name, description, triggers)
        self.character_id = character_id

    def execute_action(self, game_state):
        """
        Heal the target character if all triggers are satisfied.

        Args:
            game_state (object): The current state of the game, which includes character data.
        """
        if self.triggered:
            character = game_state.characters[self.character_id]
            character.health = character.max_health
