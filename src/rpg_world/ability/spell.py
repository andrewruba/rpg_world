from .ability import Ability
import logging

class Spell(Ability):
    def __init__(self, name, mana_cost, cooldown, effects):
        """
        Initialize a spell with specific attributes.

        Args:
            name (str): The name of the spell.
            mana_cost (float): The mana cost required to cast the spell.
            cooldown (float): Time in seconds between spell uses.
            effects (list): A list of effects, where each effect is an instance of an Effect object.
        """
        # Create a dictionary of attributes with real values
        attributes = {
            'mana_cost': mana_cost,
            'cooldown': cooldown
        }

        # Initialize the Ability with the name and attributes
        super().__init__(
            name=name,
            attributes=attributes,
            effects=effects
        )

    def cast(self, caster, target, current_time):
        """
        Cast the spell on the target. Checks if the spell is on cooldown before casting.

        Args:
            caster (object): The entity casting the spell (e.g., a player or character).
            target (object): The entity receiving the spell (e.g., an enemy or target).
            current_time (float): The current time (timestamp) used to check for spell cooldowns.

        Returns:
            bool: True if the spell was successfully cast, False otherwise.
        """
        if self.is_on_cooldown(current_time):
            self.logger.warning(f"{self.name} is on cooldown and cannot be cast yet.")
            return False

        # Log the spell casting event
        self.logger.info(f"{caster.name} casts {self.name} on {target.name}!")

        # Update the last cast time to the current time
        self.last_cast_time = current_time

        # Perform effect calculation and apply effects
        for effect in self.effects:
            self.logger.debug(f"Applying effect: {effect}")
            effect.apply(
                caster=caster,
                target=target,
                ability=self
            )
        
        self.logger.info(f"Spell {self.name} cast successfully.")
        return True
