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

        # Ensure health is an attribute, set to 100 if not specified
        if 'health' not in self.attributes:
            self.attributes['health'] = 100

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
        Process an effect applied to the character. The effect modifies the attribute by the specified amount.

        Args:
            effect (dict): A dictionary describing the effect. Example:
                        {'attribute': 'health', 'amount': -30}
                        {'attribute': 'strength', 'amount': 10}
        """
        attribute = effect.get('attribute')
        amount = effect.get('amount')

        if attribute not in self.attributes:
            print(f"{self.name} does not have the attribute '{attribute}'. Adding it with initial value 0.")
            self.attributes[attribute] = 0  # Initialize the attribute if it doesn't exist

        current_value = self.get_attribute(attribute)
        new_value = current_value + amount

        # Cap certain attributes at 0 (e.g., health, mana, focus) to prevent negative values
        if attribute in ['health', 'mana', 'focus'] and new_value < 0:
            new_value = 0

        self.set_attribute(attribute, new_value)
        print(f"{self.name}'s {attribute} changed from {current_value} to {new_value} by adding {amount}.")

        # Check for character death based on health
        if attribute == 'health' and new_value == 0:
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
