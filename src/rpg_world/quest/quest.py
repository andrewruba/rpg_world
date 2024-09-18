class Quest:
    def __init__(self, name, description, objectives=None, rewards=None, id=None):
        """
        Initialize a quest with a name, description, objectives, and rewards.

        Args:
            name (str): The name of the quest.
            description (str): A brief description of the quest.
            objectives (list): A list of QuestObjective objects (optional).
            rewards (dict): A dictionary of rewards for completing the quest (optional).
        """
        self.id = id
        self.name = name
        self.description = description
        self.objectives = objectives or []
        self.rewards = rewards or {}

    def add_objective(self, objective):
        """
        Add an objective to the quest.

        Args:
            objective (QuestObjective): The objective to add to the quest.
        """
        self.objectives.append(objective)

    def is_completed(self):
        """
        Check if all the quest's objectives are completed.

        Returns:
            bool: True if all objectives are completed, False otherwise.
        """
        return all(obj.is_completed() for obj in self.objectives)

    def complete_quest(self):
        """
        Complete the quest and return the rewards.

        Returns:
            dict: The rewards for completing the quest.
        """
        if self.is_completed():
            print(f"Quest '{self.name}' completed! You earned: {self.rewards}")
            return self.rewards
        else:
            print(f"Quest '{self.name}' is not yet completed.")
            return None

    def __str__(self):
        """
        String representation of the quest.

        Returns:
            str: A summary of the quest, including name, description, and objectives.
        """
        objectives = "\n".join([str(obj) for obj in self.objectives])
        return f"Quest: {self.name}\nDescription: {self.description}\nObjectives:\n{objectives}"
