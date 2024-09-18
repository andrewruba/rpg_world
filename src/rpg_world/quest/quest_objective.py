from ..utils.logger import Logger
from ..event.event import Event

class QuestObjective(Event):
    def __init__(self, name, description, triggers=None):
        """
        Initialize a quest objective that extends Event.

        Args:
            name (str): The name of the quest objective.
            description (str): A description of the objective.
            triggers (list of Trigger, optional): A list of triggers for the objective to be completed.
        """
        triggers = triggers if triggers else []  # Initialize with an empty list if no triggers provided
        super().__init__(name=name, triggers=triggers)
        self.description = description
        self.logger = Logger(f"QuestObjective-{self.name}")

    def execute_action(self, game_state):
        """
        Execute the default action when the quest objective is triggered (completed).
        By default, it logs the completion of the objective.

        Args:
            game_state (object): The current state of the game.
        """
        if self.triggered:
            self.logger.info(f"Objective '{self.name}' marked as completed.")

    def is_complete(self):
        """
        Check if the quest objective is complete.

        Returns:
            bool: True if the objective is complete, False otherwise.
        """
        return self.triggered

    def __str__(self):
        """
        String representation of the quest objective.

        Returns:
            str: A summary of the objective, its description, and its completion status.
        """
        status = "Completed" if self.is_complete() else "Incomplete"
        return f"Objective: {self.name} - {self.description} [{status}]"
