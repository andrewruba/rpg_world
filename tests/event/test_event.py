import pytest
from rpg_world import GameState, Character, Event, HealEvent, Trigger, CharacterStats
from rpg_world import HealthBelowThresholdTrigger

class MockTrigger(Trigger):
    """
    A mock trigger that can be manually set to evaluate as True or False.
    """
    def __init__(self, result=True):
        super().__init__(description="Mock trigger")
        self.result = result

    def evaluate(self, game_state):
        return self.result

@pytest.fixture
def game_state():
    """
    Fixture to initialize a new GameState instance for testing.
    """
    return GameState()

@pytest.fixture
def mock_character():
    """
    Fixture to create a mock character.
    """
    character = Character(name="Hero", stats=CharacterStats(), id="char_001")
    character.health = 50
    return character

def test_event_trigger_not_met(game_state, mock_character):
    """
    Test if the event is not triggered when triggers are not met.
    """
    # Create a mock character and add it to the game state
    game_state.add_character(mock_character)

    # Create a trigger that returns False
    trigger = MockTrigger(result=False)

    # Create an event with this trigger
    event = HealEvent(name="Heal Event", triggers=[trigger], character_id="char_001")

    # Check if the event is triggered
    assert not event.check_triggers(game_state)

def test_event_trigger_met(game_state, mock_character):
    """
    Test if the event is triggered when all triggers are met.
    """
    # Create a mock character and add it to the game state
    game_state.add_character(mock_character)

    # Create a trigger that returns True
    trigger = MockTrigger(result=True)

    # Create an event with this trigger
    event = HealEvent(name="Heal Event", triggers=[trigger], character_id="char_001")

    # Check if the event is triggered
    assert event.check_triggers(game_state)

def test_event_action_execution(game_state, mock_character):
    """
    Test if the event's action is executed when all triggers are met.
    """
    # Add mock character to game state
    game_state.add_character(mock_character)

    # Create a trigger that returns True
    trigger = MockTrigger(result=True)

    # Create a HealEvent with the trigger
    event = HealEvent(name="Heal Event", triggers=[trigger], character_id="char_001")

    # Check if the event is triggered and action is executed (healing character)
    event.check_triggers(game_state)

    # Verify that the character's health is restored to max health
    assert game_state.characters["char_001"].health == game_state.characters["char_001"].max_health

def test_event_reset(game_state, mock_character):
    """
    Test if the event can be reset and triggered again.
    """
    # Add mock character to game state
    game_state.add_character(mock_character)

    # Create a trigger that returns True
    trigger = MockTrigger(result=True)

    # Create a HealEvent with the trigger
    event = HealEvent(name="Heal Event", triggers=[trigger], character_id="char_001")

    # Trigger the event once
    assert event.check_triggers(game_state)

    # Verify that the event was triggered and health was restored
    assert event.triggered
    assert game_state.characters["char_001"].health == game_state.characters["char_001"].max_health

    # Reset the event and trigger again
    event.reset()
    assert not event.triggered
    event.check_triggers(game_state)
    assert game_state.characters["char_001"].health == game_state.characters["char_001"].max_health

def test_event_triggered_only_once(game_state, mock_character):
    """
    Test if the event only executes once unless reset.
    """
    # Add mock character to game state
    game_state.add_character(mock_character)

    # Create a trigger that returns True
    trigger = MockTrigger(result=True)

    # Create a HealEvent with the trigger
    event = HealEvent(name="Heal Event", triggers=[trigger], character_id="char_001")

    # Trigger and execute the event
    event.check_triggers(game_state)
    assert event.triggered

    # Lower character health and try triggering the event again without reset
    game_state.characters["char_001"].health = 10
    event.check_triggers(game_state)

    # Health should remain at 10 because the event was not re-triggered
    assert game_state.characters["char_001"].health == 10
