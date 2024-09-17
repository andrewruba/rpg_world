import pytest
from rpg_world import Consumable
from rpg_world import BaseEffect
from rpg_world import BaseCharacter
from rpg_world import CharacterStats
from rpg_world import SimpleChangeFormula

# Mock effect class for testing
class MockEffect(BaseEffect):
    def __init__(self, attribute, formula):
        super().__init__(attribute, formula)
    
    def apply(self, target, **kwargs):
        # Apply the effect by modifying the target's attribute
        super().apply(target, **kwargs)

    def __str__(self):
        return f"MockEffect({self.attribute})"

effect = MockEffect("health", SimpleChangeFormula(10))

# Fixtures for setting up test scenarios
@pytest.fixture
def setup_target():
    stats = CharacterStats(health=50, mana=50, focus=30, armor=20)
    target = BaseCharacter("TestCharacter", stats)
    return target

@pytest.fixture
def setup_consumable():
    effects = [effect]
    return Consumable(name="Health Potion", description="Heals health and mana", value=50, effects=effects)

# Tests for Consumable class
def test_consumable_use(setup_consumable, setup_target):
    consumable = setup_consumable
    target = setup_target

    # Ensure initial health and mana values
    assert target.stats.get("health") == 50
    assert target.stats.get("mana") == 50

    # Use the consumable
    consumable.use(target)

    # Check that the effects were applied correctly
    assert target.stats.get("health") == 60  # Health modified by 10
    assert target.stats.get("mana") == 50  # Mana modified by 10
