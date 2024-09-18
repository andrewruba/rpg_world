class GameState:
    def __init__(self):
        """
        Initialize the game state to track the current status of the world, characters, quests, and more.
        """
        self.current_world = None
        self.characters = {}
        self.quests = {}

    def update_world(self, world):
        """
        Update the current world in the game state.

        Args:
            world (World): The world to update.
        """
        assert hasattr(world, 'id'), "World must have an 'id' attribute."
        self.current_world = world

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
