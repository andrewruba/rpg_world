from .place import Place

class World(Place):
    """
    Represents the game world, which contains multiple locations and manages the player's movement between them.
    """

    def __init__(self, name, id=None):
        """
        Initialize the World with a name and an optional identifier. The world contains locations and tracks the player's current location.

        Args:
            name (str): The name of the world.
            id (str, optional): An optional unique identifier for the world. Defaults to None.
        """
        super().__init__(name, id)
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
            self.logger.info(f"Starting location set to: {self.current_location.name}")
        else:
            self.logger.warning(f"Location {location_name} not found in the world.")

    def move_to_location(self, location_name, new_position=None):
        """
        Move the player to a different location in the world, ensuring the new location is connected to the current one.

        Args:
            location_name (str): The name of the location to move to.
            new_position (Position, optional): A position within the new location to move to. Defaults to (0, 0).
        """
        if location_name not in self.locations:
            self.logger.warning(f"Location {location_name} not found in the world.")
            return
        
        if location_name not in self.current_location.connected_locations:
            self.logger.warning(f"You cannot move to {location_name} from {self.current_location.name}. The locations are not connected.")
            return
        
        self.current_location = self.locations[location_name]
        self.logger.info(f"Moved to: {self.current_location.name}")
        
        # Update position in the new location
        if new_position:
            self.current_location.update_position(new_position)
