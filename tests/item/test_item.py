import pytest
from rpg_world import Item
from rpg_world import Effect
from rpg_world import SimpleChangeFormula, SimpleChangeFormulaWithStatLimits
from rpg_world import Character
from rpg_world import CharacterStats

# Mock effect class for testing
class MockEffect(Effect):
    def __init__(self, attribute, formula):
        super().__init__(attribute, formula)
    
    def apply(self, target, **kwargs):
        # Apply the effect by modifying the target's attribute
        super().apply(target, **kwargs)

    def __str__(self):
        return f"MockEffect({self.attribute})"

# Mock character class for testing
class MockCharacter(Character):
    def __init__(self, name, health, strength):
        stats = CharacterStats(health=health, strength=strength)
        super().__init__(name, stats)

# Mock item class for testing Item's functionality
class MockItem(Item):
    def __init__(self, name, description, value, effects):
        super().__init__(name, description, value, effects)

# Unit Tests

def test_item_initialization():
    # Create mock effects and an item
    effect1 = MockEffect("health", SimpleChangeFormula(10))
    effect2 = MockEffect("strength", SimpleChangeFormula(5))

    item = MockItem("Healing Potion", "Heals 10 health", 100, [effect1, effect2])

    # Check that the item is initialized correctly
    assert item.name == "Healing Potion"
    assert item.description == "Heals 10 health"
    assert item.value == 100
    assert len(item.effects) == 2

def test_item_use():
    # Create a mock character
    character = MockCharacter("Hero", health=50, strength=30)

    # Create mock effects and an item
    effect1 = MockEffect("health", SimpleChangeFormula(-10))  # Heals -10 health
    effect2 = MockEffect("strength", SimpleChangeFormula(5))  # Adds 5 strength

    item = MockItem("Healing Potion", "Heals -10 health and adds 5 strength", 100, [effect1, effect2])

    # Use the item on the character
    item.use(character)

    # Check that the effects have been applied correctly
    assert character.stats.get("health") == 40  # 50 - 10
    assert character.stats.get("strength") == 35  # 30 + 5

def test_item_use_does_not_exceed_max():
    # Create a mock character
    character = MockCharacter("Hero", health=50, strength=30)

    # Create mock effects and an item
    effect1 = MockEffect("health", SimpleChangeFormulaWithStatLimits(10))  # Heals 10 health
    effect2 = MockEffect("strength", SimpleChangeFormulaWithStatLimits(5))  # Adds 5 strength

    item = MockItem("Healing Potion", "Heals 10 health and adds 5 strength", 100, [effect1, effect2])

    # Use the item on the character
    item.use(character)

    # Check that the effects have been applied correctly
    assert character.stats.get("health") == 50  # max health is 50
    assert character.stats.get("strength") == 35  # 30 + 5

def test_item_str_representation():
    # Create mock effects and an item
    effect1 = MockEffect("health", SimpleChangeFormula(10))
    effect2 = MockEffect("strength", SimpleChangeFormula(5))

    item = MockItem("Strength Potion", "Adds 5 strength and heals 10 health", 150, [effect1, effect2])

    # Check the string representation of the item
    expected_str = "Item: Strength Potion, Value: 150, Description: Adds 5 strength and heals 10 health, Effects: MockEffect(health), MockEffect(strength)"
    assert str(item) == expected_str
