import pytest
from rpg_world import Position

def test_position_initialization():
    pos = Position("Test", 5, 10)

    # Check if the position is initialized correctly
    assert pos.x == 5
    assert pos.y == 10

def test_position_representation():
    pos = Position("Test", 3, 7)

    # Check the string representation of the Position object
    assert repr(pos) == "Position(Test, 3, 7)"

def test_position_equals_true():
    pos1 = Position("Test1", 4, 8)
    pos2 = Position("Test2", 4, 8)

    # Check if two positions are equal
    assert pos1.equals(pos2)

def test_position_equals_false():
    pos1 = Position("Test", 1, 2)
    pos2 = Position("Test", 2, 3)

    # Check if two different positions are not equal
    assert not pos1.equals(pos2)

def test_position_distance():
    pos1 = Position("Test", 0, 0)
    pos2 = Position("Test", 3, 4)

    # Check if the distance is correctly calculated
    assert pos1.distance_to(pos2) == 5.0

def test_position_distance_same_point():
    pos1 = Position("Test", 2, 2)
    pos2 = Position("Test", 2, 2)

    # Distance between the same points should be 0
    assert pos1.distance_to(pos2) == 0.0
