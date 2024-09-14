from abc import ABC

class BaseEffect(ABC):
    """
    Represents an effect that can be applied to a character.
    """

    def __init__(self, attribute: str, formula):
        """
        Initialize the BaseEffect with an attribute and a formula function.

        Args:
            attribute (str): The name of the attribute to affect.
            formula (callable): A function to calculate the change in attribute value.
                                It should accept context variables as keyword arguments.
        """
        self.attribute = attribute
        self.formula = formula

    def apply(self, target, **kwargs):
        """
        Apply the effect to the target character.

        Args:
            target (BaseCharacter): The character to apply the effect to.
            **kwargs: Additional context variables that can be used in the formula.
        """
        if not self.attribute:
            print(f"No attribute specified in effect: {self}")
            return

        # Prepare the context for evaluating the formula
        context = {
            'target': target
        }
        context.update(kwargs)

        # Evaluate the formula to calculate the amount
        amount = self.formula(**context)

        # Modify the target's attribute
        target.stats.modify(self.attribute, amount)
        print(f"{target.name}'s {self.attribute} changed by {amount}. New value: {target.get_attribute(self.attribute)}")

        # Update alive status if health changes
        if self.attribute == 'health' and not target.stats.is_alive():
            target.is_alive_flag = False
            print(f"{target.name} has died.")

    def __str__(self):
        """
        String representation of the effect.

        Returns:
            str: A string describing the effect.
        """
        return f"Effect({self.attribute}, {self.formula})"
