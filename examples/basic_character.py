from rpg_simulator.character.base_character import BaseCharacter

class Warrior(BaseCharacter):
    def take_action(self, action_name: str, target=None):
        """
        Defines how the Warrior performs actions.

        Args:
            action_name (str): The name of the action (e.g., 'attack').
            target (BaseCharacter): The target of the action.
        """
        if action_name == 'attack' and target:
            strength = self.get_attribute('strength') or 10  # Default to 10 if 'strength' not defined
            effect = {'attribute': 'health', 'amount': -strength}  # Damage is calculated externally as a negative value
            print(f"{self.name} attacks {target.name} for {strength} damage!")
            target.process_effect(effect)
        else:
            print(f"{self.name} doesn't know how to perform '{action_name}'.")


if __name__ == "__main__":
    # Create a warrior character
    attributes = {'health': 100, 'max_health': 100, 'strength': 20, 'defense': 5}
    conan = Warrior(name="Conan", attributes=attributes)
    print(conan)

    # Create an enemy character
    attributes_enemy = {'health': 80, 'max_health': 80, 'strength': 15}
    enemy = Warrior(name="Enemy Orc", attributes=attributes_enemy)
    
    # Conan attacks the enemy
    conan.take_action('attack', target=enemy)
    print(enemy)
    
    # Conan receives a buff to strength
    conan.process_effect({'attribute': 'strength', 'amount': 5})
    print(conan)
    
    # Heal Conan by adding to health
    conan.process_effect({'attribute': 'health', 'amount': 10})
    print(conan)
