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
            stats (CharacterStats): An instance of CharacterStats.
            id (str, optional): A unique identifier for the character. Defaults to None.
        """
        self.id = id
        self.name = name
        self.stats = stats
        self.inventory = Inventory()

        # Initialize logger for this ability
        self.logger = Logger(f"Character-{self.name}")
        self.logger.info(f"Character '{self.name}' initialized with stats: {self.stats}")

    def is_alive(self) -> bool:
        """
        Checks if the character is still alive.

        Returns:
            bool: True if the character is alive, False otherwise.
        """
        return self.stats.is_alive()

    def __getattr__(self, attr_name):
        """
        Override __getattr__ to dynamically return attributes from CharacterStats if they exist.

        Args:
            attr_name (str): The name of the attribute to retrieve.

        Returns:
            The value of the attribute if it exists in CharacterStats.
        """
        if attr_name in self.stats.attributes:
            return self.stats.get(attr_name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr_name}'")

    def __setattr__(self, attr_name, value):
        """
        Override __setattr__ to dynamically set attributes in CharacterStats if they exist.
        """
        if attr_name in ['name', 'stats', 'inventory', 'id']:
            super().__setattr__(attr_name, value)
        elif attr_name in self.stats.attributes:
            self.stats.set(attr_name, value)
        else:
            super().__setattr__(attr_name, value)

    def __str__(self):
        """
        String representation of the character's name and stats.
        """
        return f"{self.name}: {self.stats}"
