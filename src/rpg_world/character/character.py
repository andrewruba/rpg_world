from abc import ABC
from ..stats.character_stats import CharacterStats
from ..item.inventory import Inventory
from ..utils.logger import Logger

class Character(ABC):
    def __init__(self, name: str, stats: CharacterStats, id: str = None):
        """
        Initialize a base character with character statistics, an inventory, and an optional ID.

        Args:
            name (str): The character's name.
            stats (CharacterStats): An instance of CharacterStats that holds the character's core attributes.
            id (str, optional): A unique identifier for the character. Defaults to None.
        """
        self.id = id
        self.name = name
        self.stats = stats
        self.inventory = Inventory()

        # Initialize logger for this character
        self.logger = Logger(f"Character-{self.name}")
        self.logger.info(f"Character '{self.name}' initialized with stats: {self.stats}")

    def is_alive(self) -> bool:
        """
        Checks if the character is alive by verifying if their health is greater than 0.

        Returns:
            bool: True if the character's health is above 0, False otherwise.
        """
        return self.stats.is_alive()

    def __getattr__(self, attr_name):
        """
        Dynamically return attributes from CharacterStats if they exist.

        Args:
            attr_name (str): The name of the attribute to retrieve from the character's stats.

        Returns:
            Any: The value of the attribute from CharacterStats.

        Raises:
            AttributeError: If the attribute does not exist in CharacterStats.
        """
        if attr_name in self.stats.attributes:
            return self.stats.get(attr_name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr_name}'")

    def __setattr__(self, attr_name, value):
        """
        Dynamically set attributes in CharacterStats if they exist in the stats dictionary.

        Args:
            attr_name (str): The name of the attribute to set.
            value (Any): The value to set for the attribute.
        """
        if attr_name in ['name', 'stats', 'inventory', 'id']:
            super().__setattr__(attr_name, value)
        elif attr_name in self.stats.attributes:
            self.stats.set(attr_name, value)
        else:
            super().__setattr__(attr_name, value)

    def __str__(self):
        """
        Provides a string representation of the character's name and current stats.

        Returns:
            str: A string containing the character's name and their stats.
        """
        return f"{self.name}: {self.stats}"
