from rpg_world import Spell
from rpg_world import BaseCharacter, Mage

# Create a spell that reduces health and focus, and increases armor temporarily
multi_effect_spell = Spell(
    name="Mystic Blast",
    mana_cost=25.0,
    cooldown=5.0,
    effects=[
        {
            'attribute': 'health',
            'formula': '-50 * (1 - (target_attributes.get("armor", 0) / 100.0))'
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

# Assuming BaseCharacter and Mage are defined as before
caster = Mage(name="Merlin", health=100.0, mana=100.0, focus=90.0, armor=10.0)
target = BaseCharacter(name="Goblin", attributes={'health': 80.0, 'armor': 20.0, 'focus': 50.0})

# Caster learns the spell
caster.learn_spell(multi_effect_spell)

# Caster casts the spell on the target
current_time = time.time()
caster.cast_spell("Mystic Blast", target, current_time)

