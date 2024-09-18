from abc import ABC
from ..utils.logger import Logger

class Place(ABC):
    """
    Abstract base class for game entities like World, Location, and Position.
    """

    def __init__(self, name):
        """
        Initialize the entity with a name.
        Args:
            name (str): The name of the entity.
        """
        self.name = name

        # Initialize logger for this ability
        self.logger = Logger(f"{self.__class__.__name__}-{self.name}")
        self.logger.info(f"{self.__class__.__name__} '{self.name}' initialized")
