from .formula import Formula

class SimpleFocusTurnOrderFormula(Formula):
    """
    A simple formula that returns a sorted turn order based on focus.
    """
    def __init__(self, participants):
        self.participants = participants

    def calculate(self, **kwargs):
        return sorted(
            self.participants,
            key=lambda char: char.focus,
            reverse=True
        )
