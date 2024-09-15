from .item import Item

class Equipment(Item):
    def __init__(self, name: str, description: str, value: int, attack_bonus: int = 0, defense_bonus: int = 0):
        """
        Initialize an equippable item like a weapon or armor.

        Args:
            name (str): The name of the equipment.
            description (str): A brief description of the equipment.
            value (int): The monetary value of the equipment.
            attack_bonus (int): The bonus to attack when equipped (default is 0).
            defense_bonus (int): The bonus to defense when equipped (default is 0).
        """
        super().__init__(name, description, value)
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

    def equip(self, target):
        """
        Equip the item and apply its bonuses to the target.

        Args:
            target (BaseCharacter): The character equipping the item.
        """
        print(f"{target.name} equips {self.name}!")
        target.stats.modify('strength', self.attack_bonus)
        target.stats.modify('defense', self.defense_bonus)

    def unequip(self, target):
        """
        Unequip the item and remove its bonuses from the target.

        Args:
            target (BaseCharacter): The character unequipping the item.
        """
        print(f"{target.name} unequips {self.name}!")
        target.stats.modify('strength', -self.attack_bonus)
        target.stats.modify('defense', -self.defense_bonus)

    def __str__(self):
        """
        String representation of the equipment.

        Returns:
            str: A string describing the equipment.
        """
        return f"{super().__str__()}, Attack Bonus: {self.attack_bonus}, Defense Bonus: {self.defense_bonus}"
