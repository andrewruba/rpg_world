import pytest
from rpg_world import Location
from rpg_world import Position
from rpg_world import World


# Fixtures for testing
@pytest.fixture
def setup_world():
    world = World("Earth")

    # Create locations
    town = Location("Town", "A small peaceful town.")
    forest = Location("Forest", "A dark, dense forest.")
    cave = Location("Cave", "A mysterious cave with echoes.")

    # Connect locations
    town.add_connected_location("Forest")
    forest.add_connected_location("Cave")

    # Add locations to world
    world.add_location(town)
    world.add_location(forest)
    world.add_location(cave)

    return world


def test_add_location(setup_world):
    world = setup_world

    # Check if locations have been added correctly
    assert "Town" in world.locations
    assert "Forest" in world.locations
    assert "Cave" in world.locations


def test_set_starting_location(setup_world):
    world = setup_world

    # Set and verify the starting location
    world.set_starting_location("Town")
    assert world.current_location.name == "Town"

    world.set_starting_location("Forest")
    assert world.current_location.name == "Forest"

    # Test invalid location
    world.set_starting_location("InvalidLocation")
    assert world.current_location.name == "Forest"  # No change


def test_move_to_connected_location(setup_world):
    world = setup_world

    world.set_starting_location("Town")

    # Move to a connected location
    world.move_to_location("Forest")
    assert world.current_location.name == "Forest"

    # Move to another connected location
    world.move_to_location("Cave")
    assert world.current_location.name == "Cave"


def test_move_to_unconnected_location(setup_world):
    world = setup_world

    world.set_starting_location("Town")

    # Try to move to an unconnected location
    world.move_to_location("Cave")
    assert world.current_location.name == "Town"  # No change


def test_move_with_new_position(setup_world):
    world = setup_world

    world.set_starting_location("Town")
    new_position = Position("Forest Position", 5, 10)

    # Move to a connected location with a new position
    world.move_to_location("Forest", new_position=new_position)
    assert world.current_location.name == "Forest"
    assert world.current_location.current_position.x == 5
    assert world.current_location.current_position.y == 10
