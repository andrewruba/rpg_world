from rpg_world.character.base_character import BaseCharacter
from rpg_world.character.character_stats import CharacterStats

# Create character stats
stats = CharacterStats(health=120, mana=80, focus=100, armor=10)

# Create a character
character = BaseCharacter(name="Arcanist", stats=stats)

# Display character stats
print(character)

# Modify character attributes
character.process_effect({'attribute': 'health', 'amount': -30})
character.process_effect({'attribute': 'mana', 'amount': -20})
character.process_effect({'attribute': 'focus', 'amount': 10})

# Check if the character is alive
if character.is_alive():
    print(f"{character.name} is still alive.")
else:
    print(f"{character.name} has perished.")

# Display updated character stats
print(character)
