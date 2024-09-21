from .turn_order import TurnOrder
from ..utils.logger import Logger

class BattleManager:
    def __init__(self, player_party, enemy_party, turn_order_formula):
        """
        Initialize the BattleManager with the player's party and the enemy's party.

        Args:
            player_party (list): A list of characters in the player's party.
            enemy_party (list): A list of characters in the enemy's party.
            turn_order_formula (function): A function or callable object that calculates the turn order based on the participants.
        """
        self.player_party = player_party
        self.enemy_party = enemy_party
        self.turn_order = None
        self.turn_order_formula = turn_order_formula
        self.logger = Logger("BattleManager")

    def start_battle(self):
        """
        Starts the battle by initializing the turn order and setting up the initial battle state.
        It combines the player and enemy parties into a single list and calculates the turn order.
        """
        self.turn_order = TurnOrder(self.player_party + self.enemy_party, self.turn_order_formula)
        self.logger.info("Battle started!")

    def get_next_turn(self):
        """
        Executes a single turn by retrieving the next character in the turn order.
        
        Returns:
            Character: The character whose turn it is to act next in the battle.
        """
        return self.turn_order.get_next_turn()

    def check_battle_outcome(self):
        """
        Checks if the battle has ended by evaluating whether all characters in one party have been defeated.

        Returns:
            list or None: The winning party (player or enemy) if the battle is over, otherwise None.
        """
        if all(not char.is_alive() for char in self.enemy_party):
            self.logger.info("Player Wins!")
            return self.player_party
        elif all(not char.is_alive() for char in self.player_party):
            self.logger.info("Enemy Wins!")
            return self.enemy_party
        return None
