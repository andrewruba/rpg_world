# rpg_world

**rpg_world** is a Python library designed to simplify the creation of RPGs by providing a robust backend system for managing RPG **game state**. Whether you're developing classic turn-based RPGs or real-time combat systems, **rpg_world** offers a comprehensive framework to manage the intricacies of character progression, combat mechanics, inventory systems, quests, dialogues, and more. By focusing on the backend game logic, it significantly reduces the complexity of developing RPGs, making them more accessible to developers of all levels.

> **Note:** While **rpg_world** is specialized in managing the backend game logic and state, it does not include functionalities traditionally provided by full-fledged game engines, such as graphics rendering, audio processing, or real-time visual effects. This design allows **rpg_world** to be seamlessly integrated into existing projects or serve as a backend component for custom game engines, giving developers the freedom to pair it with their preferred tools for visuals and other front-end features.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Character Management**: Create and manage diverse characters with customizable stats and abilities.
- **Ability and Spell System**: Define a wide range of abilities and spells with unique effects and cooldowns.
- **Combat Systems**: Implement both turn-based and real-time combat mechanics.
- **Item System**: Manage consumables, equipment, and inventory with ease.
- **World and Exploration**: Design expansive game worlds with interconnected locations and dynamic events.
- **Quest System**: Create engaging quests with multiple objectives and rewarding outcomes.
- **Saving and Loading**: Save and load game states seamlessly.

## Planned Features - not implemented yet!
- **Dialogue System**: Facilitate interactive dialogues with NPCs, including branching conversations.
- **Skill Trees**: Develop comprehensive skill trees for character progression and ability enhancements.
- **Leveling and Experience**: Implement experience gain and leveling mechanics to advance characters.
- **Cutscene Management**: Create immersive cutscenes to advance the story.
- **Party Management**: Manage and switch between party members efficiently.
- **Environment Effects**: Introduce dynamic weather and time-of-day systems to enhance gameplay.
- **Crafting System**: Allow players to gather materials and craft items, weapons, and potions.
- **Achievements System**: Track and reward player achievements and milestones.
- **AI and Balancing**: Develop intelligent AI opponents and ensure balanced gameplay through metrics.

## Project Structure

The following directory layout outlines the current structure of the **rpg_world** library. This organization ensures scalability, maintainability, and ease of navigation for developers.

```plaintext
rpg_world/
│
├── src/                                # Source code directory
│   └── rpg_world/                      # Core package folder (inside src)
│       ├── __init__.py                 # Package initialization
│       │
│       ├── ability/                    # Ability/spell system
│       │   ├── __init__.py
│       │   ├── ability.py              # Base ability class
│       │   └── spell.py                # Spell class with spell attributes and effects
│       │
│       ├── character/                  # Character-related logic
│       │   ├── __init__.py
│       │   ├── character.py            # Base class for characters
│       │   └── mage.py                 # Mage class with spellcasting abilities
│       │
│       ├── combat/                     # Combat system
│       │   ├── __init__.py
│       │   ├── battle_manager.py       # Manages battles, turn order, and actions
│       │   └── turn_order.py           # Turn-based combat system
│       │
│       ├── effect/                     # Effects of abilities system
│       │   ├── __init__.py
│       │   ├── effect.py               # Calculates effects of abilities on targets
│       │   └── spell_effect.py         # Calculates effects of spells on targets
│       │
│       ├── event/                      # Generic event system
│       │   ├── __init__.py
│       │   ├── event_manager.py        # Manages events across the game
│       │   ├── event.py                # Defines different types of events
│       │   └── trigger.py              # Manages the conditions in the game state that cause events
│       │
│       ├── formula/                    # Formulas for making calculations
│       │   ├── __init__.py
│       │   ├── formula.py              # Base formula class
│       │   ├── effect_formula.py       # Example formulas for calculating effects
│       │   └── turn_order_formula.py   # Example formulas for calculating turn order
│       │
│       ├── item/                       # Item system (weapons, potions, etc.)
│       │   ├── __init__.py
│       │   ├── item.py                 # Base item class
│       │   ├── consumable.py           # Consumable items (e.g., potions)
│       │   ├── equipment.py            # Equipment items (weapons, armor)
│       │   └── inventory.py            # Manages inventory of items for characters/party
│       │
│       ├── place/                      # World and exploration logic
│       │   ├── __init__.py
│       │   ├── place.py                # Base place class
│       │   ├── world.py                # Represents the game world, locations, and navigation
│       │   ├── location.py             # Represents locations in the game world
│       │   └── position.py             # Represents position in a location
│       │
│       ├── quest/                      # Quest and objective system
│       │   ├── __init__.py
│       │   ├── quest.py                # Represents quests with objectives and rewards
│       │   ├── quest_objective.py      # Extends event, individual objectives within a quest
│       │   └── quest_manager.py        # Manages active quests and progression
│       │
│       ├── save_load/
│       │   ├── __init__.py
│       │   ├── save_manager.py         # Manages saving game data to a file
│       │   └── load_manager.py         # Manages loading game data from a file
│       │
│       ├── stats/                      # Generic stat system
│       │   ├── __init__.py
│       │   ├── stats.py                # Base stats class
│       │   └── character_stats.py      # Character statistics (health, mana, etc.)
│       │
│       ├── utils/                      # Helper functions and utilities
│       │   ├── __init__.py
│       │   └── logger.py               # Logging and debug utilities
│       │
│       └── game/                       # Game logic and execution
│           ├── __init__.py
│           ├── game.py                 # Core game loop logic
│           └── game_state.py           # Representation of the game state 
│
├── tests/                              # Unit and integration tests for all classes
│
├── scripts/                            # Folder for utility scripts
│   ├── build_and_install.sh            # Script for building and installing the package
│   ├── lint_and_style.sh               # Script for running code checks and linter
│   ├── test.sh                         # Script for running unit tests
│   └── update_reqs.sh                  # Script for updating the requirements.txt file
│
├── .github/                            # CI/CD pipeline
│
├── .gitignore                          # Specifies files and directories to ignore in Git
├── environment.yml                     # Conda environment configuration
├── requirements.txt                    # Python package dependencies
├── setup.py                            # Setup file for package installation
├── pytest.ini                          # Pytest config file
├── README.md                           # Readme with project overview
├── CONTRIBUTING.md                     # How to contribute
└── LICENSE                             # License for the package
```

