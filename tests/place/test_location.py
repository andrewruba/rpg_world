import pytest
from rpg_world import Location, Position

@pytest.fixture
def setup_location():
    # Initialize a location for testing
    return Location(name="Forest", description="A dense, mysterious forest.")


def test_location_initialization_without_position(setup_location):
    location = setup_location
    
    # Verify location's initial details
    assert location.name == "Forest"
    assert location.description == "A dense, mysterious forest."
    assert location.current_position.x == 0
    assert location.current_position.y == 0
    assert location.connected_locations == []


def test_location_initialization_with_position():
    initial_position = Position("Town position", 5, 5)
    location = Location(name="Town", description="A peaceful village.", initial_position=initial_position)

    # Verify that the initial position was set correctly
    assert location.current_position.x == 5
    assert location.current_position.y == 5


def test_add_connected_location(setup_location):
    location = setup_location
    location.add_connected_location("Town")

    # Check if the location is added to the connected locations
    assert "Town" in location.connected_locations


def test_update_position(setup_location):
    location = setup_location
    new_position = Position("Town position", 3, 7)

    # Update the player's position in the location
    location.update_position(new_position)

    # Verify the player's new position
    assert location.current_position.x == 3
    assert location.current_position.y == 7
