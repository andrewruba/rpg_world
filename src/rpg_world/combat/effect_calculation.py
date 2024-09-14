class EffectCalculation:
    def __init__(self, spell, caster, target):
        """
        Initialize the effect calculation with a spell, caster, and target.

        Args:
            spell (Spell): The spell being cast.
            caster (BaseCharacter): The character casting the spell.
            target (BaseCharacter): The character receiving the effect of the spell.
        """
        self.spell = spell
        self.caster = caster
        self.target = target

    def apply_effects(self):
        """
        Apply the spell's effects to the target's attributes.

        The effects are calculated based on the formulas provided in the spell's effects list.
        """
        effects = self.spell.get_attribute('effects')
        if not effects:
            print(f"No effects to apply for spell '{self.spell.name}'.")
            return

        for effect in effects:
            attribute = effect.get('attribute')
            formula = effect.get('formula')

            # Prepare the context for evaluating the formula
            context = {
                'caster_attributes': self.caster.attributes,
                'target_attributes': self.target.attributes,
                'caster': self.caster,
                'target': self.target,
                'spell_attributes': self.spell.attributes,
                # Include any other variables needed in the formula
            }

            # Evaluate the formula to calculate the amount
            amount = self.evaluate_formula(formula, context)

            # Create the effect dictionary and process it
            effect_dict = {'attribute': attribute, 'amount': amount}
            self.target.process_effect(effect_dict)
            print(f"Applied effect on {self.target.name}: {attribute} changed by {amount}.")

    def evaluate_formula(self, formula, context):
        """
        Evaluate the formula string using the provided context.

        Args:
            formula (str): The formula to evaluate.
            context (dict): A dictionary containing variables used in the formula.

        Returns:
            The result of the evaluated formula.
        """
        # Use eval in a safe way
        allowed_names = {
            'min': min,
            'max': max,
            'abs': abs,
            # Include any other safe built-in functions if needed
        }

        # Combine allowed names and context
        safe_dict = {**allowed_names, **context}

        try:
            result = eval(formula, {"__builtins__": None}, safe_dict)
        except Exception as e:
            print(f"Error evaluating formula '{formula}': {e}")
            result = 0

        return result