## Installation

### Prerequisites
- **Python 3.7+**: Ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).
- **Conda**: For environment management using Conda, install [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
- **pip**: For environment management using `venv`, ensure `pip` is installed. It typically comes with Python 3.4+.


### Installation Methods

You can install **rpg_world** using one of the following methods:

1. **Using Conda** (Building from source)
2. **Using `venv`** (Building from source)

---

#### Using Conda (Building from source)

1. **Clone the Repository**
    ```bash
    git clone https://github.com/andrewruba/rpg_world.git
    cd rpg_world
    ```

2. **Set Up the Conda Environment**
    ```bash
    conda env create -f environment.yml
    ```

3. **Activate the Conda Environment**
    ```bash
    conda activate rpg_world_env
    ```

4. **Build the Package**
    ```bash
    python setup.py sdist bdist_wheel
    ```

5. **Install the Package**
    ```bash
    pip install dist/rpg_world-*.whl --force-reinstall
    ```

---

#### Using `venv` (Building from source)

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/rpg_world.git
    cd rpg_world
    ```

2. **Set Up the Virtual Environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**
    - **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```
    - **On Windows**:
        ```bash
        venv\Scripts\activate
        ```

4. **Install the Required Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5. **Build the Package**
    ```bash
    python setup.py sdist bdist_wheel
    ```

6. **Install the Package**
    ```bash
    pip install dist/rpg_world-*.whl --force-reinstall
    ```

## Quick Start

The following example demonstrates how to create a `Mage`, define a `Spell` with multiple `Effect`s, and cast that spell on a `Goblin`.

```python
from rpg_world import (
    Character,
    Mage,
    CharacterStats,
    Spell,
    SpellEffect,
    SimpleChangeFormula
)

# Create a Mage named Merlin
merlin = Mage(name="Merlin", health=100, mana=100, focus=90, armor=10)

# Define a spell called 'Mystic Blast' with multiple effects
mystic_blast = Spell(
    name="Mystic Blast",
    mana_cost=25.0,
    cooldown=1.0,   # second
    effects=[
        SpellEffect(attribute='health', formula=SimpleChangeFormula(-25)),  # Damage health
        SpellEffect(attribute='focus', formula=SimpleChangeFormula(-15))  # Reduce focus
    ]
)

# Merlin learns the 'Mystic Blast' spell
merlin.learn_spell(mystic_blast)

# Create a Goblin with specific stats
goblin_stats = CharacterStats(health=80, focus=40, armor=10)
goblin = Character(name="Goblin", stats=goblin_stats)

# Print initial stats for both characters
print(f"Before casting spell:")
print(f"Merlin: {merlin.stats}")
print(f"Goblin: {goblin.stats}")

# Merlin casts 'Mystic Blast' on the Goblin
current_time = 0.0  # This could be your game loop's current time, used for cooldowns
merlin.cast_spell("Mystic Blast", goblin, current_time)

# Print the updated stats after the spell is cast
print(f"\nAfter casting 'Mystic Blast':")
print(f"Merlin: {merlin.stats}")
print(f"Goblin: {goblin.stats}")
```

## Usage

See unit tests in the `tests/` directory for more complete class usage examples for now.

## Testing

Unit and integration tests are located in the tests/ directory. These tests ensure that each component of the rpg_world library functions correctly.

### Running Tests

You can run the tests using the provided scripts or with pytest directly.

```bash
pytest
```

## Contributing

See CONTRIBUTING.md

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.

## Contact

For any questions, suggestions, or support, feel free to reach out.

GitHub Issues: [rpg_world Issues](https://github.com/andrewruba/rpg_world/issues)

GitHub Discussions: [rpg_world Discussions](https://github.com/andrewruba/rpg_world/discussions)
