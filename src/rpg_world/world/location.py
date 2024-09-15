class Location:
    def __init__(self, name, description, connected_locations=None, events=None):
        """
        Initialize a Location in the game world.

        Args:
            name (str): The name of the location.
            description (str): A description of the location.
            connected_locations (list): A list of connected location names (optional).
            events (list): A list of events that can occur in this location (optional).
        """
        self.name = name
        self.description = description
        self.connected_locations = connected_locations or []
        self.events = events or []

    def add_connected_location(self, location_name):
        """
        Add a new connected location to this location.

        Args:
            location_name (str): The name of the connected location.
        """
        self.connected_locations.append(location_name)

    def show_description(self):
        """
        Display the description of the location.
        """
        print(self.description)

    def list_connected_locations(self):
        """
        List all connected locations from this location.
        """
        if self.connected_locations:
            print(f"From {self.name}, you can go to: {', '.join(self.connected_locations)}")
        else:
            print(f"{self.name} is isolated.")
