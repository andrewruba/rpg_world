from .turn_order import TurnOrder
from ..utils.logger import Logger

class BattleManager:
    def __init__(self, player_party, enemy_party, turn_order_formula):
        """
        Initialize the BattleManager with the player's party and the enemy's party.

        Args:
            player_party (list): List of player characters.
            enemy_party (list): List of enemy characters.
        """
        self.player_party = player_party
        self.enemy_party = enemy_party
        self.turn_order = None
        self.turn_order_formula = turn_order_formula
        self.logger = Logger("BattleManager")

    def start_battle(self):
        """
        Starts the battle by initializing the turn order and battle state.
        """
        self.turn_order = TurnOrder(self.player_party + self.enemy_party, self.turn_order_formula)
        self.logger.info("Battle started!")

    def get_next_turn(self):
        """
        Executes a single turn in the battle.
        """
        return self.turn_order.get_next_turn()

    def check_battle_outcome(self):
        """
        Checks if the battle is over by evaluating the health of all parties.
        """
        if all(not char.is_alive() for char in self.enemy_party):
            self.logger.info("Player Wins!")
            return self.player_party
        elif all(not char.is_alive() for char in self.player_party):
            self.logger.info("Enemy Wins!")
            return self.enemy_party
        return None
