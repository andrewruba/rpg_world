from abc import ABC, abstractmethod
from ..utils.logger import Logger

class Ability(ABC):
    def __init__(self, name, attributes, effects = None):
        """
        Initialize the base ability class with dynamic attributes.

        Args:
            name (str): Name of the ability.
            attributes (dict): A dictionary of ability attributes (e.g., {'damage': 50, 'range': 'long-range'}).
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
            current_time (float): The current time (timestamp).
        
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
            caster: The entity casting the ability.
            target: The entity receiving the ability.
            current_time (float): The current time to check cooldown.
        """
        pass

    def __getattr__(self, attr_name):
        """
        Override __getattr__ to dynamically return attributes from the ability's attributes dictionary if they exist.

        Args:
            attr_name (str): The name of the attribute to retrieve.

        Returns:
            The value of the attribute if it exists in attributes.
        """
        if attr_name in self.attributes:
            return self.attributes[attr_name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr_name}'")

    def __setattr__(self, attr_name, value):
        """
        Override __setattr__ to dynamically set attributes in the attributes dictionary if they exist.
        """
        if attr_name in ['name', 'attributes', 'effects', 'last_cast_time', 'logger']:
            super().__setattr__(attr_name, value)
        else:
            self.attributes[attr_name] = value
            self.logger.debug(f"Attribute '{attr_name}' of ability '{self.name}' set to {value}")

    def __str__(self):
        attrs = ', '.join(f"{key}: {value}" for key, value in self.attributes.items())
        return f"Ability: {self.name}, Attributes: {attrs}"
