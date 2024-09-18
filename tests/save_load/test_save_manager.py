import pytest
import os
import pickle
from rpg_world import SaveManager

# A mock GameState class for testing
class MockGameState:
    def __init__(self, data):
        self.data = data

@pytest.fixture
def temp_save_dir(tmp_path):
    """
    Fixture that creates a temporary directory for testing save files.
    """
    return tmp_path

@pytest.fixture
def save_manager(temp_save_dir):
    """
    Fixture that initializes the SaveManager with the temporary directory.
    """
    return SaveManager(save_directory=temp_save_dir, file_name='test_game_save.pkl')

@pytest.fixture
def mock_game_state():
    """
    Fixture that provides a mock game state for testing.
    """
    return MockGameState(data={"level": 5, "health": 100, "quests": ["Find the treasure", "Defeat the dragon"]})

def test_save_game_creates_file(save_manager, mock_game_state, temp_save_dir):
    """
    Test that the save_game function successfully creates a file and writes the game state.
    """
    save_manager.save_game(mock_game_state)

    # Ensure the save file was created in the temporary directory
    save_path = os.path.join(temp_save_dir, 'test_game_save.pkl')
    assert os.path.exists(save_path)

    # Ensure the file contains the correct game state by reading it back
    with open(save_path, 'rb') as f:
        saved_data = pickle.load(f)
        assert saved_data.data == mock_game_state.data

def test_save_game_creates_directory_if_not_exists(save_manager, mock_game_state, tmp_path):
    """
    Test that the save directory is created if it doesn't exist.
    """
    # Create a new path that doesn't exist
    new_save_dir = tmp_path / "non_existent_dir"
    save_manager_with_new_dir = SaveManager(save_directory=new_save_dir, file_name='test_game_save.pkl')

    save_manager_with_new_dir.save_game(mock_game_state)

    # Ensure the directory was created
    assert os.path.exists(new_save_dir)

    # Ensure the save file was created in the new directory
    save_path = os.path.join(new_save_dir, 'test_game_save.pkl')
    assert os.path.exists(save_path)

def test_save_game_error_handling(save_manager, mock_game_state, caplog):
    """
    Test error handling when saving the game fails.
    """
    # Simulate an error by setting an invalid directory
    save_manager.save_path = "/invalid/directory/test_game_save.pkl"
    
    with caplog.at_level("ERROR"):
        save_manager.save_game(mock_game_state)

    assert "No such file or directory" in caplog.text
