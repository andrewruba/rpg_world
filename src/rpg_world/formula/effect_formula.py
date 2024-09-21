from .formula import Formula

class SimpleChangeFormula(Formula):
    """
    A formula that applies a fixed change to an attribute, regardless of any other context.
    """

    def __init__(self, value):
        """
        Initialize the formula with a fixed change value.

        Args:
            value (float): The fixed amount by which the attribute will change.
        """
        self.value = value

    def calculate(self, **kwargs):
        """
        Return the fixed value as the result of the calculation.

        Args:
            **kwargs: Additional context variables (not used in this formula).

        Returns:
            float: The fixed change value.
        """
        return self.value


class SimpleChangeFormulaWithStatLimits(Formula):
    """
    A formula that applies a fixed change to an attribute, but respects min/max limits on that attribute.
    """

    def __init__(self, value):
        """
        Initialize the formula with a fixed change value.

        Args:
            value (float): The fixed amount by which the attribute will change.
        """
        self.value = value

    def calculate(self, **kwargs):
        """
        Calculate the value to be applied, ensuring it adheres to the target's attribute limits.

        Args:
            **kwargs: Must contain 'target' (the character whose attribute is being modified)
                      and 'attribute' (the name of the attribute being modified).

        Returns:
            float: The modified value after applying limits.
        """
        target = kwargs.get("target")
        attribute = kwargs.get("attribute")
        return self.apply_limits(self.value, target, attribute)


class MultiEffectTargetFormula(Formula):
    """
    A formula that calculates an effect value based on the target's focus and armor attributes.
    The more focus the target has, the stronger the effect, while armor reduces the effect.
    """

    def calculate(self, **kwargs):
        """
        Calculate the effect value using the target's focus and armor attributes.

        Args:
            **kwargs: Must contain 'target' (the character receiving the effect).

        Returns:
            float: The calculated effect value.
        """
        target = kwargs.get("target")
        return -(50 + (target.stats.get("focus") * 0.5)) * (1 - (target.stats.get("armor") / 100.0))


class MultiEffectRecipientFormula(Formula):
    """
    A formula that calculates an effect based on the recipient's focus and armor attributes.
    The more focus the recipient has, the stronger the effect, while armor reduces the effect.
    """

    def calculate(self, **kwargs):
        """
        Calculate the effect value using the recipient's focus and armor attributes.

        Args:
            **kwargs: Must contain 'recipient' (the character receiving the effect).

        Returns:
            float: The calculated effect value.
        """
        recipient = kwargs.get("recipient")
        return -(50 + (recipient.stats.get("focus") * 0.1)) * (1 - (recipient.stats.get("armor") / 100.0))
