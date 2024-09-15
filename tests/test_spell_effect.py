import pytest
import time
from rpg_world import Spell, BaseCharacter, CharacterStats, Mage, SpellEffect
from rpg_world import SimpleChangeFormula, MultiEffectRecipientFormula, MultiEffectTargetFormula

@pytest.fixture
def multi_effect_spell():
    """
    Fixture to initialize the multi-effect spell "Mystic Blast".
    """
    return Spell(
        name="Mystic Blast",
        mana_cost=25.0,
        cooldown=1.0,
        effects=[
            SpellEffect(attribute='health', formula=MultiEffectRecipientFormula(), recipient='caster'),
            SpellEffect(attribute='health', formula=MultiEffectTargetFormula()),
            SpellEffect(attribute='focus', formula=SimpleChangeFormula(-15)),
            SpellEffect(attribute='armor', formula=SimpleChangeFormula(5))
        ]
    )

@pytest.fixture
def mage(multi_effect_spell):
    """
    Fixture to initialize a Mage character (Merlin) with the spell "Mystic Blast".
    """
    return Mage(name="Merlin", health=100, mana=100, focus=90, armor=10, spells=[multi_effect_spell])

@pytest.fixture
def goblin():
    """
    Fixture to initialize a target character (Goblin).
    """
    goblin_stats = CharacterStats(health=80, focus=40, armor=10)
    return BaseCharacter(name="Goblin", stats=goblin_stats)

def test_mage_initialization(mage):
    """
    Test if the Mage character is initialized correctly.
    """
    assert mage.get_attribute('health') == 100
    assert mage.get_attribute('mana') == 100
    assert mage.get_attribute('focus') == 90
    assert mage.get_attribute('armor') == 10
    assert "Mystic Blast" in mage.spells

def test_goblin_initialization(goblin):
    """
    Test if the Goblin character is initialized correctly.
    """
    assert goblin.get_attribute('health') == 80
    assert goblin.get_attribute('focus') == 40
    assert goblin.get_attribute('armor') == 10

def test_spell_cast(mage, goblin):
    """
    Test the effect of casting "Mystic Blast" from Mage (Merlin) to Goblin.
    """
    current_time = time.time()

    # Assert initial stats before casting the spell
    initial_mana = mage.get_attribute('mana')
    initial_goblin_health = goblin.get_attribute('health')
    initial_mage_health = mage.get_attribute('health')

    # Cast the spell
    mage.cast_spell("Mystic Blast", goblin, current_time)

    # Check if the spell reduced mana correctly
    assert mage.get_attribute('mana') == initial_mana - 25.0

    # Check the health effect on the goblin
    assert goblin.get_attribute('health') < initial_goblin_health

    # Check the focus and armor effects on the goblin
    assert goblin.get_attribute('focus') == 25  # Reduced by 15
    assert goblin.get_attribute('armor') == 15  # Increased by 5

    # Check if the spell had an effect on the caster's health
    assert mage.get_attribute('health') < initial_mage_health

    # Verify if the spell is on cooldown
    assert mage.spells["Mystic Blast"].is_on_cooldown(current_time)

def test_spell_cooldown(mage, goblin):
    """
    Test the cooldown functionality for spell casting.
    """
    # Cast the spell
    mage.cast_spell("Mystic Blast", goblin, time.time())

    # Try to cast again immediately (should fail due to cooldown)
    mage.cast_spell("Mystic Blast", goblin, time.time())

    # Assert that the second cast didn't occur (mana should remain unchanged)
    assert mage.get_attribute('mana') == 75  # Mana only deducted once

    # Wait for spell cooldown + little extra
    time.sleep(1.1)

    # Try to cast again (should succeed due to cooldown ending)
    mage.cast_spell("Mystic Blast", goblin, time.time())

    # Assert that the third cast did succeed and mana cost was deducted
    assert mage.get_attribute('mana') == 50
