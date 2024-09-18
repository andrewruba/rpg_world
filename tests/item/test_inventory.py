import pytest
from rpg_world import Inventory
from rpg_world import Item
from rpg_world import Character
from rpg_world import CharacterStats

# Mock Item for testing
class MockItem(Item):
    def __init__(self, name):
        super().__init__(name, "Test item", 10, [])

    def use(self, target):
        # Simulate item use by increasing health
        target.stats.modify("health", 10)

# Fixtures for setting up test scenarios
@pytest.fixture
def setup_target():
    stats = CharacterStats(health=50, mana=50, focus=30, armor=20)
    target = Character("TestCharacter", stats)
    return target

@pytest.fixture
def setup_inventory():
    return Inventory()

@pytest.fixture
def setup_item():
    return MockItem("TestPotion")

# Tests for Inventory class
def test_add_item(setup_inventory, setup_item):
    inventory = setup_inventory
    item = setup_item

    # Ensure inventory is initially empty
    assert len(inventory.items) == 0

    # Add an item and verify
    inventory.add_item(item)
    assert len(inventory.items) == 1
    assert inventory.items[0] == item

def test_remove_item(setup_inventory, setup_item):
    inventory = setup_inventory
    item = setup_item

    # Add the item and then remove it
    inventory.add_item(item)
    assert len(inventory.items) == 1
    inventory.remove_item(item)
    assert len(inventory.items) == 0

def test_remove_non_existent_item(setup_inventory, setup_item):
    inventory = setup_inventory
    item = setup_item

    # Try to remove an item not in the inventory
    inventory.remove_item(item)  # Should trigger warning but not raise an error

def test_list_items(setup_inventory, setup_item, caplog):
    inventory = setup_inventory
    item = setup_item

    # Check listing for an empty inventory
    inventory.list_items()
    assert "The inventory is empty." in caplog.text

    # Add an item and list items
    inventory.add_item(item)
    inventory.list_items()
    assert f"- {item}" in caplog.text
