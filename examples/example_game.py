from rpg_world.game import Game  # Import the Game class from your rpg_world package
import time

# Entry point for the game example
if __name__ == "__main__":
    # Initialize the game
    game = Game()

    # Run the game
    print("Running the game for 3 seconds...")
    game.run()

    # Stop the game after 3 seconds
    time.sleep(3)
    game.stop()

    print("Game has stopped.")
