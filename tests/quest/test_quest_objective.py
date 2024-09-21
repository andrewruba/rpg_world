import pytest
from rpg_world import (
    QuestObjective,
    HealthBelowThresholdTrigger,
    GameState,
    Character,
    CharacterStats
)

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
    Fixture to create a basic QuestObjective instance.
    """
    return QuestObjective(name="Test Objective", description="Test description")

@pytest.fixture
def quest_objective_with_trigger():
    """
    Fixture to create a QuestObjective instance with a trigger.
    """
    trigger = HealthBelowThresholdTrigger(character_id="hero", threshold=50)
    return QuestObjective(name="Health Objective", description="Objective when health is low", triggers=[trigger])

def test_quest_objective_initialization(quest_objective):
    """
    Test that the QuestObjective is initialized correctly.
    """
    assert quest_objective.name == "Test Objective"
    assert quest_objective.description == "Test description"
    assert not quest_objective.is_complete()
    assert len(quest_objective.triggers) == 0

def test_quest_objective_with_triggers_initialization(quest_objective_with_trigger):
    """
    Test that the QuestObjective with a trigger is initialized correctly.
    """
    assert quest_objective_with_trigger.name == "Health Objective"
    assert quest_objective_with_trigger.description == "Objective when health is low"
    assert len(quest_objective_with_trigger.triggers) == 1

def test_quest_objective_completion(mock_game_state, quest_objective_with_trigger):
    """
    Test that completing a quest objective works correctly.
    """
    assert not quest_objective_with_trigger.is_complete()  # Should be incomplete initially
    quest_objective_with_trigger.check_triggers(mock_game_state)
    assert not quest_objective_with_trigger.is_complete()  # Should not yet be marked as complete

    mock_game_state.characters['hero'].health = 49  # Set below trigger threshold of 50
    quest_objective_with_trigger.check_triggers(mock_game_state)
    assert quest_objective_with_trigger.is_complete()  # Should now marked as complete

def test_quest_objective_string_representation(quest_objective):
    """
    Test the string representation of a QuestObjective.
    """
    objective_str = str(quest_objective)
    assert "Objective: Test Objective - Test description [Incomplete]" in objective_str
    quest_objective.triggered = True
    objective_str = str(quest_objective)
    assert "Objective: Test Objective - Test description [Completed]" in objective_str
