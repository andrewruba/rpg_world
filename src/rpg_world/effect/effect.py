from abc import ABC
from ..utils.logger import Logger

class Effect(ABC):
    """
    Represents an effect that can be applied to a character. Effects modify the specified
    attribute of the target based on a formula.
    """

    def __init__(self, attribute: str, formula):
        """
        Initialize the Effect with an attribute and a formula object.

        Args:
            attribute (str): The name of the attribute to affect (e.g., 'health', 'mana').
            formula (Formula): An instance of Formula used to calculate the change in attribute value.
                               The formula should have a `calculate` method that accepts context variables
                               like 'target' and 'attribute'.
        """
        self.attribute = attribute
        self.formula = formula

        # Initialize logger for this effect
        self.logger = Logger("Effect")
        self.logger.info(f"Effect initialized to affect attribute: {self.attribute}")

    def apply(self, target, **kwargs):
        """
        Apply the effect to the target character, modifying the specified attribute.

        Args:
            target (Character): The character to apply the effect to.
            **kwargs: Additional context variables that can be used in the formula.

        Returns:
            None
        """
        if not self.attribute:
            self.logger.warning(f"No attribute specified in effect: {self}")
            return

        # Calculate the amount to modify the attribute using the formula
        amount = self._calculate_amount(target, **kwargs)

        # Modify the target's attribute
        target.stats.modify(self.attribute, amount)
        self.logger.info(f"{target.name}'s {self.attribute} changed by {amount}. New value: {target.stats.get(self.attribute)}")

    def unapply(self, target, **kwargs):
        """
        Reverse the effect applied to the target character by undoing the attribute modification.

        Args:
            target (Character): The character to reverse the effect on.
            **kwargs: Additional context variables that can be used in the formula.

        Returns:
            None
        """
        if not self.attribute:
            self.logger.warning(f"No attribute specified in effect: {self}")
            return

        # Calculate the amount to reverse the attribute modification
        amount = self._calculate_amount(target, **kwargs)

        # Reverse the modification of the target's attribute
        target.stats.modify(self.attribute, -amount)
        self.logger.info(f"{target.name}'s {self.attribute} reversed by {amount}. New value: {target.stats.get(self.attribute)}")

    def _calculate_amount(self, target, **kwargs):
        """
        Calculate the amount of change to the target's attribute using the provided formula.

        Args:
            target (Character): The character whose attribute is being modified.
            **kwargs: Additional context variables for the formula.

        Returns:
            float: The calculated amount of change for the attribute.
        """
        amount = self.formula.calculate(
            target=target,
            attribute=self.attribute,
            **kwargs
        )

        return amount

    def __str__(self):
        """
        Return a string representation of the effect.

        Returns:
            str: A string describing the effect, including the attribute and formula.
        """
        return f"Effect({self.attribute}, {self.formula})"
