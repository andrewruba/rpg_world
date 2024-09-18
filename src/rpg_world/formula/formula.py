from abc import ABC, abstractmethod

class Formula(ABC):
    """
    Abstract base class for all formulas that calculate effect values.
    """

    @abstractmethod
    def calculate(self, **kwargs):
        """
        Abstract method to calculate the effect value.
        
        Args:
            **kwargs: Additional context variables.
        
        Returns:
            The result of the calculation.
        """
        pass

    def apply_limits(self, value, target, attribute):
        """
        Apply min/max limits to the calculated value. If the full value exceeds the limits,
        return the value required to exactly reach the limit from the current attribute level.

        Args:
            value (float): The calculated effect amount on the target attribute.
            target (Character): The target character whose attribute is being modified.
            attribute (str): The name of the attribute to apply the limits on.

        Returns:
            float: The modified value that will not exceed the limits.
        """
        current_value = target.stats.get(attribute)
        max_value = target.stats.get(f"max_{attribute}")
        min_value = 0  # Assuming the minimum is always 0 for attributes like health/mana

        # If the value would go over max
        if max_value is not None and current_value + value > max_value:
            value = max_value - current_value  # Return only the amount needed to reach max

        # If the value would go below min
        if current_value + value < min_value:
            value = min_value - current_value  # Return only the amount needed to reach min

        return value
