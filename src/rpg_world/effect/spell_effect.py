from .base_effect import BaseEffect

class SpellEffect(BaseEffect):
    """
    Represents a spell effect that can be applied to a character.
    """

    def __init__(self, attribute: str, formula, recipient: str = 'target'):
        """
        Initialize the SpellEffect with an attribute, a formula object, and a recipient.

        Args:
            attribute (str): The name of the attribute to affect.
            formula (BaseFormula): An instance of BaseFormula used to calculate the change in attribute value.
                                   It should have a `calculate` method that accepts context variables as keyword arguments.
            recipient (str): Specifies who receives the effect ('target' or 'caster'). Defaults to 'target'.
        """

        super().__init__(attribute, formula)
        self.recipient = recipient  # 'target' or 'caster'

    def apply(self, caster, target, **kwargs):
        """
        Apply the effect to the recipient character (either the caster or the target).

        Args:
            caster (BaseCharacter): The character casting the spell.
            target (BaseCharacter): The character receiving the spell.
            **kwargs: Additional context variables that can be used in the formula.
        """
        if not self.attribute:
            self.logger.warning(f"No attribute specified in effect: {self}")
            return

        # Determine the recipient of the effect
        recipient = caster if self.recipient == 'caster' else target

        # Prepare the context for evaluating the formula
        context = {
            'caster': caster,
            'recipient': recipient
        }
        context.update(kwargs)

        # Evaluate the formula to calculate the amount
        amount = self._calculate_amount(target, **context)

        # Modify the recipient's attribute
        recipient.stats.modify(self.attribute, amount)
        self.logger.info(f"{recipient.name}'s {self.attribute} changed by {amount}. New value: {recipient.stats.get(self.attribute)}")

        # Update alive status if health changes
        if self.attribute == 'health' and not recipient.is_alive():
            self.logger.info(f"{recipient.name} is dead.")

    def __str__(self):
        """
        String representation of the spell effect.

        Returns:
            str: A string describing the spell effect.
        """
        return f"SpellEffect({self.attribute}, {self.formula}, recipient='{self.recipient}')"
