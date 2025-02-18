from .effect import Effect

class SpellEffect(Effect):
    """
    Represents a spell effect that can be applied to a character. This effect can target either
    the caster or the target, depending on the specified recipient.
    """

    def __init__(self, attribute: str, formula, recipient: str = 'target'):
        """
        Initialize the SpellEffect with an attribute, a formula object, and a recipient.

        Args:
            attribute (str): The name of the attribute to affect (e.g., 'health', 'mana').
            formula (Formula): An instance of Formula used to calculate the change in attribute value.
                               The formula should have a `calculate` method that accepts context variables
                               such as 'target', 'caster', or other relevant data.
            recipient (str): Specifies who receives the effect ('target' or 'caster'). Defaults to 'target'.
        """
        super().__init__(attribute, formula)
        self.recipient = recipient  # 'target' or 'caster'

    def apply(self, caster, target, **kwargs):
        """
        Apply the effect to the recipient character (either the caster or the target).

        Args:
            caster (Character): The character casting the spell.
            target (Character): The character receiving the spell.
            **kwargs: Additional context variables that can be used in the formula.

        Returns:
            None
        """
        if not self.attribute:
            self.logger.warning(f"No attribute specified in effect: {self}")
            return

        # Determine the recipient of the effect (either caster or target)
        recipient = caster if self.recipient == 'caster' else target

        # Calculate the amount to modify the attribute using the formula
        amount = self._calculate_amount(
            target=target,
            caster=caster,
            recipient=recipient,
            **kwargs
        )

        # Modify the recipient's attribute
        recipient.stats.modify(self.attribute, amount)
        self.logger.info(f"{recipient.name}'s {self.attribute} changed by {amount}. New value: {recipient.stats.get(self.attribute)}")

    def __str__(self):
        """
        Return a string representation of the spell effect.

        Returns:
            str: A string describing the spell effect, including the attribute and recipient.
        """
        return f"SpellEffect({self.attribute}, {self.formula}, recipient='{self.recipient}')"
