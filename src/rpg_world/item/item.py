class Item:
    def __init__(self, name: str, description: str, value: int):
        """
        Initialize the base item class.

        Args:
            name (str): The name of the item.
            description (str): A brief description of the item.
            value (int): The monetary value of the item.
        """
        self.name = name
        self.description = description
        self.value = value

    def use(self, target):
        """
        Method to be overridden by subclasses. Defines how the item is used.

        Args:
            target (BaseCharacter): The character that will use the item.
        """
        raise NotImplementedError("The use method must be overridden by subclasses.")

    def __str__(self):
        """
        String representation of the item.

        Returns:
            str: A string describing the item.
        """
        return f"Item: {self.name}, Value: {self.value}, Description: {self.description}"
