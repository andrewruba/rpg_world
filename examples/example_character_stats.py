from rpg_world import BaseCharacter
from rpg_world import CharacterStats
from rpg_world import BaseEffect
from rpg_world import BaseAbility
from rpg_world import simple_change

# Create character stats
stats = CharacterStats(health=120, mana=80, focus=100, armor=10)

# Create a character
character = BaseCharacter(name="Arcanist", stats=stats)

# Display character stats
print(character)

class PlaceholderAbility(BaseAbility):
    def __init__(self):
        super().__init__("", {})

    def cast(self, caster, target, current_time):
        """
        Abstract method for casting the ability. Must be implemented by subclasses.
        
        Args:
            caster: The entity casting the ability.
            target: The entity receiving the ability.
            current_time (float): The current time to check cooldown.
        """
        pass

# Modify character attributes
# Apply a damage effect to health
health_effect = BaseEffect(attribute='health', formula=simple_change(-30))
health_effect.apply(character)

# Apply a mana reduction effect
mana_effect = BaseEffect(attribute='mana', formula=simple_change(-20))
mana_effect.apply(character)

# Apply a focus increase effect
focus_effect = BaseEffect(attribute='focus', formula=simple_change(10))
focus_effect.apply(character)

# Check if the character is alive
if character.is_alive():
    print(f"{character.name} is still alive.")
else:
    print(f"{character.name} has perished.")

# Display updated character stats
print(character)
