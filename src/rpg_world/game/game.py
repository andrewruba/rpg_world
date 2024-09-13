import time

class Game:
    def __init__(self, external_timer=None, target_fps=30):
        """
        Initialize the game. Set up game state, load resources, etc.
        """
        self.is_running = True
        self.external_timer = external_timer if external_timer else time.time  # Use provided timer or default to time.time
        self.target_fps = target_fps  # Target frame rate
        self.frame_duration = 1.0 / self.target_fps

        # Initialize game components (e.g., characters, spells, UI)
        self.init_game()

    def init_game(self):
        """
        Initialize the game state, characters, and other resources.
        """
        print("Initializing game...")

    def handle_input(self):
        """
        Handle user inputs (e.g., keyboard, mouse, controller).
        """
        # Placeholder for input handling
        pass

    def update_game(self, delta_time):
        """
        Update the game state (e.g., characters, physics, AI).
        
        Args:
            delta_time (float): Time passed since the last frame.
        """
        # Calculate the current FPS (frames per second)
        if delta_time > 0:
            fps = 1.0 / delta_time
        else:
            fps = float('inf')  # To avoid division by zero in case delta_time is 0

        # Display the FPS and delta time
        print(f"Updating game. Delta time: {delta_time:.8f} seconds, FPS: {fps:.8f}")

        # Placeholder for game update logic
        # For example, update player positions, handle physics, AI, etc.

    def render(self):
        """
        Render the current game state to the screen.
        """
        # Placeholder for rendering logic
        print("Rendering game...")

    def _sync_to_target_frame_rate(self, current_time):
        """
        Internal method to sync to the target frame rate. Uses a combination of
        sleep and busy-waiting to ensure precise timing for each frame.
        
        Args:
            current_time (float): The current time when the frame started.
        """
        # Calculate the time to the next frame
        time_to_next_frame = self.frame_duration - (self.external_timer() - current_time)
        
        # Sleep for 70% of the remaining frame time
        if time_to_next_frame > 0:
            time.sleep(time_to_next_frame * 0.7)

        # Busy-wait for the remaining time to hit the exact frame duration
        while self.external_timer() - current_time < self.frame_duration:
            pass

    def run(self):
        """
        Main game loop. This runs continuously until the game is closed.
        """
        last_time = self.external_timer() - self.frame_duration
        while self.is_running:
            current_time = self.external_timer()
            delta_time = current_time - last_time
            last_time = current_time

            # Handle input, update game state, and render
            self.handle_input()
            self.update_game(delta_time)
            self.render()

            # Sync to the target frame rate using the internal sync method
            self._sync_to_target_frame_rate(current_time)

    def stop(self):
        """
        Stop the game loop.
        """
        self.is_running = False
        print("Game stopped.")

