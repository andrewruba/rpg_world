from rpg_world import Character
from rpg_world import CharacterStats
from rpg_world import Effect
from rpg_world import SimpleChangeFormula

# Create character stats
stats = CharacterStats(health=120, mana=80, focus=100, armor=10)

# Create a character
character = Character(name="Arcanist", stats=stats)

# Display character stats
print(character)

# Modify character attributes
# Apply a damage effect to health
health_effect = Effect(attribute='health', formula=SimpleChangeFormula(-30))
health_effect.apply(character)

# Apply a mana reduction effect
mana_effect = Effect(attribute='mana', formula=SimpleChangeFormula(-20))
mana_effect.apply(character)

# Apply a focus increase effect
focus_effect = Effect(attribute='focus', formula=SimpleChangeFormula(10))
focus_effect.apply(character)

# Check if the character is alive
if character.is_alive():
    print(f"{character.name} is still alive.")
else:
    print(f"{character.name} has perished.")

# Display updated character stats
print(character)
