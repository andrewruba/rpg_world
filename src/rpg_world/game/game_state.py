class GameState:
    def __init__(self):
        """
        Initialize the game state to track the current status of characters, world, quests, and more.
        """
        self.current_location = None
        self.characters = {}
        self.quests = {}

    def update_location(self, location):
        """
        Update the current location in the game state.

        Args:
            location (Location): The new location to update.
        """
        assert hasattr(location, 'id'), "Location must have an 'id' attribute."
        self.current_location = location

    def add_character(self, character):
        """
        Add a character to the game state.

        Args:
            character (Character): The character to add.
        """
        assert hasattr(character, 'id'), "Character must have an 'id' attribute."
        self.characters[character.id] = character

    def update_quests(self, quest):
        """
        Update the current quests in the game state.

        Args:
            quest (Quest): The updated quest status.
        """
        assert hasattr(quest, 'id'), "Quest must have an 'id' attribute."
        self.quests[quest.id] = quest

    def get_game_snapshot(self):
        """
        Retrieve a snapshot of the current game state.
        """
        return {
            "location": self.current_location.__dict__ if self.current_location else None,
            "characters": {char_id: char.__dict__ for char_id, char in self.characters.items()},
            "quests": {quest_id: quest.__dict__ for quest_id, quest in self.quests.items()}
        }

    def restore_from_snapshot(self, snapshot, character_class, location_class, quest_class):
        """
        Restore the game state from a snapshot.

        Args:
            snapshot (dict): The saved snapshot of the game state.
            character_class (class): The class used to instantiate character objects.
            location_class (class): The class used to instantiate location objects.
            quest_class (class): The class used to instantiate quest objects.
        """
        if snapshot["location"]:
            self.current_location = location_class(**snapshot["location"])

        self.characters = {char_id: character_class(**data) for char_id, data in snapshot["characters"].items()}
        self.quests = {quest_id: quest_class(**data) for quest_id, data in snapshot["quests"].items()}

        print("Game state restored from snapshot.")
