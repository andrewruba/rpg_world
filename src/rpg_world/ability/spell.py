from .ability import Ability
import logging

class Spell(Ability):
    def __init__(self, name, mana_cost, cooldown, effects):
        """
        Initialize a spell with specific attributes.

        Args:
            name (str): The name of the spell.
            mana_cost (float): The mana cost to cast the spell.
            cooldown (float): Time in seconds between spell uses.
            effects (list): A list of effects, each effect is a Effect object.
        """
        # Create a dictionary of attributes with real values
        attributes = {
            'mana_cost': mana_cost,
            'cooldown': cooldown,
            'effects': effects or [],
            # Add any other attributes if necessary
        }

        # Initialize the Ability with the name and attributes
        super().__init__(name, attributes)

    def cast(self, caster, target, current_time):
        """
        Cast the spell on the target. Checks only for cooldown.

        Args:
            caster: The entity casting the spell.
            target: The entity receiving the spell.
            current_time (float): The current time for checking the cooldown.
        """
        if self.is_on_cooldown(current_time):
            self.logger.warning(f"{self.name} is on cooldown and cannot be cast yet.")
            return False

        # Log spell casting
        self.logger.info(f"{caster.name} casts {self.name} on {target.name}!")

        # Update the last cast time to the current time
        self.last_cast_time = current_time

        # Perform effect calculation and apply effects
        for effect in self.effects:
            self.logger.debug(f"Applying effect: {effect}")
            effect.apply(
                caster=caster,
                target=target,
                kwargs = {
                    'ability': self
                }
            )
        
        self.logger.info(f"Spell {self.name} cast successfully.")
        return True
