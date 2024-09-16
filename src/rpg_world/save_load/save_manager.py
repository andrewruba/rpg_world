import pickle
import os

class SaveManager:
    def __init__(self, save_directory='./save_data/', file_name='game_save.pkl'):
        """
        Initialize the SaveManager.

        Args:
            save_directory (str): Directory where save files will be stored.
            file_name (str): Name of the save file.
        """
        self.save_directory = save_directory
        self.file_name = file_name
        self.save_path = os.path.join(save_directory, file_name)

        # Create the save directory if it doesn't exist
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

    def save_game(self, game_state):
        """
        Save the current game state to a file using pickle.

        Args:
            game_state (GameState): The current state of the game to be saved.
        """
        try:
            with open(self.save_path, 'wb') as save_file:
                pickle.dump(game_state, save_file)
            print(f"Game saved successfully to {self.save_path}.")
        except Exception as e:
            print(f"Error saving game: {e}")
