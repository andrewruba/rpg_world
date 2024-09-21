from abc import ABC, abstractmethod
from ..utils.logger import Logger

class Item(ABC):
    """
    Represents a base class for all items in the game. Items can have effects and can be used by characters.
    """

    def __init__(self, name: str, description: str, value: int, effects: list):
        """
        Initialize the base item class with a name, description, value, and a list of effects.

        Args:
            name (str): The name of the item.
            description (str): A brief description of the item.
            value (int): The monetary value of the item.
            effects (list): A list of effects (instances of Effect) that the item applies when used.
        """
        self.name = name
        self.description = description
        self.value = value
        self.effects = effects

        # Initialize logger for this item
        self.logger = Logger(f"Item-{self.name}")
        self.logger.info(f"Item '{self.name}' initialized with description: '{self.description}', value: {self.value}, and {len(self.effects)} effects")

    def use(self, target, **kwargs):
        """
        Apply all the item's effects to the target character. This method should be implemented by subclasses.

        Args:
            target (Character): The character that will use the item.
            **kwargs: Additional context for the effects to use in their calculations.
        """
        self.logger.info(f"{target.name} uses {self.name}!")
        
        # Apply each effect
        for effect in self.effects:
            effect.apply(target, **kwargs)

    def __str__(self):
        """
        String representation of the item, including its name, value, description, and effects.

        Returns:
            str: A string describing the item, its value, description, and effects.
        """
        effects_descriptions = ", ".join([str(effect) for effect in self.effects])
        return f"Item: {self.name}, Value: {self.value}, Description: {self.description}, Effects: {effects_descriptions}"
