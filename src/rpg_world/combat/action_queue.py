import time

class ActionQueue:
    def __init__(self):
        """
        Initialize the ActionQueue class.
        """
        self.action_queue = []

    def add_action(self, action):
        """
        Add an action to the queue.

        Args:
            action (CombatAction): The action to add to the queue.
        """
        self.action_queue.append(action)

    def execute_actions(self):
        """
        Executes all actions in the queue.
        """
        current_time = time.time()
        for action in self.action_queue:
            if current_time >= action.execution_time:
                action.execute()
                self.action_queue.remove(action)
