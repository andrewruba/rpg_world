import pytest
from rpg_world import BaseCharacter, CharacterStats, BaseEffect, SimpleChangeFormula

@pytest.fixture
def arcanist():
    """
    Fixture to initialize the Arcanist character.
    """
    stats = CharacterStats(health=120, mana=80, focus=100, armor=10)
    return BaseCharacter(name="Arcanist", stats=stats)

def test_character_initialization(arcanist):
    """
    Test if the Arcanist character is initialized correctly.
    """
    assert arcanist.health == 120
    assert arcanist.mana == 80
    assert arcanist.focus == 100
    assert arcanist.armor == 10

def test_apply_health_effect(arcanist):
    """
    Test applying a health damage effect to the character.
    """
    health_effect = BaseEffect(attribute='health', formula=SimpleChangeFormula(-30))
    health_effect.apply(arcanist)
    
    assert arcanist.health == 90

def test_apply_mana_effect(arcanist):
    """
    Test applying a mana reduction effect to the character.
    """
    mana_effect = BaseEffect(attribute='mana', formula=SimpleChangeFormula(-20))
    mana_effect.apply(arcanist)

    assert arcanist.mana == 60

def test_apply_focus_effect(arcanist):
    """
    Test applying a focus increase effect to the character.
    """
    focus_effect = BaseEffect(attribute='focus', formula=SimpleChangeFormula(-10))
    focus_effect.apply(arcanist)

    assert arcanist.focus == 90

def test_apply_zero_health_effect(arcanist):
    """
    Test applying a focus increase effect to the character.
    """
    health_effect = BaseEffect(attribute='health', formula=SimpleChangeFormula(0))
    health_effect.apply(arcanist)
    
    assert arcanist.health == 120

def test_apply_health_effect_above_max(arcanist):
    """
    Test applying a focus increase effect to the character.
    """
    health_effect = BaseEffect(attribute='health', formula=SimpleChangeFormula(1000))
    health_effect.apply(arcanist)
    
    assert arcanist.health == 120

def test_character_alive_status(arcanist):
    """
    Test if the character is alive after taking damage.
    """
    health_effect = BaseEffect(attribute='health', formula=SimpleChangeFormula(-120))
    health_effect.apply(arcanist)
    
    assert not arcanist.is_alive(), f"{arcanist.name} should be dead after taking 120 damage."
