from .item import Item
from ..utils.logger import Logger

class Equipment(Item):
    def __init__(self, name: str, description: str, value: int, effects: list):
        """
        Initialize an equippable item like a weapon or armor.

        Args:
            name (str): The name of the equipment.
            description (str): A brief description of the equipment.
            value (int): The monetary value of the equipment.
            effects (list): A list of effects (instances of Effect) that the equipment applies.
        """
        super().__init__(name, description, value, effects)
        self.equipped = False

        # Initialize logger for this equipment
        self.logger = Logger(f"Equipment-{self.name}")
        self.logger.info(f"Equipment '{self.name}' initialized with {len(self.effects)} effects")

    def use(self, target):
        """
        Toggle the equipped status of the item. If the item is equipped, it applies effects.
        If the item is unequipped, it un-applies the effects.

        Args:
            target (Character): The character equipping or unequipping the item.
        """
        if self.equipped:
            self.unequip(target)
        else:
            self.equip(target)

    def equip(self, target):
        """
        Equip the item and apply its effects to the target.

        Args:
            target (Character): The character equipping the item.
        """
        if not self.equipped:
            self.logger.info(f"{target.name} equips {self.name}!")
            for effect in self.effects:
                effect.apply(target)
            self.equipped = True

    def unequip(self, target):
        """
        Unequip the item and unapply its effects from the target.

        Args:
            target (Character): The character unequipping the item.
        """
        if self.equipped:
            self.logger.info(f"{target.name} unequips {self.name}!")
            for effect in self.effects:
                effect.unapply(target)
            self.equipped = False
