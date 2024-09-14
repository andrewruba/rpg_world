from abc import ABC
from .character_stats import CharacterStats

class BaseCharacter(ABC):
    def __init__(self, name: str, stats: CharacterStats = None, **kwargs):
        """
        Initialize a base character with character statistics.

        Args:
            name (str): The character's name.
            stats (CharacterStats, optional): An instance of CharacterStats.
            **kwargs: Additional attributes to be passed to CharacterStats if stats is not provided.
        """
        self.name = name
        if stats:
            self.stats = stats
        else:
            self.stats = CharacterStats(**kwargs)

        self.is_alive_flag = True  # Track if the character is alive or not

    def get_attribute(self, attr_name: str):
        """
        Retrieve the value of a specific attribute from CharacterStats.

        Args:
            attr_name (str): The name of the attribute to retrieve.

        Returns:
            The value of the attribute or None if it doesn't exist.
        """
        return self.stats.get(attr_name)

    def set_attribute(self, attr_name: str, value):
        """
        Set the value of a specific attribute in CharacterStats.

        Args:
            attr_name (str): The name of the attribute to set.
            value: The value to assign to the attribute.
        """
        self.stats.set(attr_name, value)

    def process_effect(self, effect: dict):
        """
        Process an effect applied to the character.

        Args:
            effect (dict): A dictionary describing the effect.
        """
        attribute = effect.get('attribute')
        amount = effect.get('amount')

        if not attribute:
            print(f"No attribute specified in effect: {effect}")
            return

        self.stats.modify(attribute, amount)
        print(f"{self.name}'s {attribute} changed by {amount}. New value: {self.get_attribute(attribute)}")

        # Update alive status
        if attribute == 'health' and not self.stats.is_alive():
            self.is_alive_flag = False
            print(f"{self.name} has died.")

    def is_alive(self) -> bool:
        """
        Checks if the character is still alive.

        Returns:
            bool: True if the character is alive, False otherwise.
        """
        return self.is_alive_flag

    def __str__(self):
        """
        String representation of the character's name and stats.
        """
        return f"{self.name}: {self.stats}"
