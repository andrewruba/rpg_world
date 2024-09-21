from ..utils.logger import Logger
from ..event.event import Event

class QuestObjective(Event):
    """
    Represents an individual objective within a quest. Each objective is an event 
    that triggers upon completion and is part of the overall quest's progress.
    """

    def __init__(self, name, description, triggers=None):
        """
        Initialize a quest objective, which is an event with optional triggers.

        Args:
            name (str): The name of the quest objective.
            description (str): A brief description of the objective.
            triggers (list of Trigger, optional): A list of triggers for the objective to be completed. Defaults to an empty list.
        """
        triggers = triggers if triggers else []  # Initialize with an empty list if no triggers are provided
        super().__init__(name=name, description=description, triggers=triggers)
        self.logger = Logger(f"QuestObjective-{self.name}")

    def execute_action(self, game_state):
        """
        Execute the default action when the quest objective is triggered (completed).
        Logs the completion of the objective by default.

        Args:
            game_state (object): The current state of the game.
        """
        if self.triggered:
            self.logger.info(f"Objective '{self.name}' marked as completed.")

    def is_complete(self):
        """
        Check if the quest objective is complete (triggered).

        Returns:
            bool: True if the objective is completed, False otherwise.
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
