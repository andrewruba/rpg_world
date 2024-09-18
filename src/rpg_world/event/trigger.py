from abc import ABC, abstractmethod

class Trigger(ABC):
    """
    Abstract base class for all triggers. Defines the interface that all triggers must implement.
    """

    def __init__(self, description=""):
        """
        Initialize the trigger with an optional description.

        Args:
            description (str): A brief description of the trigger (optional).
        """
        self.description = description

    @abstractmethod
    def evaluate(self, game_state):
        """
        Abstract method that evaluates whether the trigger condition is met.

        Args:
            game_state (object): The current state of the game.
            **kwargs: Additional arguments specific to the trigger type.

        Returns:
            bool: True if the trigger condition is met, False otherwise.
        """
        pass

class HealthBelowThresholdTrigger(Trigger):
    """
    A trigger that checks if a player's health drops below a given threshold.
    """

    def __init__(self, character_id, threshold):
        """
        Initialize the trigger with the player name and health threshold.

        Args:
            character_id (str): The id of the character.
            threshold (int): The health threshold below which the trigger activates.
        """
        super().__init__(description=f"Trigger when health drops below {threshold}.")
        self.character_id = character_id
        self.threshold = threshold

    def evaluate(self, game_state):
        """
        Evaluate if the player's health is below the specified threshold.

        Args:
            game_state (object): The current state of the game.

        Returns:
            bool: True if the player's health is below the threshold, False otherwise.
        """
        character = game_state.characters[self.character_id]
        return character.health < self.threshold

class PlayerInLocationTrigger(Trigger):
    """
    A trigger that checks if a specific location has been reached.
    """

    def __init__(self, location_id):
        """
        Initialize the trigger with the player name and location name.

        Args:
            player_name (str): The name of the player.
            location_id (str): The name of the location.
        """
        super().__init__(description=f"Trigger when {location_id} is reached.")
        self.location_id = location_id

    def evaluate(self, game_state):
        """
        Evaluate if the player has reached the specified location.

        Args:
            game_state (object): The current state of the game.

        Returns:
            bool: True if the player is in the specified location, False otherwise.
        """
        return game_state.current_world.current_location.id == self.location_id

class QuestCompletedTrigger(Trigger):
    """
    A trigger that activates when a specific quest is completed.
    """

    def __init__(self, quest_id):
        """
        Initialize the trigger with the quest name.

        Args:
            quest_name (str): The name of the quest.
        """
        super().__init__(description=f"Trigger when the quest '{quest_id}' is completed.")
        self.quest_id = quest_id

    def evaluate(self, game_state):
        """
        Evaluate if the quest has been completed.

        Args:
            game_state (object): The current state of the game.

        Returns:
            bool: True if the quest is completed, False otherwise.
        """
        return game_state.quests[self.quest_id].is_completed()

