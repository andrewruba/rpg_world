from rpg_world.character.base_character import BaseCharacter
from rpg_world.abilities.base_ability import BaseAbility

class Spell(BaseAbility):
    def __init__(self, name, attributes):
        """
        Initialize the spell with dynamic attributes.
        
        Args:
            name (str): Name of the spell.
            attributes (dict): A dictionary of spell attributes (e.g., {'damage': 50, 'range': 'long-range'}).
        """
        super().__init__(name, attributes)

    def cast(self, caster, target, current_time):
        """
        Cast the spell on the target. Checks for cooldown and applies effects.

        Args:
            caster: The entity casting the spell.
            target: The entity receiving the spell's effects.
            current_time (float): The current time to check cooldown.
        """
        if self.is_on_cooldown(current_time):
            print(f"{self.name} is on cooldown!")
            return

        # Retrieve dynamic attributes
        damage = self.get_attribute('damage')
        range_type = self.get_attribute('range')
        special_effects = self.get_attribute('special_effects')

        print(f"{caster.name} casts {self.name} on {target.name} dealing {damage} damage.")
        target.take_damage(damage)

        # Apply special effects (if any)
        self.apply_special_effects(target)

        # Update last cast time
        self.last_cast_time = current_time


# Example usage of BaseCharacter and Spell class
if __name__ == "__main__":
    # Create a spell with generic attributes
    fireball = Spell(
        name="Fireball",
        attributes={
            'damage': 50,
            'range': 'long-range',
            'casting_time': 'medium',
            'spell_speed': 'fast',
            'cooldown': 5,
            'special_effects': {"burn": 10}  # Burn effect dealing 10 additional damage over time
        }
    )

    # Create characters using BaseCharacter
    caster_attributes = {
        'health': 100,
        'strength': 20,
        'mana': 50
    }
    target_attributes = {
        'health': 80,
        'strength': 15
    }

    caster = BaseCharacter("Wizard", caster_attributes)
    target = BaseCharacter("Goblin", target_attributes)

    # Cast the spell in a simulated real-time environment
    import time
    current_time = time.time()
    fireball.cast(caster, target, current_time)
    time.sleep(6)  # Wait for cooldown to expire
    fireball.cast(caster, target, time.time())
