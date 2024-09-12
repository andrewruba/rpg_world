# rpg_world
A Python library that can simulate RPG battles

# Tentative project structure
```
rpg_world/
│
├── src/                                # Source code directory
│   └── rpg_world/                  # Core package folder (inside src)
│       ├── __init__.py                 # Package initialization
│       ├── character/                  # Character-related logic
│       │   ├── __init__.py
│       │   ├── base_character.py       # Base class for characters
│       │   ├── player_character.py     # Player character class, extending base
│       │   ├── npc_character.py        # Non-player character (NPC) class
│       │   └── character_stats.py      # Character statistics (HP, strength, etc.)
│       │
│       ├── abilities/                  # Abilities/spells system
│       │   ├── __init__.py
│       │   ├── base_ability.py         # Base ability class
│       │   ├── spells.py               # Spell classes (fireball, shield, etc.)
│       │   └── effects.py              # Effects from abilities (buffs, debuffs, etc.)
│       │
│       ├── items/                      # Item system (weapons, potions, etc.)
│       │   ├── __init__.py
│       │   ├── base_item.py            # Base item class
│       │   ├── weapon.py               # Weapon class
│       │   └── consumable.py           # Consumable item class (healing potions, etc.)
│       │
│       ├── combat/                     # Combat system and mechanics
│       │   ├── __init__.py
│       │   ├── combat_system.py        # Core combat mechanics (turns, damage, etc.)
│       │   ├── battle.py               # Battle scenarios (1v1, party vs enemy, etc.)
│       │   ├── turn_order.py           # Turn order system
│       │   └── damage_calculation.py   # Damage formulas and calculations
│       │
│       ├── balance/                    # Balancing utilities
│       │   ├── __init__.py
│       │   ├── ai_balancing.py         # AI vs AI simulations for balancing
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
│   └── rpg_world_example.py       # Example RPG simulation using various components
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

# Build

Activate the conda env:
```
conda activate rpg_world_env
```

Build the package
```
python setup.py sdist bdist_wheel
```
