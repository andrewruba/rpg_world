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

        # Prepare the context for evaluating the formula
        context = {
            'target': target
        }
        context.update(kwargs)

        # Evaluate the formula to calculate the amount
        amount = self.formula.calculate(**context)

        # Modify the target's attribute
        target.stats.modify(self.attribute, amount)
        self.logger.info(f"{target.name}'s {self.attribute} changed by {amount}. New value: {target.stats.get(self.attribute)}")

        # Update alive status if health changes
        if self.attribute == 'health' and not target.is_alive():
            self.logger.info(f"{target.name} is dead.")

    def __str__(self):
        """
        String representation of the effect.

        Returns:
            str: A string describing the effect.
        """
        return f"Effect({self.attribute}, {self.formula})"
