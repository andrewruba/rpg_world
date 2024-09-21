class TurnOrder:
    def __init__(self, participants, turn_order_formula):
        """
        Initialize the TurnOrder class with a list of participants and a formula for calculating turn order.

        Args:
            participants (list): A list of characters (both player and enemy) participating in the battle.
            turn_order_formula (function): A function or callable object that calculates the turn order based on the participants.
        """
        self.participants = participants
        self.turn_order_formula = turn_order_formula
        self.turn_queue = self.calculate_turn_order()

    def calculate_turn_order(self):
        """
        Calculates the turn order based on the provided turn order formula. This method
        applies the turn order formula to the list of participants to generate a sorted list.

        Returns:
            list: A sorted list of characters based on the turn order formula.
        """
        return self.turn_order_formula(self.participants).calculate()

    def get_next_turn(self):
        """
        Returns the next character in the turn order and recalculates the turn order if the queue is empty.

        Returns:
            Character: The character whose turn it is next to act in the battle.
        """
        character = self.turn_queue.pop(0)
        if len(self.turn_queue) == 0:
            self.turn_queue = self.calculate_turn_order()  # Recalculate if the queue is empty
        return character
