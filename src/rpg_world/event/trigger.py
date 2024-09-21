from abc import ABC, abstractmethod

class Trigger(ABC):
    """
    Abstract base class for all triggers. Triggers define conditions that, when satisfied,
    will activate an associated event.
    """

    def __init__(self, description=""):
        """
        Initialize the trigger with an optional description.

        Args:
            description (str): A brief description of the trigger. Defaults to an empty string.
        """
        self.description = description

    @abstractmethod
    def evaluate(self, game_state):
        """
        Abstract method that evaluates whether the trigger condition is met.

        Args:
            game_state (object): The current state of the game.

        Returns:
            bool: True if the trigger condition is met, False otherwise.
        """
        pass


class HealthBelowThresholdTrigger(Trigger):
    """
    A trigger that activates when a character's health drops below a specified threshold.
    """

    def __init__(self, character_id, threshold):
        """
        Initialize the trigger with the character ID and the health threshold.

        Args:
            character_id (str): The ID of the character to monitor.
            threshold (int): The health threshold below which the trigger activates.
        """
        super().__init__(description=f"Trigger when health drops below {threshold}.")
        self.character_id = character_id
        self.threshold = threshold

    def evaluate(self, game_state):
        """
        Evaluate if the character's health is below the specified threshold.

        Args:
            game_state (object): The current state of the game, including character data.

        Returns:
            bool: True if the character's health is below the threshold, False otherwise.
        """
        character = game_state.characters[self.character_id]
        return character.health < self.threshold


class PlayerInLocationTrigger(Trigger):
    """
    A trigger that activates when the player reaches a specific location in the game world.
    """

    def __init__(self, location_id):
        """
        Initialize the trigger with the ID of the location.

        Args:
            location_id (str): The ID of the location to trigger when the player reaches it.
        """
        super().__init__(description=f"Trigger when location '{location_id}' is reached.")
        self.location_id = location_id

    def evaluate(self, game_state):
        """
        Evaluate if the player has reached the specified location.

        Args:
            game_state (object): The current state of the game, including the player's location.

        Returns:
            bool: True if the player is in the specified location, False otherwise.
        """
        return game_state.current_world.current_location.id == self.location_id


class QuestCompletedTrigger(Trigger):
    """
    A trigger that activates when a specific quest is completed by the player.
    """

    def __init__(self, quest_id):
        """
        Initialize the trigger with the quest ID.

        Args:
            quest_id (str): The ID of the quest to trigger upon completion.
        """
        super().__init__(description=f"Trigger when the quest '{quest_id}' is completed.")
        self.quest_id = quest_id

    def evaluate(self, game_state):
        """
        Evaluate if the specified quest has been completed.

        Args:
            game_state (object): The current state of the game, including quest completion status.

        Returns:
            bool: True if the quest is completed, False otherwise.
        """
        return game_state.quests[self.quest_id].is_complete()
