import pytest
from rpg_world import QuestManager
from rpg_world import Quest
from rpg_world import QuestObjective
from rpg_world import GameState

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
def quest_manager(mock_logger):
    """
    Fixture to initialize a QuestManager instance for testing.
    """
    return QuestManager()

@pytest.fixture
def quest_with_objectives():
    """
    Fixture to create a Quest with objectives.
    """
    objective1 = QuestObjective(name="Find the key", description="Locate the hidden key.")
    objective2 = QuestObjective(name="Open the door", description="Use the key to open the door.")
    return Quest(name="The Great Escape", description="Escape the dungeon", objectives=[objective1, objective2])

@pytest.fixture
def mock_game_state():
    """
    Fixture to provide a mock game state for testing.
    """
    return GameState()

def test_add_quest(quest_manager, quest_with_objectives):
    """
    Test adding a new quest to the QuestManager.
    """
    quest_manager.add_quest(quest_with_objectives)
    
    # Verify the quest was added to the manager
    assert len(quest_manager.get_all_quests()) == 1
    assert quest_manager.get_all_quests()[0] == quest_with_objectives

def test_remove_quest(quest_manager, quest_with_objectives):
    """
    Test removing a quest from the QuestManager.
    """
    quest_manager.add_quest(quest_with_objectives)
    
    # Verify the quest was added
    assert len(quest_manager.get_all_quests()) == 1
    
    # Now remove the quest
    quest_manager.remove_quest(quest_with_objectives)
    
    # Verify the quest was removed
    assert len(quest_manager.get_all_quests()) == 0

def test_get_incomplete_quests(quest_manager, quest_with_objectives):
    """
    Test retrieving incomplete quests from the QuestManager.
    """
    quest_manager.add_quest(quest_with_objectives)
    
    # Verify the quest is incomplete
    incomplete_quests = quest_manager.get_incomplete_quests()
    assert len(incomplete_quests) == 1
    assert incomplete_quests[0] == quest_with_objectives

def test_get_complete_quests(quest_manager, quest_with_objectives, mock_game_state):
    """
    Test retrieving completed quests from the QuestManager.
    """
    quest_manager.add_quest(quest_with_objectives)
    
    # Mark all objectives as complete
    for objective in quest_with_objectives.events:
        objective.triggered = True
    quest_with_objectives.check_quest_progress(mock_game_state)
    
    # Verify the quest is now complete
    complete_quests = quest_manager.get_complete_quests()
    assert len(complete_quests) == 1
    assert complete_quests[0] == quest_with_objectives

def test_get_incomplete_quests_after_completion(quest_manager, quest_with_objectives, mock_game_state):
    """
    Test retrieving incomplete quests after completing all objectives.
    """
    quest_manager.add_quest(quest_with_objectives)
    
    # Mark all objectives as complete
    for objective in quest_with_objectives.events:
        objective.triggered = True
    quest_with_objectives.check_quest_progress(mock_game_state)
    
    # There should be no incomplete quests now
    incomplete_quests = quest_manager.get_incomplete_quests()
    assert len(incomplete_quests) == 0

def test_add_multiple_quests(quest_manager, quest_with_objectives):
    """
    Test adding multiple quests to the QuestManager.
    """
    quest2 = Quest(name="Save the Princess", description="Rescue the princess from the castle")
    
    quest_manager.add_quest(quest_with_objectives)
    quest_manager.add_quest(quest2)
    
    # Verify both quests are added
    assert len(quest_manager.get_all_quests()) == 2
    assert quest_with_objectives in quest_manager.get_all_quests()
    assert quest2 in quest_manager.get_all_quests()

def test_quest_progress_check(quest_manager, quest_with_objectives, mock_game_state):
    """
    Test that the QuestManager can check progress of quests.
    """
    quest_manager.add_quest(quest_with_objectives)
    
    # Initially, objectives should be incomplete
    incomplete_quests = quest_manager.get_incomplete_quests()
    assert len(incomplete_quests) == 1
    
    # Complete the objectives
    for objective in quest_with_objectives.events:
        objective.triggered = True
    quest_with_objectives.check_quest_progress(mock_game_state)
    
    # Verify progress is reflected after checking events
    complete_quests = quest_manager.get_complete_quests()
    assert len(complete_quests) == 1
