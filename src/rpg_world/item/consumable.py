from .item import Item
from ..effect.effect import Effect
from ..utils.logger import Logger

class Consumable(Item):
    def __init__(self, name: str, description: str, value: int, effects: list):
        """
        Initialize a consumable item.

        Args:
            name (str): The name of the consumable.
            description (str): A brief description of the consumable.
            value (int): The monetary value of the consumable.
            effects (list): A list of effects (instances of Effect) that the consumable applies.
        """
        super().__init__(name, description, value, effects)

        # Initialize the logger
        self.logger = Logger(f"Consumable-{self.name}")

        # Log the initialization
        self.logger.info(f"Consumable '{self.name}' initialized with {len(self.effects)} effects")

        # Indicator to track if the consumable has been used
        self.is_used = False

    def use(self, target):
        """
        Use the consumable and apply its effects to the target.

        Args:
            target (Character): The character using the consumable.
        """
        if self.is_used:
            self.logger.warning(f"{self.name} has already been used and cannot be used again.")
            return
        
        self.logger.info(f"{target.name} uses {self.name}.")

        # Apply each effect to the target
        for effect in self.effects:
            self.logger.info(f"Applying effect: {effect}")
            effect.apply(target)

        # Mark the consumable as used
        self.is_used = True

        self.logger.info(f"{self.name} has been used.")
        self.logger.info(f"{target.name}'s stats after using {self.name}: {target.stats}")
