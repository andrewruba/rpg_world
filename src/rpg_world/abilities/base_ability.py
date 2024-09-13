from abc import ABC, abstractmethod

class BaseAbility(ABC):
    def __init__(self, name, attributes):
        """
        Initialize the base ability class with dynamic attributes.

        Args:
            name (str): Name of the ability.
            attributes (dict): A dictionary of ability attributes (e.g., {'damage': 50, 'range': 'long-range'}).
        """
        self.name = name
        self.attributes = attributes
        self.last_cast_time = None  # Track the last time the ability was cast

    def get_attribute(self, attr_name):
        """
        Retrieve the value of a specific attribute.
        
        Args:
            attr_name (str): The name of the attribute to retrieve.
        
        Returns:
            The value of the attribute or None if it doesn't exist.
        """
        return self.attributes.get(attr_name)

    def set_attribute(self, attr_name, value):
        """
        Set the value of a specific attribute.
        
        Args:
            attr_name (str): The name of the attribute to set.
            value: The value to assign to the attribute.
        """
        self.attributes[attr_name] = value

    def apply_special_effects(self, target):
        """
        Apply special effects (if any) to the target. This method can be called when a spell is cast.
        
        Args:
            target: The entity receiving the effects.
        """
        special_effects = self.get_attribute('special_effects')
        if special_effects:
            for effect, value in special_effects.items():
                print(f"{self.name} applies {effect} with value {value} to {target.name}")
                # You can implement logic to apply effects like burning, freezing, buffing, etc.

    def is_on_cooldown(self, current_time):
        """
        Check if the ability is currently on cooldown.
        
        Args:
            current_time (float): The current time (timestamp).
        
        Returns:
            bool: True if the ability is on cooldown, False otherwise.
        """
        cooldown = self.get_attribute('cooldown')
        if self.last_cast_time and cooldown:
            return (current_time - self.last_cast_time) < cooldown
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

    def __str__(self):
        attrs = ', '.join(f"{key}: {value}" for key, value in self.attributes.items())
        return f"Ability: {self.name}, Attributes: {attrs}"
