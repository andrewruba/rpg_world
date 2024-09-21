from ..utils.logger import Logger

class Inventory:
    """
    Represents an inventory that can store items, add or remove items, and list the contents.
    """

    def __init__(self):
        """
        Initialize the inventory as an empty list of items.
        """
        self.items = []
        self.logger = Logger("Inventory")
        self.logger.info("Inventory initialized.")

    def add_item(self, item):
        """
        Add an item to the inventory.

        Args:
            item (Item): The item to be added to the inventory.
        """
        self.items.append(item)
        self.logger.info(f"Added {item.name} to the inventory.")

    def remove_item(self, item):
        """
        Remove an item from the inventory.

        Args:
            item (Item): The item to be removed from the inventory.
        """
        if item in self.items:
            self.items.remove(item)
            self.logger.info(f"Removed {item.name} from the inventory.")
        else:
            self.logger.warning(f"Item {item.name} not found in inventory.")

    def list_items(self):
        """
        List all items currently stored in the inventory.
        """
        if not self.items:
            self.logger.info("The inventory is empty.")
        else:
            self.logger.info("Listing inventory items:")
            for item in self.items:
                self.logger.info(f"- {item}")
