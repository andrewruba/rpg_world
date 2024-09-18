import pytest
from rpg_world import Quest, QuestObjective
from rpg_world import HealthBelowThresholdTrigger
from rpg_world import GameState
from rpg_world import Character, CharacterStats

# Mock Logger to avoid actual logging in tests
class MockLogger:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def info(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

@pytest.fixture
def mock_logger(mocker):
    """
    Fixture to mock the Logger class.
    """
    mocker.patch('rpg_world.utils.logger.Logger', new=MockLogger)

@pytest.fixture
def mock_game_state():
    """
    Fixture to provide a mock game state for testing.
    """
    game_state = GameState()
    character = Character(name="Hero", stats = CharacterStats(), id="hero")
    game_state.add_character(character)
    return game_state

@pytest.fixture
def quest_objective():
    """
    Fixture to create a QuestObjective instance with a trigger.
    """
    trigger = HealthBelowThresholdTrigger(character_id="hero", threshold=50)
    return QuestObjective(name="Health Objective", description="Objective when health is low", triggers=[trigger])

@pytest.fixture
def quest_with_objectives(quest_objective):
    """
    Fixture to create a Quest instance with objectives.
    """
    return Quest(name="Treasure Hunt", description="Complete the treasure hunt", objectives=[quest_objective])

def test_quest_initialization(quest_with_objectives):
    """
    Test that a quest is initialized correctly.
    """
    assert quest_with_objectives.name == "Treasure Hunt"
    assert quest_with_objectives.description == "Complete the treasure hunt"
    assert quest_with_objectives.is_complete() is False  # Should not be completed initially

def test_add_objective_to_quest(quest_with_objectives):
    """
    Test that objectives can be added to a quest.
    """
    quest = quest_with_objectives
    assert len(quest.events) == 1  # One objective (event) should be added

    # Adding another objective
    new_objective = QuestObjective(name="Defeat the dragon", description="Slay the dragon.")
    quest.add_objective(new_objective)

    assert len(quest.events) == 2  # Two objectives should now be added

def test_quest_is_complete_with_incomplete_objectives(quest_with_objectives):
    """
    Test that a quest is not marked complete when objectives are incomplete.
    """
    quest = quest_with_objectives
    assert quest.is_complete() is False  # Initially, objectives are not completed

def test_quest_is_complete_with_completed_objectives(quest_with_objectives, mock_game_state):
    """
    Test that a quest is marked as complete when all objectives are completed.
    """
    quest = quest_with_objectives

    quest.check_quest_progress(mock_game_state)
    assert not quest.is_complete()

    mock_game_state.characters['hero'].health = 49 # Set health below trigger of 50
    quest.check_quest_progress(mock_game_state)
    assert quest.is_complete()  # Quest should now be marked as complete

def test_quest_completion_rewards():
    """
    Test that completing a quest gives the correct rewards.
    """
    rewards = {"gold": 100, "xp": 50}
    quest = Quest(name="Treasure Hunt", description="Find the treasure", rewards=rewards)

    assert quest.is_complete() is True
    assert quest.complete_quest() == rewards

def test_quest_progress_check(quest_with_objectives, mock_game_state):
    """
    Test that the quest progress check works correctly and triggers objectives.
    """
    quest = quest_with_objectives

    # Initially, the objective should be incomplete
    assert quest.is_complete() is False

    # Trigger the check, which should evaluate the progress of the quest objectives
    quest.check_quest_progress(mock_game_state)

    mock_game_state.characters['hero'].health = 49 # Set health below trigger of 50

    # Check progress again after completing objectives
    quest.check_quest_progress(mock_game_state)
    assert quest.is_complete() is True
