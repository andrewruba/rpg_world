from rpg_world import Spell
from rpg_world import BaseCharacter, CharacterStats,Mage
import time

# Create a spell where the health damage depends on the target's focus
multi_effect_spell = Spell(
    name="Mystic Blast",
    mana_cost=25.0,
    cooldown=5.0,
    effects=[
        {
            'attribute': 'health',
            'formula': '-(50 + (target_stats.get("focus") * 0.5)) * (1 - (target_stats.get("armor") / 100.0))'
        },
        {
            'attribute': 'focus',
            'formula': '-15'
        },
        {
            'attribute': 'armor',
            'formula': '+5'  # Increases target's armor by 5
        }
    ]
)

# Create a Mage character
merlin = Mage(name="Merlin", health=100, mana=100, focus=90, armor=10, spells=[multi_effect_spell])
print(merlin)

# Create a target character (e.g., a Goblin)
goblin_stats = CharacterStats(health=80, focus=40, armor=10)
goblin = BaseCharacter(name="Goblin", stats=goblin_stats)

# Merlin casts Fireball on the Goblin
current_time = time.time()
merlin.cast_spell("Mystic Blast", goblin, current_time)

# Print the Goblin's updated stats
print(goblin)
