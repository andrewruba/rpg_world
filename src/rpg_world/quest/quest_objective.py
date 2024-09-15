class QuestObjective:
    def __init__(self, description, is_completed=False):
        """
        Initialize a quest objective.

        Args:
            description (str): A description of the objective.
            is_completed (bool): Whether the objective is initially completed (default False).
        """
        self.description = description
        self.is_completed = is_completed

    def mark_completed(self):
        """
        Mark the objective as completed.
        """
        self.is_completed = True
        print(f"Objective '{self.description}' marked as completed.")

    def is_completed(self):
        """
        Check if the objective is completed.

        Returns:
            bool: True if the objective is completed, False otherwise.
        """
        return self.is_completed

    def __str__(self):
        """
        String representation of the objective.

        Returns:
            str: A summary of the objective and its completion status.
        """
        status = "Completed" if self.is_completed else "Incomplete"
        return f"Objective: {self.description} [{status}]"
