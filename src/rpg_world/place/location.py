from .place import Place
from .position import Position

class Location(Place):
    """
    Represents a specific location in the game world. A location can have connected locations and a current position.
    """

    def __init__(self, name, description, connected_locations=None, initial_position=None, id=None):
        """
        Initialize a Location in the game world.

        Args:
            name (str): The name of the location.
            description (str): A description of the location.
            connected_locations (list, optional): A list of connected location names (optional).
            initial_position (Position, optional): The initial position of the player in the location. Defaults to (0, 0).
            id (str, optional): An optional identifier for the location. Defaults to None.
        """
        super().__init__(name, id)
        self.name = name
        self.description = description
        self.connected_locations = connected_locations or []
        self.current_position = initial_position if initial_position else Position(f"{name} Position", 0, 0)

    def add_connected_location(self, location_name):
        """
        Add a new connected location to this location.

        Args:
            location_name (str): The name of the connected location to add.
        """
        self.connected_locations.append(location_name)

    def update_position(self, new_position):
        """
        Update the player's position in this location.

        Args:
            new_position (Position): The new position to update to.
        """
        self.current_position = new_position
        self.logger.info(f"Moved to position: {self.current_position}")
