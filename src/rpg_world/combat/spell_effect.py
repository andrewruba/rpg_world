from .base_effect import BaseEffect

class SpellEffect(BaseEffect):
    """
    Represents a spell effect that can be applied to a character.
    """

    def __init__(self, attribute: str, formula, recipient: str = 'target'):
        """
        Initialize the SpellEffect with an attribute, a formula function, and a recipient.

        Args:
            attribute (str): The name of the attribute to affect.
            formula (callable): A function to calculate the change in attribute value.
                                It should accept context variables as keyword arguments.
            recipient (str): Who receives the effect ('target' or 'caster'). Defaults to 'target'.
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
            print(f"No attribute specified in effect: {self}")
            return

        # Determine the recipient of the effect
        recipient = caster if self.recipient == 'caster' else target

        # Prepare the context for evaluating the formula
        context = {
            'caster': caster,
            'target': target,
            'recipient': recipient
        }
        context.update(kwargs)

        # Evaluate the formula to calculate the amount
        amount = self.formula(**context)

        # Modify the recipient's attribute
        recipient.stats.modify(self.attribute, amount)
        print(f"{recipient.name}'s {self.attribute} changed by {amount}. New value: {recipient.get_attribute(self.attribute)}")

        # Update alive status if health changes
        if self.attribute == 'health' and not recipient.is_alive():
            print(f"{recipient.name} is dead.")

    def __str__(self):
        """
        String representation of the spell effect.

        Returns:
            str: A string describing the spell effect.
        """
        return f"SpellEffect({self.attribute}, {self.formula}, recipient='{self.recipient}')"
