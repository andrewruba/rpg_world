import random

class TurnOrder:
    def __init__(self, participants):
        """
        Initialize the TurnOrder class with a list of participants.

        Args:
            participants (list): List of characters (player and enemy) in the battle.
        """
        self.participants = participants
        self.turn_queue = self.calculate_turn_order()

    def calculate_turn_order(self):
        """
        Calculates the turn order based on character agility or speed stats.

        Returns:
            list: A sorted list of characters by their turn order.
        """
        return sorted(self.participants, key=lambda char: char.get_attribute('speed'), reverse=True)

    def get_next_turn(self):
        """
        Returns the next character in the turn order.

        Returns:
            BaseCharacter: The character whose turn it is next.
        """
        character = self.turn_queue.pop(0)
        self.turn_queue.append(character)  # Rotate turn order
        return character
