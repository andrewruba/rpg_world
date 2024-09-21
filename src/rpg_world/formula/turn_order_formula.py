from .formula import Formula

class SimpleFocusTurnOrderFormula(Formula):
    """
    A simple formula that calculates and returns a turn order based on the characters' focus attribute.
    The characters with higher focus will act earlier.

    Args:
        participants (list): List of characters participating in the battle.
    """

    def __init__(self, participants):
        """
        Initialize the formula with the list of participants.

        Args:
            participants (list): A list of characters to calculate the turn order for.
        """
        self.participants = participants

    def calculate(self, **kwargs):
        """
        Calculate the turn order by sorting participants based on their focus attribute.

        Args:
            **kwargs: Additional context variables (not used here).

        Returns:
            list: A list of characters sorted by their focus in descending order.
        """
        return sorted(
            self.participants,
            key=lambda char: char.focus,
            reverse=True
        )
