from rpg_world import Spell
from rpg_world import BaseCharacter, CharacterStats,Mage
from rpg_world import SpellEffect
from rpg_world import simple_change, multi_effect_target_example, multi_effect_recipient_example
import time

# Create a spell where the health damage depends on the target's focus
multi_effect_spell = Spell(
    name="Mystic Blast",
    mana_cost=25.0,
    cooldown=5.0,
    effects=[
        SpellEffect(attribute='health', formula=multi_effect_recipient_example, recipient='caster'),
        SpellEffect(attribute='health', formula=multi_effect_target_example),
        SpellEffect(attribute='focus', formula=simple_change(-15)),
        SpellEffect(attribute='armor', formula=simple_change(5))
    ]
)

# Create a Mage character
merlin = Mage(name="Merlin", health=100, mana=100, focus=90, armor=10, spells=[multi_effect_spell])
print(merlin)

# Create a target character (e.g., a Goblin)
goblin_stats = CharacterStats(health=80, focus=40, armor=10)
goblin = BaseCharacter(name="Goblin", stats=goblin_stats)
print(goblin)

# Merlin casts Mystic Blast on the Goblin
current_time = time.time()
merlin.cast_spell("Mystic Blast", goblin, current_time)

# Print Merlin's updated stats
print(merlin)

# Print the Goblin's updated stats
print(goblin)
