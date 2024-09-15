class Inventory:
    def __init__(self):
        """
        Initialize the inventory as an empty list of items.
        """
        self.items = []

    def add_item(self, item):
        """
        Add an item to the inventory.

        Args:
            item (Item): The item to be added.
        """
        self.items.append(item)
        print(f"Added {item.name} to the inventory.")

    def remove_item(self, item):
        """
        Remove an item from the inventory.

        Args:
            item (Item): The item to be removed.
        """
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item.name} from the inventory.")
        else:
            print(f"Item {item.name} not found in inventory.")

    def list_items(self):
        """
        List all items in the inventory.
        """
        if not self.items:
            print("The inventory is empty.")
        else:
            for item in self.items:
                print(item)

    def use_item(self, item, target):
        """
        Use an item from the inventory.

        Args:
            item (Item): The item to be used.
            target (BaseCharacter): The target on whom the item is used.
        """
        if item in self.items:
            item.use(target)
            self.remove_item(item)
        else:
            print(f"Item {item.name} is not in the inventory.")
