import pytest
from rpg_world import (
    GameState,
    Character,
    Quest,
    World,
    CharacterStats
)

@pytest.fixture
def game_state():
    """
    Fixture to initialize a new GameState instance for testing.
    """
    return GameState()

@pytest.fixture
def mock_world():
    """
    Fixture to create a mock World object with an id.
    """
    return World(name="Test World", id="world_001")

@pytest.fixture
def mock_character():
    """
    Fixture to create a mock Character object with an id.
    """
    return Character(name="Hero", stats = CharacterStats(), id="char_001")

@pytest.fixture
def mock_quest():
    """
    Fixture to create a mock Quest object with an id.
    """
    return Quest(name="Save the Village", description="Save the Village", id="quest_001")

def test_update_world(game_state, mock_world):
    """
    Test that the world can be updated in the game state.
    """
    game_state.update_world(mock_world)
    assert game_state.current_world == mock_world
    assert game_state.current_world.id == "world_001"

def test_add_character(game_state, mock_character):
    """
    Test that a character can be added to the game state.
    """
    game_state.add_character(mock_character)
    assert "char_001" in game_state.characters
    assert game_state.characters["char_001"] == mock_character
    assert game_state.characters["char_001"].name == "Hero"

def test_update_quests(game_state, mock_quest):
    """
    Test that a quest can be added or updated in the game state.
    """
    game_state.update_quests(mock_quest)
    assert "quest_001" in game_state.quests
    assert game_state.quests["quest_001"] == mock_quest
    assert game_state.quests["quest_001"].name == "Save the Village"

def test_multiple_characters(game_state, mock_character):
    """
    Test adding multiple characters to the game state.
    """
    character_2 = Character(name="Villain", stats=CharacterStats(), id="char_002")
    game_state.add_character(mock_character)
    game_state.add_character(character_2)
    
    assert "char_001" in game_state.characters
    assert "char_002" in game_state.characters
    assert game_state.characters["char_001"].name == "Hero"
    assert game_state.characters["char_002"].name == "Villain"

def test_multiple_quests(game_state, mock_quest):
    """
    Test adding multiple quests to the game state.
    """
    quest_2 = Quest(name="Find the Artifact", description="Find the Artifact", id="quest_002")
    game_state.update_quests(mock_quest)
    game_state.update_quests(quest_2)
    
    assert "quest_001" in game_state.quests
    assert "quest_002" in game_state.quests
    assert game_state.quests["quest_001"].name == "Save the Village"
    assert game_state.quests["quest_002"].name == "Find the Artifact"

def test_update_world_assert_error(game_state):
    """
    Test that updating the world without an id raises an assertion error.
    """
    class MockWorldNoID:
        def __init__(self, name):
            self.name = name

    mock_world_no_id = MockWorldNoID(name="World Without ID")
    
    with pytest.raises(AssertionError, match="World must have an 'id' attribute"):
        game_state.update_world(mock_world_no_id)

def test_add_character_assert_error(game_state):
    """
    Test that adding a character without an id raises an assertion error.
    """
    class MockCharacterNoID:
        def __init__(self, name):
            self.name = name

    mock_character_no_id = MockCharacterNoID(name="Character Without ID")

    with pytest.raises(AssertionError, match="Character must have an 'id' attribute"):
        game_state.add_character(mock_character_no_id)

def test_update_quests_assert_error(game_state):
    """
    Test that updating quests without an id raises an assertion error.
    """
    class MockQuestNoID:
        def __init__(self, name):
            self.name = name

    mock_quest_no_id = MockQuestNoID(name="Quest Without ID")

    with pytest.raises(AssertionError, match="Quest must have an 'id' attribute"):
        game_state.update_quests(mock_quest_no_id)
