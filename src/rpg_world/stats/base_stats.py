class BaseStats:
    """
    Base class for managing general statistics. Provides methods to modify and retrieve attributes.
    """

    def __init__(self, **kwargs):
        """
        Initialize the statistics with any provided attributes.

        Args:
            **kwargs: Key-value pairs for initializing the stats.
        """
        self.attributes = kwargs

    def get(self, attr_name):
        """
        Retrieve the value of a specific attribute.

        Args:
            attr_name (str): The name of the attribute to retrieve.

        Returns:
            The value of the attribute or None if it doesn't exist.
        """
        return self.attributes.get(attr_name)

    def set(self, attr_name, value):
        """
        Set the value of a specific attribute.

        Args:
            attr_name (str): The name of the attribute to set.
            value: The value to assign to the attribute.
        """
        self.attributes[attr_name] = value

    def modify(self, attr_name, amount):
        """
        Modify the value of an attribute by a specified amount.

        Args:
            attr_name (str): The name of the attribute to modify.
            amount (float): The amount to add (or subtract) from the attribute.
        """
        current_value = self.get(attr_name) or 0
        new_value = current_value + amount
        self.set(attr_name, new_value)

    def __getattr__(self, attr_name):
        """
        Override __getattr__ to dynamically return attributes from the attributes dictionary.

        Args:
            attr_name (str): The name of the attribute to retrieve.

        Returns:
            The value of the attribute if it exists in the dictionary.
        """
        if attr_name in self.attributes:
            return self.attributes[attr_name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr_name}'")

    def __setattr__(self, attr_name, value):
        """
        Override __setattr__ to dynamically set attributes in the attributes dictionary.

        Args:
            attr_name (str): The name of the attribute to set.
            value: The value to assign to the attribute.
        """
        if attr_name == 'attributes':
            super().__setattr__(attr_name, value)
        else:
            self.attributes[attr_name] = value

    def __str__(self):
        """
        String representation of the statistics.

        Returns:
            str: A string listing the attributes and their values.
        """
        attrs = ', '.join(f"{key}: {value}" for key, value in self.attributes.items())
        return f"BaseStats({attrs})"
