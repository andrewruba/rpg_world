import pytest
from rpg_world import TurnOrder
from rpg_world import SimpleFocusTurnOrderFormula

# Mock Character class for testing
class MockCharacter:
    def __init__(self, name, health, focus):
        self.name = name
        self.health = health
        self.focus = focus

@pytest.fixture
def characters():
    return [MockCharacter("Character1", 100, 10), MockCharacter("Character2", 100, 50), MockCharacter("Character3", 100, 30)]

@pytest.fixture
def turn_order(characters):
    return TurnOrder(characters, SimpleFocusTurnOrderFormula)

def test_turn_order_calculation(turn_order):
    turn_order.calculate_turn_order()
    assert turn_order.turn_queue[0].name == "Character2"
    assert turn_order.turn_queue[1].name == "Character3"
    assert turn_order.turn_queue[2].name == "Character1"

def test_turn_order_get_next_turn(turn_order):
    next_character = turn_order.get_next_turn()
    assert next_character.name == "Character2"

    # Ensure the next call returns the next character in the queue
    next_character = turn_order.get_next_turn()
    assert next_character.name == "Character3"

def test_turn_order_gets_recalculated(turn_order):
    next_character = turn_order.get_next_turn()
    assert next_character.name == "Character2"

    # Ensure the next call returns the next character in the queue
    next_character = turn_order.get_next_turn()
    assert next_character.name == "Character3"

    # Ensure the next call returns the last character in the queue
    # and queue gets recalculated
    assert len(turn_order.turn_queue) == 1
    next_character = turn_order.get_next_turn()
    assert next_character.name == "Character1"
    assert len(turn_order.turn_queue) == 3
