import pytest
from rpg_world import Equipment
from rpg_world import Effect
from rpg_world import SimpleChangeFormula
from rpg_world import Character
from rpg_world import CharacterStats

# Mock effect class for testing
class MockEffect(Effect):
    def __init__(self, attribute, formula):
        super().__init__(attribute, formula)

    def apply(self, target, **kwargs):
        super().apply(target, **kwargs)

    def unapply(self, target, **kwargs):
        super().unapply(target, **kwargs)

    def __str__(self):
        return f"MockEffect({self.attribute})"

# Mock character class for testing
class MockCharacter(Character):
    def __init__(self, name, health, strength):
        stats = CharacterStats(health=health, strength=strength)
        super().__init__(name, stats)

# Unit Tests

def test_equipment_initialization():
    # Create mock effects and an equipment
    effect1 = MockEffect("health", SimpleChangeFormula(10))
    effect2 = MockEffect("strength", SimpleChangeFormula(5))

    equipment = Equipment("Sword", "A sharp blade.", 150, [effect1, effect2])

    # Check that the equipment is initialized correctly
    assert equipment.name == "Sword"
    assert equipment.description == "A sharp blade."
    assert equipment.value == 150
    assert len(equipment.effects) == 2
    assert not equipment.equipped  # The equipment should not be equipped initially

def test_equipment_equip():
    # Create a mock character
    character = MockCharacter("Hero", health=50, strength=30)

    # Create mock effects and an equipment
    effect1 = MockEffect("health", SimpleChangeFormula(10))  # Heals 10 health
    effect2 = MockEffect("strength", SimpleChangeFormula(5))  # Adds 5 strength

    equipment = Equipment("Sword", "A sharp blade.", 150, [effect1, effect2])

    # Equip the item
    equipment.equip(character)

    # Check that the equipment is now equipped and effects have been applied
    assert equipment.equipped
    assert character.stats.get("health") == 60  # 50 + 10
    assert character.stats.get("strength") == 35  # 30 + 5

def test_equipment_unequip():
    # Create a mock character
    character = MockCharacter("Hero", health=50, strength=30)

    # Create mock effects and an equipment
    effect1 = MockEffect("health", SimpleChangeFormula(10))  # Heals 10 health
    effect2 = MockEffect("strength", SimpleChangeFormula(5))  # Adds 5 strength

    equipment = Equipment("Sword", "A sharp blade.", 150, [effect1, effect2])

    # Equip and then unequip the item
    equipment.equip(character)
    equipment.unequip(character)

    # Check that the equipment is now unequipped and effects have been unapplied
    assert not equipment.equipped
    assert character.stats.get("health") == 50  # 60 - 10
    assert character.stats.get("strength") == 30  # 35 - 5

def test_equipment_use_toggle():
    # Create a mock character
    character = MockCharacter("Hero", health=50, strength=30)

    # Create mock effects and an equipment
    effect1 = MockEffect("health", SimpleChangeFormula(10))  # Heals 10 health
    effect2 = MockEffect("strength", SimpleChangeFormula(5))  # Adds 5 strength

    equipment = Equipment("Sword", "A sharp blade.", 150, [effect1, effect2])

    # Use the equipment (should equip it)
    equipment.use(character)
    assert equipment.equipped
    assert character.stats.get("health") == 60  # 50 + 10
    assert character.stats.get("strength") == 35  # 30 + 5

    # Use the equipment again (should unequip it)
    equipment.use(character)
    assert not equipment.equipped
    assert character.stats.get("health") == 50  # 60 - 10
    assert character.stats.get("strength") == 30  # 35 - 5

def test_equipment_str_representation():
    # Create mock effects and an equipment
    effect1 = MockEffect("health", SimpleChangeFormula(10))
    effect2 = MockEffect("strength", SimpleChangeFormula(5))

    equipment = Equipment("Sword", "A sharp blade.", 150, [effect1, effect2])

    # Check the string representation of the equipment
    expected_str = "Item: Sword, Value: 150, Description: A sharp blade., Effects: MockEffect(health), MockEffect(strength)"
    assert str(equipment) == expected_str
