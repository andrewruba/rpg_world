from .base_stats import BaseStats

class CharacterStats(BaseStats):
    """
    Manages character statistics such as health, mana, focus, and armor.
    Provides methods to modify and retrieve these attributes safely.
    """

    def __init__(self, health=100, mana=100, focus=100, armor=0, **kwargs):
        """
        Initialize the character's statistics with default or provided values.

        Args:
            health (float): The current health of the character.
            mana (float): The current mana of the character.
            focus (float): The current focus of the character.
            armor (float): The armor value, reducing incoming damage.
            **kwargs: Additional attributes as key-value pairs.
        """
        super().__init__(
            health=health, max_health=health,
            mana=mana, max_mana=mana,
            focus=focus, max_focus=focus,
            armor=armor, **kwargs
        )

    def is_alive(self):
        """
        Check if the character is still alive.

        Returns:
            bool: True if health is greater than zero, False otherwise.
        """
        return self.get('health') > 0

    def modify(self, attr_name, amount):
        """
        Modify the value of an attribute by a specified amount.

        Args:
            attr_name (str): The name of the attribute to modify.
            amount (float): The amount to add (or subtract) from the attribute.
        """
        current_value = self.get(attr_name) or 0
        new_value = current_value + amount
        self.set(attr_name, new_value)
