from ..utils.logger import Logger
from ..event.event_manager import EventManager

class QuestManager(EventManager):
    def __init__(self):
        """
        Initialize the QuestManager with an empty list of active quests.
        """
        super().__init__()  # Inherit from EventManager
        self.logger = Logger("QuestManager")

    def add_quest(self, quest):
        """
        Add a new quest to the active quests list by registering it as an event.

        Args:
            quest (Quest): The quest to add.
        """
        self.add_event(quest)  # Use EventManager's add_event method
        self.logger.info(f"Quest '{quest.name}' added to active quests.")

    def remove_quest(self, quest):
        """
        Remove a quest from the active quests list by removing the event.

        Args:
            quest (Quest): The quest to remove.
        """
        self.remove_event(quest)  # Use EventManager's remove_event method
        self.logger.info(f"Quest '{quest.name}' removed from active quests.")

    def get_all_quests(self):
        """
        Get a list of all active quests (events).

        Returns:
            list: A list of active quests.
        """
        return self.events

    def get_incomplete_quests(self):
        """
        Get a list of all active quests (events).

        Returns:
            list: A list of active quests.
        """
        return [quest for quest in self.get_all_quests() if not quest.is_complete()]

    def get_complete_quests(self):
        """
        Get a list of all active quests (events).

        Returns:
            list: A list of active quests.
        """
        return [quest for quest in self.get_all_quests() if quest.is_complete()]

