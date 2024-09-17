from abc import ABC
from ..utils.logger import Logger

class BaseEffect(ABC):
    """
    Represents an effect that can be applied to a character.
    """

    def __init__(self, attribute: str, formula):
        """
        Initialize the BaseEffect with an attribute and a formula object.

        Args:
            attribute (str): The name of the attribute to affect.
            formula (BaseFormula): An instance of BaseFormula used to calculate the change in attribute value.
                                   It should have a `calculate` method that accepts context variables as keyword arguments.
        """
        self.attribute = attribute
        self.formula = formula

        # Initialize logger for this ability
        self.logger = Logger(f"Effect")
        self.logger.info(f"Effect initialized to affect attribute: {self.attribute}")

    def apply(self, target, **kwargs):
        """
        Apply the effect to the target character.

        Args:
            target (BaseCharacter): The character to apply the effect to.
            **kwargs: Additional context variables that can be used in the formula.
        """
        if not self.attribute:
            self.logger.warning(f"No attribute specified in effect: {self}")
            return

        # Evaluate the formula to calculate the amount
        amount = self._calculate_amount(target, **kwargs)

        # Modify the target's attribute
        target.stats.modify(self.attribute, amount)
        self.logger.info(f"{target.name}'s {self.attribute} changed by {amount}. New value: {target.stats.get(self.attribute)}")

    def unapply(self, target, **kwargs):
        """
        Reverse the effect applied to the target character.

        Args:
            target (BaseCharacter): The character to reverse the effect on.
            **kwargs: Additional context variables that can be used in the formula.
        """
        if not self.attribute:
            self.logger.warning(f"No attribute specified in effect: {self}")
            return

        # Evaluate the formula to calculate the amount to reverse
        amount = self._calculate_amount(target, **kwargs)

        # Reverse the modification of the target's attribute
        target.stats.modify(self.attribute, -amount)
        self.logger.info(f"{target.name}'s {self.attribute} reversed by {amount}. New value: {target.stats.get(self.attribute)}")

    def _calculate_amount(self, target, **kwargs):
        """
        Calculate the amount of change using the formula.

        Args:
            target (BaseCharacter): The character to apply the effect to.
            **kwargs: Additional context variables that can be used in the formula.

        Returns:
            float: The calculated amount.
        """
        # Prepare the context for evaluating the formula
        context = {
            'target': target,
            'attribute': self.attribute
        }
        context.update(kwargs)

        # Evaluate the formula to calculate the amount
        amount = self.formula.calculate(**context)

        return amount

    def __str__(self):
        """
        String representation of the effect.

        Returns:
            str: A string describing the effect.
        """
        return f"Effect({self.attribute}, {self.formula})"

