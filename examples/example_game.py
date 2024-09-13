from rpg_world.game import Game  # Import the Game class from your rpg_world package
import time

# Entry point for the game example
if __name__ == "__main__":
    target_fps = 60

    # Example using internal timer
    game = Game(target_fps=target_fps)

    # Simulate running the game for a few seconds with the internal timer
    print("Running the game with the internal timer for 3 seconds...")
    start_time = time.time()
    while time.time() - start_time < 3:
        game.run()

    game.stop()

    # Example with external timer
    def external_timer():
        """
        Simulate an external engine providing time in a real-world integration.
        """
        return time.time()

    # Now, using the external timer
    game_with_external_timer = Game(external_timer=external_timer, target_fps=target_fps)

    # Simulate running the game for a few seconds with the external timer
    print("Running the game with the external timer for 3 seconds...")
    start_time = time.time()
    while time.time() - start_time < 3:
        game_with_external_timer.run()

    game_with_external_timer.stop()
