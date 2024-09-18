from .formula import Formula

class SimpleChangeFormula(Formula):
    """
    A simple formula that returns a fixed change value.
    """
    def __init__(self, value):
        self.value = value

    def calculate(self, **kwargs):
        return self.value

class SimpleChangeFormulaWithStatLimits(Formula):
    """
    A simple formula that returns a fixed change value.
    """
    def __init__(self, value):
        self.value = value

    def calculate(self, **kwargs):
        target = kwargs.get("target")
        attribute = kwargs.get("attribute")
        return self.apply_limits(self.value, target, attribute)

class MultiEffectTargetFormula(Formula):
    """
    A formula that applies an effect based on the target's focus and armor.
    """
    def calculate(self, **kwargs):
        target = kwargs.get("target")
        return -(50 + (target.stats.get("focus") * 0.5)) * (1 - (target.stats.get("armor") / 100.0))


class MultiEffectRecipientFormula(Formula):
    """
    A formula that applies an effect based on the recipient's focus and armor.
    """
    def calculate(self, **kwargs):
        recipient = kwargs.get("recipient")
        return -(50 + (recipient.stats.get("focus") * 0.1)) * (1 - (recipient.stats.get("armor") / 100.0))
