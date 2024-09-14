from abc import ABC

class BaseEffect(ABC):
    """
    Represents an effect that can be applied to a character.
    """

    def __init__(self, attribute: str, formula: str):
        """
        Initialize the BaseEffect with an attribute and formula.

        Args:
            attribute (str): The name of the attribute to affect.
            formula (str): The formula to evaluate and used to calculate the change in attribute value.
        """
        self.attribute = attribute
        self.formula = formula

    def apply(self, ability, caster, target):
        """
        Apply the effect to the target character.

        Args:
            target (BaseCharacter): The character to apply the effect to.
        """
        if not self.attribute:
            print(f"No attribute specified in effect: {self}")
            return

        # Prepare the context for evaluating the formula
        context = {
            'caster_stats': caster.stats.attributes,
            'target_stats': target.stats.attributes,
            'ability_attributes': ability.attributes,
        }

        # Evaluate the formula to calculate the amount
        amount = self.evaluate_formula(self.formula, context)

        # Modify the target's attribute
        target.stats.modify(self.attribute, amount)
        print(f"{target.name}'s {self.attribute} changed by {amount}. New value: {target.get_attribute(self.attribute)}")

        # Update alive status if health changes
        if self.attribute == 'health' and not target.stats.is_alive():
            target.is_alive_flag = False
            print(f"{target.name} has died.")

    def evaluate_formula(self, formula: str, context: dict):
        """
        Evaluate the formula string using the provided context.

        Args:
            formula (str): The formula to evaluate.
            context (dict): A dictionary containing variables used in the formula.

        Returns:
            The result of the evaluated formula.
        """
        # Define allowed built-in functions and safe variables
        allowed_functions = {
            'min': min,
            'max': max,
            'abs': abs,
            'round': round,
            'int': int,
            'float': float,
            # Add any other safe built-in functions as needed
        }

        # Combine allowed functions and safe context
        safe_globals = {"__builtins__": None}
        safe_locals = {**allowed_functions, **context}

        try:
            result = eval(formula, safe_globals, safe_locals)
            return result
        except Exception as e:
            print(f"Error evaluating formula '{formula}': {e}")
            return 0

    def __str__(self):
        """
        String representation of the effect.

        Returns:
            str: A string describing the effect.
        """
        return f"Effect({self.attribute}, {self.amount})"
