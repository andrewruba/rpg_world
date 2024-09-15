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
│       ├── effect/                     # Effects of abilties system
│       │   ├── __init__.py
│       │   ├── base_effect.py          # Calculates effects of abilities on targets
│       │   ├── spell_effect.py         # Calculates effects of spells on targets
│       │   └── effect_formulas.py      # Formulas for calculating effects
│       │
│       ├── combat/                     # Combat system
│       │   ├── __init__.py
│       │   ├── battle_manager.py       # Manages battles, turn order, and actions
│       │   ├── turn_order.py           # Turn-based combat system
│       │   └── action_queue.py         # Action queue for real-time combat system
│       │
│       ├── item/                       # Item system (weapons, potions, etc.)
│       │   ├── __init__.py
│       │   ├── item.py                 # Base item class
│       │   ├── consumable.py           # Consumable items (e.g., potions)
│       │   ├── equipment.py            # Equipment items (weapons, armor)
│       │   └── inventory.py            # Manages inventory of items for characters/party
│       │
│       ├── world/                      # World and exploration logic
│       │   ├── __init__.py
│       │   ├── world.py                # Represents the game world, locations, and navigation
│       │   ├── location.py             # Represents locations in the game world
│       │   └── event.py                # Represents game events and triggers
│       │
│       ├── quest/                      # Quest and objective system
│       │   ├── __init__.py
│       │   ├── quest.py                # Represents quests with objectives and rewards
│       │   ├── quest_objective.py      # Individual objectives within a quest
│       │   └── quest_manager.py        # Manages active quests and progression
│       │
│       ├── dialogue/
│       │   ├── __init__.py
│       │   ├── dialogue_manager.py       # Manages dialogue sequences and branching dialogue options
│       │   ├── dialogue_node.py          # Represents individual lines of dialogue or choices
│       │   └── dialogue_script.py        # Contains dialogue scripts for different NPCs or events
│       │
│       ├── skill_tree/
│       │   ├── __init__.py
│       │   ├── skill_node.py             # Represents an individual skill in the tree
│       │   ├── skill_tree.py             # Manages the entire skill tree, unlocks, and dependencies
│       │   └── skill_manager.py          # Handles the allocation of skill points and progression
│       │
│       ├── leveling/
│       │   ├── __init__.py
│       │   ├── experience_manager.py     # Manages experience gains and leveling up
│       │   └── level_curve.py            # Determines XP thresholds for leveling up
│       │
│       ├── save_load/
│       │   ├── __init__.py
│       │   ├── save_manager.py           # Manages saving game data to a file
│       │   └── load_manager.py           # Manages loading game data from a file
│       │
│       ├── cutscene/
│       │   ├── __init__.py
│       │   ├── cutscene_manager.py       # Manages the logic and timing for cutscenes
│       │   ├── cutscene_sequence.py      # Defines sequences of events for a cutscene
│       │   └── cutscene_event.py         # Individual events (e.g., dialogue, animations) within a cutscene
│       │
│       ├── party/
│       │   ├── __init__.py
│       │   ├── party_manager.py          # Manages the player's party, switching characters, etc.
│       │   └── character_switch.py       # Logic for switching between active characters
│       │
│       ├── environment/
│       │   ├── __init__.py
│       │   ├── weather.py                # Manages weather effects (e.g., rain, snow, storms)
│       │   └── time_of_day.py            # Manages time-of-day changes (e.g., day-night cycles)
│       │
│       ├── crafting/
│       │   ├── __init__.py
│       │   ├── crafting_manager.py       # Manages crafting recipes and processes
│       │   └── recipe.py                 # Defines crafting recipes and required materials
│       │
│       ├── achievements/
│       │   ├── __init__.py
│       │   ├── achievement.py            # Defines individual achievements
│       │   └── achievement_manager.py    # Tracks and manages unlocked achievements
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
│       │   └── game.py                 # Core game loop logic
│       │
│       ├── config.py                   # Configuration for game settings
│       │
├── tests/                              # Unit and integration tests
│   ├── test_base_character.py
│   ├── test_spell_effect.py
│   ├── test_character_stats.py
│   ├── test_logger.py
│   └── test_game.py
│
├── examples/                           # Example scripts
│   ├── example_character.py            # Examples of character creation and interaction
│   ├── example_character_stats.py      # Examples of character stat creation
│   ├── example_game.py                 # Example of the game loop and gameplay mechanics
│   └── example_spell.py                # Examples of spell creation and casting
│
├── docs/                               # Documentation
│   ├── index.md                        # Main documentation index
│   ├── usage.md                        # Usage instructions
│   └── api_reference.md                # API reference for developers
│
├── scripts/                            # Folder for utility scripts
│   ├── build_install.sh                # Script for building and installing the package
│   ├── run_tests.sh                    # Script for running unit tests
│   └── update_requirements.sh          # Script for updating the requirements.txt file
│
├── .gitignore                          # Specifies files and directories to ignore in Git
├── environment.yml                     # Conda environment configuration
├── requirements.txt                    # Python package dependencies
├── setup.py                            # Setup file for package installation
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
