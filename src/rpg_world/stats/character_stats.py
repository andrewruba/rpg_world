from .stats import Stats

class CharacterStats(Stats):
    """
    Manages character statistics such as health, mana, focus, and armor.
    Ensures stats like health, mana, and focus are handled safely with max values.
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
        return self.health > 0
