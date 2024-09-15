from .item import Item

class Consumable(Item):
    def __init__(self, name: str, description: str, value: int, healing_amount: int):
        """
        Initialize a consumable item.

        Args:
            name (str): The name of the consumable.
            description (str): A brief description of the consumable.
            value (int): The monetary value of the consumable.
            healing_amount (int): The amount of health this consumable heals.
        """
        super().__init__(name, description, value)
        self.healing_amount = healing_amount

    def use(self, target):
        """
        Heal the target by the healing amount.

        Args:
            target (BaseCharacter): The character to be healed.
        """
        print(f"{target.name} uses {self.name} and heals for {self.healing_amount} health.")
        target.stats.modify('health', self.healing_amount)

    def __str__(self):
        """
        String representation of the consumable.

        Returns:
            str: A string describing the consumable.
        """
        return f"{super().__str__()}, Heals for {self.healing_amount}"
