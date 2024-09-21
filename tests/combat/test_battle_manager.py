import pytest
from rpg_world import (
    BattleManager,
    TurnOrder,
    SimpleFocusTurnOrderFormula,
    Character,
    CharacterStats
)

# Mock Character class for testing
class MockCharacter(Character):
    def __init__(self, name, focus):
        stats = CharacterStats(focus=focus)
        super().__init__(name, stats)

@pytest.fixture
def player_party():
    return [MockCharacter("Player1", 50), MockCharacter("Player2", 30)]

@pytest.fixture
def enemy_party():
    return [MockCharacter("Enemy1", 40), MockCharacter("Enemy2", 20)]

@pytest.fixture
def battle_manager(player_party, enemy_party):
    return BattleManager(player_party, enemy_party, SimpleFocusTurnOrderFormula)

def test_battle_starts_correctly(battle_manager, caplog):
    with caplog.at_level("INFO"):
        battle_manager.start_battle()
    assert "Battle started!" in caplog.text

def test_battle_turn_order(battle_manager):
    battle_manager.start_battle()
    next_character = battle_manager.get_next_turn()
    
    # Verify that the character with the highest focus takes the first turn
    assert next_character.name == "Player1"

def test_battle_outcome_player_wins(battle_manager, enemy_party):
    for enemy in battle_manager.enemy_party:
        enemy.health = 0

    outcome = battle_manager.check_battle_outcome()
    assert outcome == battle_manager.player_party

def test_battle_outcome_enemy_wins(battle_manager, player_party):
    for player in battle_manager.player_party:
        player.health = 0

    outcome = battle_manager.check_battle_outcome()
    assert outcome == battle_manager.enemy_party

def test_battle_is_ongoing(battle_manager):
    outcome = battle_manager.check_battle_outcome()
    assert outcome == None
