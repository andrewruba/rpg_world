# rpg_world
A Python library that can simulate RPG battles

# Tentative project structure
```
rpg_world/
│
├── src/                                # Source code directory
│   └── rpg_world/                      # Core package folder (inside src)
│       ├── __init__.py                 # Package initialization
│       ├── character/                  # Character-related logic
│       │   ├── __init__.py
│       │   ├── base_character.py       # Base class for characters
│       │   ├── player_character.py     # Player character class, extending base
│       │   ├── npc_character.py        # Non-player character (NPC) class with AI behavior
│       │   ├── character_stats.py      # Character statistics (health, strength, etc.)
│       │   └── status_effects.py       # Effects like stuns, freezes, buffs, debuffs
│       │
│       ├── abilities/                  # Abilities/spells system
│       │   ├── __init__.py
│       │   ├── base_ability.py         # Base ability class
│       │   └── spells.py               # Spell classes (fireball, shield, etc.)
│       │
│       ├── items/                      # Item system (weapons, potions, etc.)
│       │   ├── __init__.py
│       │   ├── base_item.py            # Base item class
│       │   ├── weapon.py               # Weapon class
│       │   ├── armor.py                # Armor class
│       │   └── consumable.py           # Consumable item class (healing potions, etc.)
│       │
│       ├── combat/                     # Real-time combat system
│       │   ├── __init__.py
│       │   ├── real_time_combat.py     # Core real-time combat mechanics (event-driven)
│       │   ├── action_queue.py         # Queue of actions to handle in real-time processing
│       │   ├── cooldown_manager.py     # Cooldowns for abilities and items
│       │   ├── damage_calculation.py   # Dynamic damage calculations
│       │   └── spell_casting.py        # Continuous input for casting spells in real time
│       │
│       ├── ai/                         # AI logic and training system
│       │   ├── __init__.py
│       │   ├── ai_training.py          # Core class for training AI characters
│       │   ├── rl_agent.py             # Reinforcement learning agents for real-time AI
│       │   ├── behavior_tree.py        # Optional: Behavior trees for AI decisions
│       │
│       ├── balance/                    # Balancing utilities (modified for real-time)
│       │   ├── __init__.py
│       │   ├── ai_balancing.py         # AI vs AI real-time simulations for balancing
│       │   └── metrics.py              # Metrics for tracking balance (win rates, etc.)
│       │
│       ├── utils/                      # Helper functions and utilities
│       │   ├── __init__.py
│       │   └── logger.py               # Logging and debug utilities
│       │
│       └── config.py                   # Configuration for RPG rules, settings, etc.
│
├── tests/                              # Unit and integration tests
│   ├── test_character.py
│   ├── test_combat_system.py
│   ├── test_spells.py
│   ├── test_balance.py
│   └── test_items.py
│
├── examples/                           # Example scripts
│   ├── basic_battle.py                 # Example of a simple battle setup
│   └── rpg_world_example.py            # Example RPG simulation using various components
│
├── docs/                               # Documentation
│   ├── index.md
│   ├── usage.md
│   └── api_reference.md
│
├── setup.py                            # Setup file for installation
├── README.md                           # Readme with project overview
└── LICENSE                             # License for the package
```

# Development

Activate the conda env:
```
conda activate rpg_world_env
```

Build the package
```
python setup.py sdist bdist_wheel
```

Install
```
pip install dist/rpg_world-*.whl --force-reinstall
```
