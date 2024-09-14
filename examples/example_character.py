from rpg_world import BaseCharacter
from rpg_world import CharacterStats

class Warrior(BaseCharacter):
    def __init__(self, name, health=100, strength=15, defense=5):
        """
        Initialize a Warrior character with basic attributes.

        Args:
            name (str): The name of the warrior.
            health (int): The initial health of the warrior.
            strength (int): The attack strength of the warrior.
            defense (int): The defensive value of the warrior.
        """
        # Create CharacterStats with provided attributes
        stats = CharacterStats(health=health, strength=strength, defense=defense)

        # Initialize BaseCharacter with name and stats
        super().__init__(name, stats)

if __name__ == "__main__":
    # Create a warrior character
    conan = Warrior(name="Conan", health=100, strength=20, defense=5)
    print(conan)

    # Create an enemy character
    enemy_orc = Warrior(name="Enemy Orc", health=80, strength=15, defense=3)
    print(enemy_orc)
