class CharacterStats:
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
        self.attributes = {
            'health': health,
            'max_health': health,
            'mana': mana,
            'max_mana': mana,
            'focus': focus,
            'max_focus': focus,
            'armor': armor,
        }

        # Include any additional attributes provided
        self.attributes.update(kwargs)

    def get(self, attr_name):
        """
        Retrieve the value of a specific attribute.

        Args:
            attr_name (str): The name of the attribute to retrieve.

        Returns:
            The value of the attribute or None if it doesn't exist.
        """
        return self.attributes.get(attr_name)

    def set(self, attr_name, value):
        """
        Set the value of a specific attribute.

        Args:
            attr_name (str): The name of the attribute to set.
            value: The value to assign to the attribute.
        """
        self.attributes[attr_name] = value

    def modify(self, attr_name, amount):
        """
        Modify the value of an attribute by a specified amount.

        Args:
            attr_name (str): The name of the attribute to modify.
            amount (float): The amount to add (or subtract) from the attribute.
        """
        current_value = self.get(attr_name) or 0
        new_value = current_value + amount

        # Ensure that health, mana, and focus do not fall below zero or exceed their maximums
        if attr_name in ['health', 'mana', 'focus']:
            max_attr = self.get(f'max_{attr_name}') or current_value
            new_value = max(0, min(new_value, max_attr))

        self.set(attr_name, new_value)

    def is_alive(self):
        """
        Check if the character is still alive.

        Returns:
            bool: True if health is greater than zero, False otherwise.
        """
        return self.get('health') > 0

    def __getattr__(self, attr_name):
        """
        Override __getattr__ to dynamically return attributes from the attributes dictionary.

        Args:
            attr_name (str): The name of the attribute to retrieve.

        Returns:
            The value of the attribute if it exists in the dictionary.
        """
        if attr_name in self.attributes:
            return self.attributes[attr_name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr_name}'")

    def __setattr__(self, attr_name, value):
        """
        Override __setattr__ to dynamically set attributes in the attributes dictionary.

        Args:
            attr_name (str): The name of the attribute to set.
            value: The value to assign to the attribute.
        """
        if attr_name == 'attributes':
            super().__setattr__(attr_name, value)
        else:
            self.attributes[attr_name] = value

    def __str__(self):
        """
        String representation of the character's statistics.

        Returns:
            str: A string listing the attributes and their values.
        """
        attrs = ', '.join(f"{key}: {value}" for key, value in self.attributes.items())
        return f"CharacterStats({attrs})"
