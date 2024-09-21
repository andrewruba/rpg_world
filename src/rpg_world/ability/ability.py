from abc import ABC, abstractmethod
from ..utils.logger import Logger

class Ability(ABC):
    def __init__(self, name, attributes, effects=None):
        """
        Initialize the base Ability class with dynamic attributes.

        Args:
            name (str): The name of the ability.
            attributes (dict): A dictionary of ability attributes (e.g., {'damage': 50, 'range': 'long-range'}).
            effects (list, optional): A list of effects (instances of Effect) that the ability applies. Defaults to None.
        """
        self.name = name
        self.attributes = attributes
        self.effects = effects or []
        self.last_cast_time = None  # Track the last time the ability was cast

        # Ensure cooldown is an attribute, set to 0 if not specified
        if 'cooldown' not in self.attributes:
            self.attributes['cooldown'] = 0

        # Initialize logger for this ability
        self.logger = Logger(f"Ability-{self.name}")
        self.logger.info(f"Ability '{self.name}' initialized with attributes: {self.attributes}")

    def is_on_cooldown(self, current_time):
        """
        Check if the ability is currently on cooldown.

        Args:
            current_time (float): The current time (in seconds as a timestamp).

        Returns:
            bool: True if the ability is on cooldown, False otherwise.
        """
        if self.last_cast_time and self.cooldown:
            remaining_time = self.cooldown - (current_time - self.last_cast_time)
            if remaining_time > 0:
                self.logger.info(f"Ability '{self.name}' is on cooldown for another {remaining_time:.2f} seconds.")
                return True
        return False

    @abstractmethod
    def cast(self, caster, target, current_time):
        """
        Abstract method for casting the ability. Must be implemented by subclasses.

        Args:
            caster (object): The entity casting the ability (e.g., a character or player).
            target (object): The entity receiving the ability (e.g., a target or enemy).
            current_time (float): The current time (timestamp) used to check for ability cooldowns.

        Returns:
            bool: True if the ability was successfully cast, False otherwise.
        """
        pass

    def __getattr__(self, attr_name):
        """
        Dynamically return attributes from the ability's attributes dictionary if they exist.

        Args:
            attr_name (str): The name of the attribute to retrieve.

        Returns:
            Any: The value of the attribute if it exists.

        Raises:
            AttributeError: If the attribute does not exist in the attributes dictionary.
        """
        if attr_name in self.attributes:
            return self.attributes[attr_name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr_name}'")

    def __setattr__(self, attr_name, value):
        """
        Dynamically set attributes in the attributes dictionary if they exist.

        Args:
            attr_name (str): The name of the attribute to set.
            value (Any): The value to set for the attribute.
        """
        if attr_name in ['name', 'attributes', 'effects', 'last_cast_time', 'logger']:
            super().__setattr__(attr_name, value)
        else:
            self.attributes[attr_name] = value
            self.logger.debug(f"Attribute '{attr_name}' of ability '{self.name}' set to {value}")

    def __str__(self):
        """
        Returns a string representation of the ability, including its name and attributes.

        Returns:
            str: A string describing the ability.
        """
        attrs = ', '.join(f"{key}: {value}" for key, value in self.attributes.items())
        return f"Ability: {self.name}, Attributes: {attrs}"
