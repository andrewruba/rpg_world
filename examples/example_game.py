from rpg_world.game import Game  # Import the Game class from your rpg_world package
import time

# Entry point for the game example
if __name__ == "__main__":
    target_fps = 60 # frames per second
    max_run_time = 3 # seconds

    # Example using internal timer
    game = Game(target_fps=target_fps, max_run_time=max_run_time)

    # Simulate running the game for a few seconds with the internal timer
    print(f"Running the game with the internal timer for {max_run_time} seconds...")
    game.run()
    game.stop()

    # Example with external timer
    def external_timer():
        """
        Simulate an external engine providing time in a real-world integration.
        """
        return time.time()

    # Now, using the external timer
    game_with_external_timer = Game(external_timer=external_timer, target_fps=target_fps, max_run_time=max_run_time)

    # Simulate running the game for a few seconds with the external timer
    print(f"Running the game with the external timer for {max_run_time} seconds...")
    game_with_external_timer.run()
    game_with_external_timer.stop()
