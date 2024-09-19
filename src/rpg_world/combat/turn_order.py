class TurnOrder:
    def __init__(self, participants, turn_order_formula):
        """
        Initialize the TurnOrder class with a list of participants.

        Args:
            participants (list): List of characters (player and enemy) in the battle.
        """
        self.participants = participants
        self.turn_order_formula = turn_order_formula
        self.turn_queue = self.calculate_turn_order()

    def calculate_turn_order(self):
        """
        Calculates the turn order based on the provided turn order formula.

        Returns:
            list: A sorted list of characters by their turn order.
        """
        return self.turn_order_formula(self.participants).calculate()

    def get_next_turn(self):
        """
        Returns the next character in the turn order.

        Returns:
            Character: The character whose turn it is next.
        """
        character = self.turn_queue.pop(0)
        if len(self.turn_queue) == 0:
            self.turn_queue = self.calculate_turn_order()  # Recalculate if queue is empty
        return character
