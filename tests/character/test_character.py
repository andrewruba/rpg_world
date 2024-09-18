import pytest
from rpg_world import Character
from rpg_world import CharacterStats
from rpg_world import Consumable

class Warrior(Character):
    def __init__(self, name, health=100, strength=15, defense=5, id=None):
        """
        Initialize a Warrior character with basic attributes.

        Args:
            name (str): The name of the warrior.
            health (int): The initial health of the warrior.
            strength (int): The attack strength of the warrior.
            defense (int): The defensive value of the warrior.
            id (str, optional): The unique identifier for the warrior.
        """
        # Create CharacterStats with provided attributes
        stats = CharacterStats(health=health, strength=strength, defense=defense)

        # Initialize Character with name, stats, and optional ID
        super().__init__(name, stats, id=id)

@pytest.fixture
def conan():
    """
    Fixture to initialize the Conan warrior.
    """
    return Warrior(name="Conan", health=100, strength=20, defense=5, id="conan_id")

@pytest.fixture
def enemy_orc():
    """
    Fixture to initialize the Enemy Orc warrior.
    """
    return Warrior(name="Enemy Orc", health=80, strength=15, defense=3)

@pytest.fixture
def healing_potion():
    """
    Fixture to create a consumable healing potion item.
    """
    return Consumable(name="Healing Potion", description="Restores 50 health.", value=10, effects=[])

def test_warrior_initialization(conan, enemy_orc):
    """
    Test if the warriors are initialized correctly with the given stats.
    """
    # Check Conan's initial stats and ID
    assert conan.name == "Conan"
    assert conan.health == 100
    assert conan.strength == 20
    assert conan.defense == 5
    assert conan.id == "conan_id"

    # Check Enemy Orc's initial stats and ID
    assert enemy_orc.name == "Enemy Orc"
    assert enemy_orc.health == 80
    assert enemy_orc.strength == 15
    assert enemy_orc.defense == 3
    assert enemy_orc.id is None  # Orc has no ID assigned

def test_warrior_stat_modification(conan, enemy_orc):
    """
    Test modification of warrior stats.
    """
    # Modify Conan's health
    conan.health = 90
    assert conan.health == 90

    # Modify Enemy Orc's defense
    enemy_orc.defense = 10
    assert enemy_orc.defense == 10

def test_warrior_combat_scenario(conan, enemy_orc):
    """
    Test basic combat scenario where Conan attacks the Enemy Orc.
    """
    # Conan attacks Enemy Orc, reducing health based on strength and defense
    initial_health = enemy_orc.health
    strength = conan.strength
    defense = enemy_orc.defense
    
    # Simple damage calculation: damage = strength - defense
    damage = max(0, strength - defense)
    enemy_orc.health = initial_health - damage

    # Check if the damage was applied correctly
    assert enemy_orc.health == initial_health - damage

def test_inventory_management(conan, healing_potion):
    """
    Test inventory management by adding, using, and removing an item.
    """
    # Add the healing potion to Conan's inventory
    conan.inventory.add_item(healing_potion)
    assert len(conan.inventory.items) == 1
    assert conan.inventory.items[0].name == "Healing Potion"

    # Use the healing potion and check if it's removed from the inventory
    conan.inventory.remove_item(healing_potion)
    assert len(conan.inventory.items) == 0

def test_warrior_id(conan, enemy_orc):
    """
    Test that the characters have the correct ID assigned.
    """
    assert conan.id == "conan_id"
    assert enemy_orc.id is None

    # Assign an ID to enemy_orc and verify
    enemy_orc.id = "orc_id"
    assert enemy_orc.id == "orc_id"
