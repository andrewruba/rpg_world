# rpg_world
A Python library that can simulate RPG battles

# Tentative project structure
```
rpg_world/
│
├── src/                                # Source code directory
│   └── rpg_world/                      # Core package folder (inside src)
│       ├── __init__.py                 # Package initialization
│       │
│       ├── character/                  # Character-related logic
│       │   ├── __init__.py
│       │   ├── base_character.py       # Base class for characters
│       │   ├── mage.py                 # Mage class with spellcasting abilities
│       │   └── character_stats.py      # Character statistics (health, mana, etc.)
│       │
│       ├── ability/                    # Ability/spell system
│       │   ├── __init__.py
│       │   ├── base_ability.py         # Base ability class
│       │   └── spell.py                # Spell class with spell attributes and effects
│       │
│       ├── combat/                     # Combat system
│       │   ├── __init__.py
│       │   └── effect_calculation.py   # Calculates effects of spells on targets
│       │
│       ├── spellbook/                  # Spellbook system for different themes
│       │   ├── __init__.py
│       │   ├── spellbook.py            # Base spellbook class
│       │   ├── classic_spellbook.py    # Classic medieval magic spells
│       │   ├── egyptian_spellbook.py   # Egyptian magic spells
│       │   └── alien_spellbook.py      # Alien magic spells
│       │
│       ├── ai/                         # AI logic and training system
│       │   ├── __init__.py
│       │   ├── ai_training.py          # Core class for training AI characters
│       │   ├── rl_agent.py             # Reinforcement learning agents for AI
│       │   ├── behavior_tree.py        # Optional: Behavior trees for AI decisions
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
│       ├── game/                       # Game logic and execution
│       │   ├── __init__.py
│       │   └── game.py                 # Main gameplay loop logic
│       │
│       ├── config.py                   # Configuration for game settings
│
├── tests/                              # Unit and integration tests
│   ├── test_character.py
│   ├── test_spell.py
│   ├── test_effect_calculation.py
│   ├── test_ai.py
│   ├── test_balance.py
│   └── test_spellbook.py
│
├── examples/                           # Example scripts
│   ├── example_character.py            # Examples of character creation and interaction
│   ├── example_game.py                 # Example of the game loop and gameplay mechanics
│   ├── example_spell.py                # Examples of spell creation and casting
│   └── typecast_demo.py                # Demonstration of the TypeCast game mechanics
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

Alternatively, run the build and install bash script
```
./scripts/build_install.sh
```
