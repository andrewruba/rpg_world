class QuestManager:
    def __init__(self):
        """
        Initialize the QuestManager with an empty list of active quests.
        """
        self.active_quests = []

    def add_quest(self, quest):
        """
        Add a new quest to the active quests list.

        Args:
            quest (Quest): The quest to add.
        """
        self.active_quests.append(quest)
        print(f"Quest '{quest.name}' added to active quests.")

    def remove_quest(self, quest):
        """
        Remove a quest from the active quests list.

        Args:
            quest (Quest): The quest to remove.
        """
        if quest in self.active_quests:
            self.active_quests.remove(quest)
            print(f"Quest '{quest.name}' removed from active quests.")

    def complete_quest(self, quest):
        """
        Complete a quest and remove it from the active quests if all objectives are done.

        Args:
            quest (Quest): The quest to complete.
        """
        if quest.is_completed():
            quest.complete_quest()
            self.remove_quest(quest)
        else:
            print(f"Quest '{quest.name}' is not yet completed.")

    def get_active_quests(self):
        """
        Get a list of all active quests.

        Returns:
            list: A list of active quests.
        """
        return self.active_quests

    def list_active_quests(self):
        """
        Print all active quests and their status.
        """
        if not self.active_quests:
            print("No active quests.")
        else:
            for quest in self.active_quests:
                print(quest)
