from rpg_world import BaseCharacter

class Warrior(BaseCharacter):
    def __init__(self, name: str, attributes: dict):
        """
        Initialize a Warrior character with specific attributes.

        Args:
            name (str): The name of the warrior.
            attributes (dict): A dictionary of the warrior's attributes.
        """
        # Ensure necessary attributes are present, set defaults if not
        default_attributes = {
            'health': 100,
            'max_health': 100,
            'strength': 15,
            'defense': 5,
        }
        # Update default attributes with any provided attributes
        combined_attributes = {**default_attributes, **attributes}
        super().__init__(name, combined_attributes)

    def attack(self, target):
        """
        Warrior attacks the target.

        Args:
            target (BaseCharacter): The target being attacked.
        """
        strength = self.get_attribute('strength')
        # Calculate damage considering the target's defense
        target_defense = target.get_attribute('defense') or 0
        damage = max(0, strength - target_defense)
        effect = {'attribute': 'health', 'amount': -damage}
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.process_effect(effect)

    def defend(self):
        """
        Warrior takes a defensive stance, temporarily increasing defense.
        """
        # Increase defense temporarily
        defense_bonus = 5
        current_defense = self.get_attribute('defense')
        self.set_attribute('defense', current_defense + defense_bonus)
        print(f"{self.name} is defending and increases defense by {defense_bonus}.")

    def __str__(self):
        """
        String representation of the warrior's attributes.
        """
        attrs = ', '.join(f"{key}: {value}" for key, value in self.attributes.items())
        return f"Warrior {self.name}: {attrs}"

if __name__ == "__main__":
    # Create a warrior character
    conan_attributes = {'health': 100, 'max_health': 100, 'strength': 20, 'defense': 5}
    conan = Warrior(name="Conan", attributes=conan_attributes)
    print(conan)

    # Create an enemy character
    enemy_attributes = {'health': 80, 'max_health': 80, 'strength': 15, 'defense': 3}
    enemy_orc = Warrior(name="Enemy Orc", attributes=enemy_attributes)
    print(enemy_orc)

    # Conan attacks the enemy Orc
    conan.attack(enemy_orc)
    print(enemy_orc)

    # Conan receives a buff to strength
    conan.process_effect({'attribute': 'strength', 'amount': 5})
    print(conan)

    # Heal Conan by adding to health
    conan.process_effect({'attribute': 'health', 'amount': 10})
    print(conan)

    # Enemy Orc attacks Conan
    enemy_orc.attack(conan)
    print(conan)

    # Conan defends
    conan.defend()
    print(conan)
