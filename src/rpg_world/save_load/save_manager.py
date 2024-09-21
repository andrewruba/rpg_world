import pickle
import os
from ..utils.logger import Logger

class SaveManager:
    """
    Manages saving the current game state to a file. Handles serialization of game data using pickle.
    """

    def __init__(self, save_directory='./save_data/', file_name='game_save.pkl'):
        """
        Initialize the SaveManager, which handles saving the game state to a file.

        Args:
            save_directory (str): The directory where save files will be stored. Defaults to './save_data/'.
            file_name (str): The name of the save file. Defaults to 'game_save.pkl'.
        """
        self.save_directory = save_directory
        self.file_name = file_name
        self.save_path = os.path.join(save_directory, file_name)
        self.logger = Logger("SaveManager")

        # Create the save directory if it doesn't exist
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)
            self.logger.info(f"Created save directory at {self.save_directory}")

    def save_game(self, game_state):
        """
        Save the current game state to a file using pickle serialization.

        Args:
            game_state (GameState): The current state of the game to be saved.
        """
        try:
            with open(self.save_path, 'wb') as save_file:
                pickle.dump(game_state, save_file)
            self.logger.info(f"Game saved successfully to {self.save_path}.")
        except Exception as e:
            self.logger.error(f"Error saving game: {e}")
