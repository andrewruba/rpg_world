import pytest
from rpg_world import BaseEffect
from rpg_world import SimpleChangeFormula
from rpg_world import BaseCharacter
from rpg_world import CharacterStats

# Mock class for testing purposes
class MockCharacter(BaseCharacter):
    def __init__(self, name, health, strength):
        stats = CharacterStats(health=health, strength=strength)
        super().__init__(name, stats)

# Test BaseEffect apply method
def test_base_effect_apply():
    # Create a mock character
    character = MockCharacter("Hero", health=100, strength=50)

    # Create a simple formula for a strength effect
    formula = SimpleChangeFormula(10)  # Adds 10 to the strength
    effect = BaseEffect("strength", formula)

    # Apply the effect
    effect.apply(character)

    # Assert that the strength increased by 10
    assert character.stats.get("strength") == 60

# Test BaseEffect unapply method
def test_base_effect_unapply():
    # Create a mock character
    character = MockCharacter("Hero", health=100, strength=50)

    # Create a simple formula for a strength effect
    formula = SimpleChangeFormula(10)  # Adds 10 to the strength
    effect = BaseEffect("strength", formula)

    # Apply the effect
    effect.apply(character)
    # Assert that the strength increased by 10
    assert character.stats.get("strength") == 60

    # Unapply the effect
    effect.unapply(character)
    
    # Assert that the strength returned to its original value
    assert character.stats.get("strength") == 50

# Test BaseEffect with a health attribute
def test_base_effect_health():
    # Create a mock character
    character = MockCharacter("Hero", health=100, strength=50)

    # Create a simple formula for a health effect
    formula = SimpleChangeFormula(-20)  # Decreases health by 20
    effect = BaseEffect("health", formula)

    # Apply the effect
    effect.apply(character)

    # Assert that the health decreased by 20
    assert character.stats.get("health") == 80

    # Unapply the effect
    effect.unapply(character)

    # Assert that the health returned to its original value
    assert character.stats.get("health") == 100

# Test that BaseEffect warns if no attribute is specified
def test_base_effect_no_attribute(caplog):
    # Create a mock character
    character = MockCharacter("Hero", health=100, strength=50)

    # Create a simple formula
    formula = SimpleChangeFormula(10)
    
    # Create an effect with no attribute (invalid case)
    effect = BaseEffect(None, formula)

    # Apply the effect and capture log output
    with caplog.at_level("WARNING"):
        effect.apply(character)

    # Assert that a warning was logged
    assert "No attribute specified in effect" in caplog.text
