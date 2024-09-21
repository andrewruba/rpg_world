class GameState:
    """
    Represents the current state of the game, including characters, quests, and the game world.
    """

    def __init__(self):
        """
        Initialize the game state with empty placeholders for the world, characters, and quests.
        """
        self.current_world = None
        self.characters = {}
        self.quests = {}

    def update_world(self, world):
        """
        Update the current world in the game state.

        Args:
            world (World): The world object to set as the current game world.
        """
        assert hasattr(world, 'id'), "World must have an 'id' attribute."
        self.current_world = world

    def add_character(self, character):
        """
        Add a character to the game state.

        Args:
            character (Character): The character object to add to the game state.
        """
        assert hasattr(character, 'id'), "Character must have an 'id' attribute."
        self.characters[character.id] = character

    def update_quests(self, quest):
        """
        Update the current quest status in the game state.

        Args:
            quest (Quest): The quest object to update in the game state.
        """
        assert hasattr(quest, 'id'), "Quest must have an 'id' attribute."
        self.quests[quest.id] = quest
