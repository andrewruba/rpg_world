from .place import Place

class Position(Place):
    def __init__(self, name, x, y):
        """
        Initialize a Position within a location.

        Args:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
        """
        super().__init__(name)
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Position({self.name}, {self.x}, {self.y})"

    def equals(self, other_position):
        """
        Compare this position to another position.

        Args:
            other_position (Position): The position to compare against.

        Returns:
            bool: True if positions are equal, False otherwise.
        """
        return self.x == other_position.x and self.y == other_position.y

    def distance_to(self, other_position):
        """
        Calculate the Euclidean distance to another position.

        Args:
            other_position (Position): The other position to calculate distance to.

        Returns:
            float: The Euclidean distance.
        """
        return ((self.x - other_position.x) ** 2 + (self.y - other_position.y) ** 2) ** 0.5
