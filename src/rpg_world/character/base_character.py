from abc import ABC
from ..stats.character_stats import CharacterStats
from ..utils.logger import Logger

class BaseCharacter(ABC):
    def __init__(self, name: str, stats: CharacterStats):
        """
        Initialize a base character with character statistics.

        Args:
            name (str): The character's name.
            stats (CharacterStats, optional): An instance of CharacterStats.
            **kwargs: Additional attributes to be passed to CharacterStats if stats is not provided.
        """
        self.name = name
        self.stats = stats

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
        if attr_name == 'name' or attr_name == 'stats':
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
