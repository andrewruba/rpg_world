class World:
    def __init__(self):
        """
        Initialize the World with locations and an entry point.
        """
        self.locations = {}
        self.current_location = None

    def add_location(self, location):
        """
        Add a new location to the world.

        Args:
            location (Location): The location to add to the world.
        """
        self.locations[location.name] = location

    def set_starting_location(self, location_name):
        """
        Set the initial location for the player in the world.

        Args:
            location_name (str): The name of the location where the player starts.
        """
        if location_name in self.locations:
            self.current_location = self.locations[location_name]
            print(f"Starting location set to: {self.current_location.name}")
        else:
            print(f"Location {location_name} not found in the world.")

    def move_to_location(self, location_name):
        """
        Move the player to a different location in the world.

        Args:
            location_name (str): The name of the location to move to.
        """
        if location_name in self.locations:
            self.current_location = self.locations[location_name]
            print(f"Moved to: {self.current_location.name}")
        else:
            print(f"Location {location_name} not found in the world.")
