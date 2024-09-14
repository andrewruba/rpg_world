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

    def attack(self, target):
        """
        Warrior attacks the target.

        Args:
            target (BaseCharacter): The target being attacked.
        """
        strength = self.get_attribute('strength')
        target_defense = target.get_attribute('defense') or 0
        damage = max(0, strength - target_defense)
        effect = {'attribute': 'health', 'amount': -damage}
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.process_effect(effect)
        if not target.is_alive():
            print(f"{target.name} has been defeated!")

if __name__ == "__main__":
    # Create a warrior character
    conan = Warrior(name="Conan", health=100, strength=20, defense=5)
    print(conan)

    # Create an enemy character
    enemy_orc = Warrior(name="Enemy Orc", health=80, strength=15, defense=3)
    print(enemy_orc)

    # Conan attacks the Enemy Orc
    conan.attack(enemy_orc)
    print(enemy_orc)

    # Enemy Orc attacks Conan
    enemy_orc.attack(conan)
    print(conan)

    # Conan attacks again
    conan.attack(enemy_orc)
    print(enemy_orc)

