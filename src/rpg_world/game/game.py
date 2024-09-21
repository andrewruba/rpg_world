import time
from ..utils.logger import Logger

class Game:
    """
    Represents the main game loop and handles updating the game state, syncing to a target frame rate, and managing game resources.
    """

    def __init__(self, game_state, external_timer=None, target_fps=30, max_run_time=None):
        """
        Initialize the game. Set up the game state, configure the timer, and set up the frame rate and runtime limits.

        Args:
            game_state (GameState): The initial state of the game, which contains characters, quests, and world data.
            external_timer (function, optional): An optional custom timer function (defaults to `time.time`).
            target_fps (int, optional): The target frames per second for the game loop. Defaults to 30.
            max_run_time (float, optional): The maximum time in seconds after which the game loop will automatically stop. Defaults to None (no limit).
        """
        self.game_state = game_state
        self.is_running = True
        self.external_timer = external_timer if external_timer else time.time  # Use provided timer or default to time.time
        self.target_fps = target_fps  # Target frame rate
        self.frame_duration = 1.0 / self.target_fps  # Duration of each frame in seconds
        self.max_run_time = max_run_time  # Maximum time to run (None means no time limit)
        self.start_time = None  # To track when the game starts

        # Initialize logger for this game instance
        self.logger = Logger("Game")
        self.logger.info(f"""Game initialized with attributes: {
            {
                "target_fps": self.target_fps,
                "frame_duration": self.frame_duration,
                "max_run_time": self.max_run_time,
            }
        }""")

        # Initialize game components (e.g., characters, spells, UI)
        self.init_game()

    def init_game(self):
        """
        Initialize game components such as the game state, characters, world, and any other resources.
        This method is meant to be extended for additional game setup.
        """
        self.logger.info("Initializing game...")

    def update_game(self, delta_time):
        """
        Update the game state on each frame, including characters, physics, AI, and other gameplay elements.

        Args:
            delta_time (float): The amount of time passed since the last frame in seconds.
        """
        # Calculate the current FPS (frames per second)
        if delta_time > 0:
            fps = 1.0 / delta_time
        else:
            fps = float('inf')  # To avoid division by zero if delta_time is zero

        # Display the FPS and delta time
        self.logger.debug(f"Updating game. Delta time: {delta_time:.8f} seconds, FPS: {fps:.8f}")

    def _sync_to_target_frame_rate(self, current_time):
        """
        Synchronize the game loop to the target frame rate using a combination of sleep and busy-waiting.

        Args:
            current_time (float): The current time when the frame started.
        """
        # Calculate the time remaining to the next frame
        time_to_next_frame = self.frame_duration - (self.external_timer() - current_time)
        
        # Sleep for 70% of the remaining time to save CPU
        if time_to_next_frame > 0:
            time.sleep(time_to_next_frame * 0.7)

        # Busy-wait for the remaining time to hit the exact frame duration
        while self.external_timer() - current_time < self.frame_duration:
            pass

    def _check_time_elapsed(self, current_time):
        """
        Check if the maximum run time has been exceeded and stop the game if necessary.

        Args:
            current_time (float): The current time from the external timer.
        """
        if self.max_run_time is not None:
            time_elapsed = current_time - self.start_time
            if time_elapsed >= self.max_run_time:
                self.logger.info(f"Max run time of {self.max_run_time} seconds reached. Stopping the game.")
                self.stop()

    def run(self):
        """
        The main game loop. This loop continuously updates the game state until the game is stopped or the maximum runtime is exceeded.
        """
        self.start_time = self.external_timer()  # Track the time when the game starts
        last_time = self.start_time - self.frame_duration

        while self.is_running:
            current_time = self.external_timer()
            delta_time = current_time - last_time
            last_time = current_time

            # Update game state
            self.update_game(delta_time)

            # Check if the maximum run time has been reached
            self._check_time_elapsed(current_time)

            # Sync to the target frame rate
            self._sync_to_target_frame_rate(current_time)

    def stop(self):
        """
        Stop the game loop, effectively ending the game.
        """
        self.is_running = False
        self.logger.info("Game stopped.")
