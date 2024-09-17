from abc import ABC, abstractmethod
from ..utils.logger import Logger

class BaseItem(ABC):
    def __init__(self, name: str, description: str, value: int, effects: list):
        """
        Initialize the base item class with effects.

        Args:
            name (str): The name of the item.
            description (str): A brief description of the item.
            value (int): The monetary value of the item.
            effects (list): A list of effects (instances of BaseEffect) that the item applies.
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
        Apply all the item's effects to the target character.

        Args:
            target (BaseCharacter): The character that will use the item.
            **kwargs: Additional context for the effects to use in their calculations.
        """
        self.logger.info(f"{target.name} uses {self.name}!")
        
        # Apply each effect
        for effect in self.effects:
            effect.apply(target, **kwargs)

    def __str__(self):
        """
        String representation of the item.

        Returns:
            str: A string describing the item.
        """
        effects_descriptions = ", ".join([str(effect) for effect in self.effects])
        return f"Item: {self.name}, Value: {self.value}, Description: {self.description}, Effects: {effects_descriptions}"
