from abc import ABC, abstractmethod

class BaseCharacter(ABC):
    def __init__(self, name: str, attributes: dict):
        """
        Initialize a base character with a dynamic set of attributes.

        Args:
            name (str): The character's name.
            attributes (dict): A dictionary of character attributes (e.g., {'health': 100, 'strength': 20}).
        """
        self.name = name
        self.attributes = attributes
        self.is_alive_flag = True  # Track if the character is alive or not

    def get_attribute(self, attr_name: str):
        """
        Retrieve the value of a specific attribute.

        Args:
            attr_name (str): The name of the attribute to retrieve.
        
        Returns:
            The value of the attribute or None if it doesn't exist.
        """
        return self.attributes.get(attr_name)

    def set_attribute(self, attr_name: str, value):
        """
        Set the value of a specific attribute.

        Args:
            attr_name (str): The name of the attribute to set.
            value: The value to assign to the attribute.
        """
        self.attributes[attr_name] = value

    @abstractmethod
    def take_action(self, action_name: str, target=None):
        """
        Abstract method to define how the character performs an action.

        Args:
            action_name (str): The name of the action to perform.
            target: The target of the action (optional).
        """
        pass

    def process_effect(self, effect: dict):
        """
        Process an effect applied to the character. The effect is assumed to be pre-calculated, 
        with the 'amount' field being positive or negative based on the intended modification.

        Args:
            effect (dict): A dictionary describing the effect. Example:
                           {'attribute': 'health', 'amount': -30}
                           {'attribute': 'strength', 'amount': 10}
        """
        attribute = effect.get('attribute')
        amount = effect.get('amount')

        if attribute not in self.attributes:
            print(f"{self.name} does not have the attribute '{attribute}'")
            return

        current_value = self.get_attribute(attribute)
        new_value = current_value + amount

        self.set_attribute(attribute, new_value)
        print(f"{self.name}'s {attribute} changed from {current_value} to {new_value} by adding {amount}.")

        # Optional: Check for conditions like character death
        if attribute == 'health' and new_value <= 0:
            self.is_alive_flag = False
            print(f"{self.name} has died.")

    def is_alive(self) -> bool:
        """
        Checks if the character is still alive based on its attributes.
        
        Returns:
            bool: True if the character is alive, False if not.
        """
        return self.is_alive_flag

    def __str__(self):
        """
        String representation of the character's attributes.
        """
        attrs = ', '.join(f"{key}: {value}" for key, value in self.attributes.items())
        return f"{self.name}: {attrs}"

# Example of extending BaseCharacter:
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
            effect = {'attribute': 'health', 'amount': -strength}  # External calculation for negative amount
            print(f"{self.name} attacks {target.name} for {strength} damage!")
            target.process_effect(effect)
        else:
            print(f"{self.name} doesn't know how to perform '{action_name}'.")

# Example usage:
if __name__ == "__main__":
    # Create a warrior with dynamic attributes
    attributes = {'health': 100, 'max_health': 100, 'strength': 20, 'defense': 5}
    warrior = Warrior(name="Conan", attributes=attributes)
    print(warrior)

    # Create an enemy
    attributes_enemy = {'health': 80, 'max_health': 80, 'strength': 15}
    enemy = Warrior(name="Enemy Orc", attributes=attributes_enemy)
    
    # Warrior attacks enemy
    warrior.take_action('attack', target=enemy)
    print(enemy)
    
    # Warrior receives a buff to strength
    warrior.process_effect({'attribute': 'strength', 'amount': 5})
    print(warrior)
    
    # Heal the warrior by adding to health
    warrior.process_effect({'attribute': 'health', 'amount': 10})
    print(warrior)
