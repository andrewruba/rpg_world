from abc import ABC
from ..utils.logger import Logger

class Place(ABC):
    """
    Abstract base class for all places in the game world, including entities like World, Location, and Position.
    """

    def __init__(self, name, id=None):
        """
        Initialize the place with a name and optional identifier.

        Args:
            name (str): The name of the place.
            id (str, optional): An optional unique identifier for the place. Defaults to None.
        """
        self.id = id
        self.name = name

        # Initialize logger for this place
        self.logger = Logger(f"{self.__class__.__name__}-{self.name}")
        self.logger.info(f"{self.__class__.__name__} '{self.name}' initialized")
