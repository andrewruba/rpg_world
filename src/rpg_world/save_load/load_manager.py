import pickle
import os
from ..utils.logger import Logger

class LoadManager:
    def __init__(self, save_directory='./save_data/', file_name='game_save.pkl'):
        """
        Initialize the LoadManager.

        Args:
            save_directory (str): Directory where save files are stored.
            file_name (str): Name of the save file.
        """
        self.save_directory = save_directory
        self.file_name = file_name
        self.save_path = os.path.join(save_directory, file_name)
        self.logger = Logger("LoadManager")

    def load_game(self):
        """
        Load the saved game state from a file using pickle.

        Returns:
            GameState: The game state object loaded from the save file, or None if loading fails.
        """
        try:
            with open(self.save_path, 'rb') as save_file:
                game_state = pickle.load(save_file)
                self.logger.info(f"Game loaded successfully from {self.save_path}.")
                return game_state
        except FileNotFoundError:
            self.logger.warning(f"Save file not found: {self.save_path}.")
            return None
        except Exception as e:
            self.logger.error(f"Error loading game: {e}")
            return None
