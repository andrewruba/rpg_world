import pytest
from rpg_world import Effect
from rpg_world import SimpleChangeFormula
from rpg_world import Character
from rpg_world import CharacterStats

# Mock class for testing purposes
class MockCharacter(Character):
    def __init__(self, name, health, strength):
        stats = CharacterStats(health=health, strength=strength)
        super().__init__(name, stats)

# Test Effect apply method
def test_effect_apply():
    # Create a mock character
    character = MockCharacter("Hero", health=100, strength=50)

    # Create a simple formula for a strength effect
    formula = SimpleChangeFormula(10)  # Adds 10 to the strength
    effect = Effect("strength", formula)

    # Apply the effect
    effect.apply(character)

    # Assert that the strength increased by 10
    assert character.stats.get("strength") == 60

# Test Effect unapply method
def test_effect_unapply():
    # Create a mock character
    character = MockCharacter("Hero", health=100, strength=50)

    # Create a simple formula for a strength effect
    formula = SimpleChangeFormula(10)  # Adds 10 to the strength
    effect = Effect("strength", formula)

    # Apply the effect
    effect.apply(character)
    # Assert that the strength increased by 10
    assert character.stats.get("strength") == 60

    # Unapply the effect
    effect.unapply(character)
    
    # Assert that the strength returned to its original value
    assert character.stats.get("strength") == 50

# Test Effect with a health attribute
def test_effect_health():
    # Create a mock character
    character = MockCharacter("Hero", health=100, strength=50)

    # Create a simple formula for a health effect
    formula = SimpleChangeFormula(-20)  # Decreases health by 20
    effect = Effect("health", formula)

    # Apply the effect
    effect.apply(character)

    # Assert that the health decreased by 20
    assert character.stats.get("health") == 80

    # Unapply the effect
    effect.unapply(character)

    # Assert that the health returned to its original value
    assert character.stats.get("health") == 100

# Test that Effect warns if no attribute is specified
def test_effect_no_attribute(caplog):
    # Create a mock character
    character = MockCharacter("Hero", health=100, strength=50)

    # Create a simple formula
    formula = SimpleChangeFormula(10)
    
    # Create an effect with no attribute (invalid case)
    effect = Effect(None, formula)

    # Apply the effect and capture log output
    with caplog.at_level("WARNING"):
        effect.apply(character)

    # Assert that a warning was logged
    assert "No attribute specified in effect" in caplog.text
