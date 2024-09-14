from ..character.base_character import BaseCharacter
from ..ability.base_ability import BaseAbility

class EffectCalculation:
    def __init__(self, ability: BaseAbility, caster: BaseCharacter, target: BaseCharacter):
        """
        Initialize the effect calculation with an ability, caster, and target.

        Args:
            ability (BaseAbility): The ability being used.
            caster (BaseCharacter): The character using the ability.
            target (BaseCharacter): The character receiving the effect of the ability.
        """
        self.ability = ability
        self.caster = caster
        self.target = target

    def apply_effects(self):
        """
        Apply the ability's effects to the target's attributes.

        The effects are calculated based on the formulas provided in the ability's effects list.
        """
        effects = self.ability.get_attribute('effects')
        if not effects:
            print(f"No effects to apply for ability '{self.ability.name}'.")
            return

        for effect in effects:
            attribute = effect.get('attribute')
            formula = effect.get('formula')

            if not attribute or not formula:
                print(f"Invalid effect definition in ability '{self.ability.name}': {effect}")
                continue

            # Prepare the context for evaluating the formula
            context = {
                'caster_stats': self.caster.stats.attributes,
                'target_stats': self.target.stats.attributes,
                'ability_attributes': self.ability.attributes,
            }

            # Evaluate the formula to calculate the amount
            amount = self.evaluate_formula(formula, context)

            # Create the effect dictionary and process it
            effect_dict = {'attribute': attribute, 'amount': amount}
            self.target.process_effect(effect_dict)
            print(f"Applied effect on {self.target.name}: {attribute} changed by {amount}.")

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
