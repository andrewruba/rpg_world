from abc import ABC, abstractmethod

class Formula(ABC):
    """
    Abstract base class for all formulas that calculate effect values in the game.
    Subclasses must implement the `calculate` method, which performs the specific calculation.
    """

    @abstractmethod
    def calculate(self, **kwargs):
        """
        Abstract method to calculate the effect value based on provided context.

        Args:
            **kwargs: Additional context variables passed during the calculation.

        Returns:
            float: The result of the formula's calculation.
        """
        pass

    def apply_limits(self, value, target, attribute):
        """
        Apply min/max limits to the calculated value, ensuring the resulting attribute value
        does not exceed the maximum or drop below the minimum.

        Args:
            value (float): The calculated effect amount on the target attribute.
            target (Character): The target character whose attribute is being modified.
            attribute (str): The name of the attribute to apply the limits on.

        Returns:
            float: The modified value that adheres to the attribute's min/max limits.
        """
        current_value = target.stats.get(attribute)
        max_value = target.stats.get(f"max_{attribute}")
        min_value = 0  # Assuming attributes like health/mana cannot drop below 0

        # Adjust the value to ensure it doesn't exceed the max limit
        if max_value is not None and current_value + value > max_value:
            value = max_value - current_value  # Return only the amount needed to reach max

        # Adjust the value to ensure it doesn't drop below the min limit
        if current_value + value < min_value:
            value = min_value - current_value  # Return only the amount needed to reach min

        return value
