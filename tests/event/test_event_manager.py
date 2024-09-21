import pytest
from rpg_world import EventManager

# Mock Event class for testing
class MockEvent:
    def __init__(self, name, triggered=False):
        self.name = name
        self.triggered = triggered

    def check_triggers(self, game_state):
        """
        Mock method to simulate checking the event trigger.
        """
        self.triggered = True  # Simulate that the event is triggered


# Mock GameState for testing
class MockGameState:
    def __init__(self):
        self.state = "MockGameState"


@pytest.fixture
def event_manager():
    """
    Fixture to initialize the EventManager.
    """
    return EventManager(id="event_manager_id", name="Event Manager Name", description="Event Manager description.")


@pytest.fixture
def mock_game_state():
    """
    Fixture to initialize a mock GameState.
    """
    return MockGameState()

def test_init_event_manager(event_manager):
    """
    Test that EventManager is initialized properly.
    """

    assert event_manager.id == "event_manager_id"
    assert event_manager.name == "Event Manager Name"
    assert event_manager.description == "Event Manager description."

def test_add_event(event_manager):
    """
    Test that events can be added to the EventManager.
    """
    event = MockEvent(name="Test Event")
    event_manager.add_event(event)

    # Check that the event has been added
    assert len(event_manager.events) == 1
    assert event_manager.events[0].name == "Test Event"


def test_remove_event(event_manager):
    """
    Test that events can be removed from the EventManager.
    """
    event = MockEvent(name="Test Event")
    event_manager.add_event(event)
    assert len(event_manager.events) == 1

    # Remove the event
    event_manager.remove_event(event)
    assert len(event_manager.events) == 0


def test_check_events(event_manager, mock_game_state):
    """
    Test that events are properly checked and their triggers evaluated.
    """
    event1 = MockEvent(name="Test Event 1", triggered=False)
    event2 = MockEvent(name="Test Event 2", triggered=False)
    
    # Add events to the manager
    event_manager.add_event(event1)
    event_manager.add_event(event2)

    # Call check_events and ensure triggers are evaluated
    event_manager.check_events(mock_game_state)

    # Verify that all events have been triggered
    assert event1.triggered is True
    assert event2.triggered is True
