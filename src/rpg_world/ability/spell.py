from .base_ability import BaseAbility

class Spell(BaseAbility):
    def __init__(self, name, damage, spell_range, casting_time, spell_speed, cooldown, mana_cost):
        """
        Initialize a spell with specific attributes.

        Args:
            name (str): The name of the spell.
            damage (float): The amount of damage the spell deals.
            spell_range (float): The effective range of the spell in meters.
            casting_time (float): The time in seconds it takes to cast the spell.
            spell_speed (float): The speed of the spell in meters per second.
            cooldown (float): Time in seconds between spell uses.
            mana_cost (float): The mana cost to cast the spell.
        """
        # Create a dictionary of attributes with real values
        attributes = {
            'damage': damage,
            'range': spell_range,  # In meters (or any real unit of measure)
            'casting_time': casting_time,  # In seconds
            'spell_speed': spell_speed,  # In meters per second
            'cooldown': cooldown,  # In seconds
            'mana_cost': mana_cost  # Mana cost to cast the spell
        }

        # Initialize the BaseAbility with the name and attributes
        super().__init__(name, attributes)

    def cast(self, caster, target, current_time):
        """
        Cast the spell on the target. Checks only for cooldown and mana cost is assumed to be checked by the caster.

        Args:
            caster: The entity casting the spell.
            target: The entity receiving the spell.
            current_time (float): The current time for checking the cooldown.
        """
        if self.is_on_cooldown(current_time):
            print(f"{self.name} is on cooldown and cannot be cast yet.")
            return

        # Simulate spell casting process
        print(f"{caster.name} casts {self.name} on {target.name}, dealing {self.get_attribute('damage')} damage!")
        print(f"{self.name} takes {self.get_attribute('casting_time')} seconds to cast.")
        print(f"{self.name} travels at {self.get_attribute('spell_speed')} meters per second.")
        
        # Update the last cast time to the current time
        self.last_cast_time = current_time

    def __str__(self):
        return super().__str__()
