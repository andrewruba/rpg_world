import pytest
from rpg_world import GameState, Character, Quest, World, CharacterStats
from rpg_world import HealthBelowThresholdTrigger, PlayerInLocationTrigger, QuestCompletedTrigger

@pytest.fixture
def game_state():
    """
    Fixture to initialize a new GameState instance for testing.
    """
    return GameState()

@pytest.fixture
def mock_character():
    """
    Fixture to create a mock character with health attribute.
    """
    return Character(name="Hero", stats=CharacterStats(), id="char_001")

@pytest.fixture
def mock_world():
    """
    Fixture to create a mock World and Location.
    """
    world = World(name="Test World", id="world_001")
    location = World(name="Test Location", id="location_001")
    world.add_location(location)
    world.set_starting_location("Test Location")
    return world

@pytest.fixture
def mock_quest():
    """
    Fixture to create a mock quest with completion status.
    """
    return Quest(name="Save the Village", description="Save the Village", id="quest_001")

def test_health_below_threshold_trigger(game_state, mock_character):
    """
    Test the HealthBelowThresholdTrigger trigger.
    """
    game_state.add_character(mock_character)
    
    # Character health is above the threshold
    health_trigger = HealthBelowThresholdTrigger(character_id="char_001", threshold=50)
    assert health_trigger.evaluate(game_state) == False
    
    # Lower character's health below threshold
    mock_character.health = 40
    assert health_trigger.evaluate(game_state) == True

def test_player_in_location_trigger(game_state, mock_world):
    """
    Test the PlayerInLocationTrigger trigger.
    """
    game_state.update_world(mock_world)
    
    # Player is in the correct location
    location_trigger = PlayerInLocationTrigger(location_id="location_001")
    assert location_trigger.evaluate(game_state) == True
    
    # Move player to a new location and check again
    mock_world.current_location = World(name="Other Location", id="location_002")
    assert location_trigger.evaluate(game_state) == False

def test_quest_completed_trigger(game_state, mock_quest):
    """
    Test the QuestCompletedTrigger trigger.
    """
    game_state.update_quests(mock_quest)
    
    # Quest is not completed yet
    quest_trigger = QuestCompletedTrigger(quest_id="quest_001")
    assert quest_trigger.evaluate(game_state) == True

def test_quest_trigger_invalid_quest(game_state):
    """
    Test the QuestCompletedTrigger with an invalid quest id.
    """
    quest_trigger = QuestCompletedTrigger(quest_id="invalid_quest")
    
    # Should return False as the quest does not exist
    with pytest.raises(KeyError):
        quest_trigger.evaluate(game_state)
