from ..utils.logger import Logger
from ..event.event_manager import EventManager

class Quest(EventManager):
    """
    Represents a full quest consisting of multiple objectives and rewards for completion.
    Inherits from EventManager to manage quest objectives as events.
    """

    def __init__(self, name, description, objectives=None, rewards=None, id=None):
        """
        Initialize a quest with a name, description, objectives, and rewards.

        Args:
            name (str): The name of the quest.
            description (str): A brief description of the quest.
            objectives (list, optional): A list of QuestObjective objects. Defaults to None.
            rewards (dict, optional): A dictionary of rewards for completing the quest. Defaults to an empty dictionary.
            id (str, optional): A unique identifier for the quest. Defaults to None.
        """
        super().__init__(id, name, description)  # Initialize EventManager with id, name, and description
        self.rewards = rewards or {}
        self.logger = Logger(f"Quest-{self.name}")

        # If objectives are provided, add them as events to EventManager
        if objectives:
            for objective in objectives:
                self.add_objective(objective)

    def add_objective(self, objective):
        """
        Add an objective to the quest and register it as an event.

        Args:
            objective (QuestObjective): The objective to add to the quest.
        """
        self.add_event(objective)  # Use EventManager's add_event method
        self.logger.info(f"Objective '{objective.name}' added to quest '{self.name}'.")

    def is_complete(self):
        """
        Check if all quest objectives are completed.

        Returns:
            bool: True if all objectives (events) are completed, False otherwise.
        """
        return all(event.triggered for event in self.events)

    def complete_quest(self):
        """
        Complete the quest if all objectives are completed and return the rewards.

        Returns:
            dict: The rewards for completing the quest, or None if it is not yet completed.
        """
        if self.is_complete():
            self.logger.info(f"Quest '{self.name}' completed! Rewards: {self.rewards}")
            return self.rewards
        else:
            self.logger.info(f"Quest '{self.name}' is not yet completed.")
            return None

    def check_quest_progress(self, game_state):
        """
        Check the progress of the quest by evaluating the status of all objectives (events).

        Args:
            game_state (object): The current state of the game to evaluate triggers.
        """
        self.logger.info(f"Checking progress for quest '{self.name}'.")
        self.check_events(game_state)  # Use EventManager's check_events method

    def __str__(self):
        """
        String representation of the quest.

        Returns:
            str: A summary of the quest, including name, description, and objectives.
        """
        objectives_status = "\n".join([f"{event.name} - {'Completed' if event.triggered else 'Incomplete'}" for event in self.events])
        status = "Completed" if self.is_complete() else "Incomplete"
        return f"Quest: {self.name} [{status}]\nDescription: {self.description}\nObjectives:\n{objectives_status}"
