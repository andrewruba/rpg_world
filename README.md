# rpg_world

**rpg_world** is a Python library designed to simplify the creation of RPGs by providing a robust backend system for managing RPG **game state**. Whether you're developing classic turn-based RPGs or real-time combat systems, **rpg_world** offers a comprehensive framework to manage the intricacies of character progression, combat mechanics, inventory systems, quests, dialogues, and more. By focusing on the backend game logic, it significantly reduces the complexity of developing RPGs, making them more accessible to developers of all levels.

> **Note:** While **rpg_world** is specialized in managing the backend game logic and state, it does not include functionalities traditionally provided by full-fledged game engines, such as graphics rendering, audio processing, or real-time visual effects. This design allows **rpg_world** to be seamlessly integrated into existing projects or serve as a backend component for custom game engines, giving developers the freedom to pair it with their preferred tools for visuals and other front-end features.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Creating Characters](#creating-characters)
  - [Defining Abilities and Spells](#defining-abilities-and-spells)
  - [Managing Combat](#managing-combat)
  - [Handling Items and Inventory](#handling-items-and-inventory)
  - [World and Exploration](#world-and-exploration)
  - [Quests and Objectives](#quests-and-objectives)
  - [Saving and Loading](#saving-and-loading)
- [Examples](#examples)
- [Documentation](#documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Current Features

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

## Planned Project Structure

The following directory layout outlines the intended structure of the **rpg_world** library once all features have been fully implemented. This organization ensures scalability, maintainability, and ease of navigation for developers.

```plaintext
rpg_world/
│
├── src/                                # Source code directory
│   └── rpg_world/                      # Core package folder (inside src)
│       ├── __init__.py                 # Package initialization
│       │
│       ├── character/                  # Character-related logic
│       │   ├── __init__.py
│       │   ├── character.py       # Base class for characters
│       │   ├── mage.py                 # Mage class with spellcasting abilities
│       │   └── character_stats.py      # Character statistics (health, mana, etc.)
│       │
│       ├── ability/                    # Ability/spell system
│       │   ├── __init__.py
│       │   ├── ability.py         # Base ability class
│       │   └── spell.py                # Spell class with spell attributes and effects
│       │
│       ├── effect/                     # Effects of abilities system
│       │   ├── __init__.py
│       │   ├── effect.py          # Calculates effects of abilities on targets
│       │   ├── spell_effect.py         # Calculates effects of spells on targets
│       │   └── effect_formulas.py      # Formulas for calculating effects
│       │
│       ├── combat/                     # Combat system
│       │   ├── __init__.py
│       │   ├── battle_manager.py       # Manages battles, turn order, and actions
│       │   └── turn_order.py           # Turn-based combat system
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
│       │   └── position.py             # Represents position in a location
│       │
│       ├── event/                      # Generic event system
│       │   ├── __init__.py
│       │   ├── event_manager.py        # Manages events across the game
│       │   ├── event.py                # Defines different types of events
│       │   └── trigger.py              # Manages the conditions in the game state that cause events
│       │
│       ├── quest/                      # Quest and objective system
│       │   ├── __init__.py
│       │   ├── quest.py                # Represents quests with objectives and rewards
│       │   ├── quest_objective.py      # Extends event, individual objectives within a quest
│       │   └── quest_manager.py        # Manages active quests and progression
│       │
│       ├── dialogue/
│       │   ├── __init__.py
│       │   ├── dialogue_manager.py     # Manages dialogue sequences and branching dialogue options
│       │   ├── dialogue_node.py        # Represents individual lines of dialogue or choices
│       │   └── dialogue_script.py      # Contains dialogue scripts for different NPCs or events
│       │
│       ├── skill_tree/
│       │   ├── __init__.py
│       │   ├── skill_node.py           # Represents an individual skill in the tree
│       │   ├── skill_tree.py           # Manages the entire skill tree, unlocks, and dependencies
│       │   └── skill_manager.py        # Handles the allocation of skill points and progression
│       │
│       ├── leveling/
│       │   ├── __init__.py
│       │   ├── experience_manager.py   # Manages experience gains and leveling up
│       │   └── level_curve.py          # Determines XP thresholds for leveling up
│       │
│       ├── save_load/
│       │   ├── __init__.py
│       │   ├── save_manager.py         # Manages saving game data to a file
│       │   └── load_manager.py         # Manages loading game data from a file
│       │
│       ├── cutscene/
│       │   ├── __init__.py
│       │   ├── cutscene_manager.py     # Manages the logic and timing for cutscenes
│       │   ├── cutscene_sequence.py    # Defines sequences of events for a cutscene
│       │   └── cutscene_event.py       # Individual events (e.g., dialogue, animations) within a cutscene
│       │
│       ├── party/
│       │   ├── __init__.py
│       │   ├── party_manager.py        # Manages the player's party, switching characters, etc.
│       │   └── character_switch.py     # Logic for switching between active characters
│       │
│       ├── environment/
│       │   ├── __init__.py
│       │   ├── weather.py              # Manages weather effects (e.g., rain, snow, storms)
│       │   └── time_of_day.py          # Manages time-of-day changes (e.g., day-night cycles)
│       │
│       ├── crafting/
│       │   ├── __init__.py
│       │   ├── crafting_manager.py     # Manages crafting recipes and processes
│       │   └── recipe.py               # Defines crafting recipes and required materials
│       │
│       ├── achievements/
│       │   ├── __init__.py
│       │   ├── achievement.py          # Extends event, defines individual achievements
│       │   └── achievement_manager.py  # Tracks and manages unlocked achievements
│       │
│       ├── ai/                         # AI logic and training system
│       │   ├── __init__.py
│       │   ├── ai_training.py          # Core class for training AI characters
│       │   └── rl_agent.py             # Reinforcement learning agents for AI
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
│       └── game/                       # Game logic and execution
│           ├── __init__.py
│           ├── game.py                 # Core game loop logic
│           └── game_state.py           # Representation of the game state 
│
├── tests/                              # Unit and integration tests
│   ├── test_character.py
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

## Installation

### Prerequisites
- **Python 3.7+**: Ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).
- **Conda**: For environment management using Conda, install [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
- **pip**: For environment management using `venv`, ensure `pip` is installed. It typically comes with Python 3.4+.


### Installation Methods

You can install **rpg_world** using one of the following methods:

1. **Using pip** (Recommended)
2. **Using Conda** (Building from source)
3. **Using `venv`** (Building from source)

---

#### Using pip (Recommended)

You can install **rpg_world** directly from PyPI using `pip`.

```bash
pip install rpg_world
```

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

## Usage

### Creating Characters

Character: The foundational class for all characters.

Mage: A subclass of Character with spellcasting abilities.

```python
from rpg_world.character.character import Character
from rpg_world.character.mage import Mage
from rpg_world.character.character_stats import CharacterStats

# Create stats for a mage
mage_stats = CharacterStats(health=80, mana=150, strength=8, defense=5)

# Create a mage character
mage = Mage(name="Gandalf", stats=mage_stats)
```

### Defining Abilities and Spells

Ability: The base class for all abilities.

Spell: A subclass of Ability tailored for spellcasting.

```python
from rpg_world.ability.spell import Spell
from rpg_world.effect.spell_effect import SpellEffect

# Define a spell effect
burn = SpellEffect(effect_type="burn", damage=15, duration=3)

# Create a spell
flame_strike = Spell(
    name="Flame Strike",
    mana_cost=25,
    cooldown=10.0,
    effects=[burn]
)
```

### Managing Combat

BattleManager: Manages the flow of battles.

TurnOrder: Handles the sequence of turns in turn-based combat.

ActionQueue: Manages actions in real-time combat.

```python
from rpg_world.combat.battle_manager import BattleManager

# Initialize battle manager
battle_manager = BattleManager(player_party=[mage], enemy_party=[goblin])

# Start and run the battle
battle_manager.run_battle()
```

### Handling Items and Inventory

Item: Base class for all items.

Consumable: Items like potions that can be used.

Equipment: Items like weapons and armor that can be equipped.

Inventory: Manages a collection of items.

```python
from rpg_world.item.consumable import Consumable
from rpg_world.item.equipment import Equipment
from rpg_world.item.inventory import Inventory

# Create items
health_potion = Consumable(name="Health Potion", description="Heals 50 HP", value=50, healing_amount=50)
iron_sword = Equipment(name="Iron Sword", description="A sturdy iron sword", value=100, attack_bonus=5, defense_bonus=0)

# Create inventory and add items
inventory = Inventory()
inventory.add_item(health_potion)
inventory.add_item(iron_sword)

# List items
inventory.list_items()

# Use a consumable
inventory.use_item(health_potion, mage)

# Equip equipment
iron_sword.equip(mage)
```

### World and Exploration

World: Represents the entire game world.

Location: Specific areas within the world.

Event: Triggers and actions within locations.

```python
from rpg_world.world.world import World
from rpg_world.world.location import Location
from rpg_world.world.event import Event

# Create a world instance
game_world = World()

# Create locations
village = Location(name="Village", description="A peaceful village with friendly inhabitants.")
forest = Location(name="Forest", description="A dense forest teeming with wildlife.")

# Connect locations
village.add_connected_location("Forest")
forest.add_connected_location("Village")

# Add locations to the world
game_world.add_location(village)
game_world.add_location(forest)

# Set the starting location
game_world.set_starting_location("Village")

# Move to a different location
game_world.move_to_location("Forest")
```

### Quests and Objectives

Quest: Represents a quest with multiple objectives and rewards.

QuestObjective: Individual tasks within a quest.

QuestManager: Manages active quests and their progression.

```python
from rpg_world.quest.quest import Quest
from rpg_world.quest.quest_objective import QuestObjective
from rpg_world.quest.quest_manager import QuestManager

# Define quest objectives
collect_herbs = QuestObjective(description="Collect 5 healing herbs")
defeat_goblin = QuestObjective(description="Defeat the forest goblin")

# Create a quest
herbal_remedy = Quest(
    name="Herbal Remedy",
    description="Collect herbs and defeat the forest goblin to create a healing potion.",
    objectives=[collect_herbs, defeat_goblin],
    rewards={"gold": 100, "experience": 50}
)

# Initialize quest manager and add quest
quest_manager = QuestManager()
quest_manager.add_quest(herbal_remedy)

# List active quests
quest_manager.list_active_quests()

# Mark objectives as completed
collect_herbs.mark_completed()
defeat_goblin.mark_completed()

# Complete the quest
quest_manager.complete_quest(herbal_remedy)
```

### Saving and Loading

SaveManager: Handles saving game data.

LoadManager: Handles loading game data.

```python
from rpg_world.save_load.save_manager import SaveManager
from rpg_world.save_load.load_manager import LoadManager

# Initialize save and load managers
save_manager = SaveManager(file_path="savegame.json")
load_manager = LoadManager(file_path="savegame.json")

# Save game state
save_manager.save_game(game_state)

# Load game state
loaded_game_state = load_manager.load_game()
```

### Examples

The examples/ directory contains scripts demonstrating how to use various components of the rpg_world library.

- example_character.py: Examples of character creation and interaction.

- example_character_stats.py: Examples of creating and modifying character stats.

- example_game.py: Demonstrates the game loop and basic gameplay mechanics.

- example_spell.py: Shows how to create and cast spells.

#### Running an Example

To run an example, navigate to the examples/ directory and execute the desired script:

```bash
cd examples
python example_game.py
```

## Documentation

Comprehensive documentation is available in the docs/ directory. It includes detailed information on usage, API references, and tutorials to help you get the most out of the rpg_world library.

- index.md: Main documentation index.
- usage.md: Instructions on how to use various features.
- api_reference.md: Detailed API reference for developers.

To view the documentation, open the Markdown files in your preferred Markdown viewer or generate HTML documentation using tools like Sphinx.

## Testing

Unit and integration tests are located in the tests/ directory. These tests ensure that each component of the rpg_world library functions correctly.

### Running Tests

You can run the tests using the provided scripts or with pytest directly.

```bash
pytest
```

### Adding New Tests

To add new tests, create a new test file in the tests/ directory following the naming convention test_<module>.py. Write your test cases using the pytest framework. 

## Contributing

Contributions are welcome! To ensure a smooth collaboration process, please follow these guidelines:

### How to Contribute

#### Fork the Repository

Click the "Fork" button at the top right of the repository page to create a copy of the repository in your GitHub account.

#### Clone Your Fork

```bash
git clone https://github.com/andrewruba/rpg_world.git
cd rpg_world
```

#### Create a New Branch

```bash
git checkout -b feature/your-feature-name
```

#### Make Your Changes

Implement your feature or bug fix. Ensure that your code adheres to the project's coding standards.

#### Run Tests

Ensure all existing **tests pass** and **add new tests** for your changes.

```bash
pytest
```

#### Commit Your Changes

```bash
git add .
git commit -m "Add feature: your feature description"
```

#### Push to Your Fork

```bash
git push origin feature/your-feature-name
```

#### Create a Pull Request

Go to the original repository on GitHub and click "New Pull Request." Provide a clear description of your changes and submit the pull request.

### Coding Standards

Follow PEP 8 style guidelines.

Write clear and concise docstrings for all classes and methods.

Ensure readability and maintainability of code.

### Reporting Issues

If you encounter any bugs or have feature requests, please open an issue on the GitHub Issues page.

### License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.

### Contact

For any questions, suggestions, or support, feel free to reach out.

GitHub Issues: [rpg_world Issues](https://github.com/andrewruba/rpg_world/issues)

GitHub Discussions: [rpg_world Discussions](https://github.com/andrewruba/rpg_world/discussions)
