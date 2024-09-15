import pytest
from rpg_world import BaseCharacter
from rpg_world import CharacterStats

class Warrior(BaseCharacter):
    def __init__(self, name, health=100, strength=15, defense=5):
        """
        Initialize a Warrior character with basic attributes.

        Args:
            name (str): The name of the warrior.
            health (int): The initial health of the warrior.
            strength (int): The attack strength of the warrior.
            defense (int): The defensive value of the warrior.
        """
        # Create CharacterStats with provided attributes
        stats = CharacterStats(health=health, strength=strength, defense=defense)

        # Initialize BaseCharacter with name and stats
        super().__init__(name, stats)

@pytest.fixture
def conan():
    """
    Fixture to initialize the Conan warrior.
    """
    return Warrior(name="Conan", health=100, strength=20, defense=5)

@pytest.fixture
def enemy_orc():
    """
    Fixture to initialize the Enemy Orc warrior.
    """
    return Warrior(name="Enemy Orc", health=80, strength=15, defense=3)

def test_warrior_initialization(conan, enemy_orc):
    """
    Test if the warriors are initialized correctly with the given stats.
    """
    # Check Conan's initial stats
    assert conan.name == "Conan"
    assert conan.get_attribute('health') == 100
    assert conan.get_attribute('strength') == 20
    assert conan.get_attribute('defense') == 5

    # Check Enemy Orc's initial stats
    assert enemy_orc.name == "Enemy Orc"
    assert enemy_orc.get_attribute('health') == 80
    assert enemy_orc.get_attribute('strength') == 15
    assert enemy_orc.get_attribute('defense') == 3

def test_warrior_stat_modification(conan, enemy_orc):
    """
    Test modification of warrior stats.
    """
    # Modify Conan's health
    conan.set_attribute('health', 90)
    assert conan.get_attribute('health') == 90

    # Modify Enemy Orc's defense
    enemy_orc.set_attribute('defense', 10)
    assert enemy_orc.get_attribute('defense') == 10

def test_warrior_combat_scenario(conan, enemy_orc):
    """
    Test basic combat scenario where Conan attacks the Enemy Orc.
    """
    # Conan attacks Enemy Orc, reducing health based on strength and defense
    initial_health = enemy_orc.get_attribute('health')
    strength = conan.get_attribute('strength')
    defense = enemy_orc.get_attribute('defense')
    
    # Simple damage calculation: damage = strength - defense
    damage = max(0, strength - defense)
    enemy_orc.set_attribute('health', initial_health - damage)

    # Check if the damage was applied correctly
    assert enemy_orc.get_attribute('health') == initial_health - damage
