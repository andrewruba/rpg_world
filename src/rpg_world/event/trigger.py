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
    def evaluate(self, game_state, **kwargs):
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

    def __init__(self, player_name, threshold):
        """
        Initialize the trigger with the player name and health threshold.

        Args:
            player_name (str): The name of the player.
            threshold (int): The health threshold below which the trigger activates.
        """
        super().__init__(description=f"Trigger when {player_name}'s health drops below {threshold}.")
        self.player_name = player_name
        self.threshold = threshold

    def evaluate(self, game_state, **kwargs):
        """
        Evaluate if the player's health is below the specified threshold.

        Args:
            game_state (object): The current state of the game.

        Returns:
            bool: True if the player's health is below the threshold, False otherwise.
        """
        player = game_state.get_player(self.player_name)
        return player.get_attribute("health") < self.threshold

class PlayerInLocationTrigger(Trigger):
    """
    A trigger that checks if a player has reached a specific location.
    """

    def __init__(self, player_name, location_name):
        """
        Initialize the trigger with the player name and location name.

        Args:
            player_name (str): The name of the player.
            location_name (str): The name of the location.
        """
        super().__init__(description=f"Trigger when {player_name} reaches {location_name}.")
        self.player_name = player_name
        self.location_name = location_name

    def evaluate(self, game_state, **kwargs):
        """
        Evaluate if the player has reached the specified location.

        Args:
            game_state (object): The current state of the game.

        Returns:
            bool: True if the player is in the specified location, False otherwise.
        """
        player = game_state.get_player(self.player_name)
        return player.current_location == self.location_name

class QuestCompletedTrigger(Trigger):
    """
    A trigger that activates when a specific quest is completed.
    """

    def __init__(self, quest_name):
        """
        Initialize the trigger with the quest name.

        Args:
            quest_name (str): The name of the quest.
        """
        super().__init__(description=f"Trigger when the quest '{quest_name}' is completed.")
        self.quest_name = quest_name

    def evaluate(self, game_state, **kwargs):
        """
        Evaluate if the quest has been completed.

        Args:
            game_state (object): The current state of the game.

        Returns:
            bool: True if the quest is completed, False otherwise.
        """
        quest = game_state.get_quest(self.quest_name)
        return quest.is_completed()

