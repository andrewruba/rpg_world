import pytest
import os
import pickle
from rpg_world import LoadManager

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
def load_manager(temp_save_dir):
    """
    Fixture that initializes the LoadManager with the temporary directory.
    """
    return LoadManager(save_directory=temp_save_dir, file_name='test_game_save.pkl')

@pytest.fixture
def mock_game_state():
    """
    Fixture that provides a mock game state for testing.
    """
    return MockGameState(data={"level": 5, "health": 100, "quests": ["Find the treasure", "Defeat the dragon"]})

def test_load_game_success(load_manager, mock_game_state, temp_save_dir):
    """
    Test that the load_game function successfully loads a saved game state.
    """
    # First, save the mock game state to the test file
    save_path = os.path.join(temp_save_dir, 'test_game_save.pkl')
    with open(save_path, 'wb') as save_file:
        pickle.dump(mock_game_state, save_file)

    # Now, load the game state using the LoadManager
    loaded_state = load_manager.load_game()

    # Verify that the loaded state matches the saved state
    assert loaded_state is not None
    assert loaded_state.data == mock_game_state.data

def test_load_game_file_not_found(load_manager, temp_save_dir, caplog):
    """
    Test that the load_game function returns None when the save file does not exist.
    """
    # Ensure there is no save file in the directory
    assert not os.path.exists(os.path.join(temp_save_dir, 'test_game_save.pkl'))

    # Try to load the game state
    with caplog.at_level("WARNING"):
        loaded_state = load_manager.load_game()

    # Verify that None is returned when the file is not found
    assert loaded_state is None
    assert "Save file not found" in caplog.text

def test_load_game_corrupted_file(load_manager, temp_save_dir, caplog):
    """
    Test that the load_game function returns None when the save file is corrupted.
    """
    # Create a corrupted save file
    corrupted_save_path = os.path.join(temp_save_dir, 'test_game_save.pkl')
    with open(corrupted_save_path, 'wb') as save_file:
        save_file.write(b"corrupted data")

    # Try to load the corrupted game state
    with caplog.at_level("ERROR"):
        loaded_state = load_manager.load_game()

    # Verify that None is returned when the file is corrupted
    assert loaded_state is None
    assert "Error loading game" in caplog.text

def test_load_game_error_handling(load_manager, mocker, caplog):
    """
    Test that load_game handles unexpected exceptions correctly and returns None.
    """
    # Mock the open function to raise an exception
    mocker.patch('builtins.open', side_effect=Exception("Unexpected error"))

    # Try to load the game state
    with caplog.at_level("ERROR"):
        loaded_state = load_manager.load_game()

    # Verify that None is returned when an unexpected error occurs
    assert loaded_state is None
    assert "Error loading game" in caplog.text
