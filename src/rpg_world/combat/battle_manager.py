class BattleManager:
    def __init__(self, player_party, enemy_party):
        """
        Initialize the BattleManager with the player's party and the enemy's party.

        Args:
            player_party (list): List of player characters.
            enemy_party (list): List of enemy characters.
        """
        self.player_party = player_party
        self.enemy_party = enemy_party
        self.turn_order = None
        self.battle_state = None

    def start_battle(self):
        """
        Starts the battle by initializing the turn order and battle state.
        """
        self.turn_order = TurnOrder(self.player_party + self.enemy_party)
        print("Battle started!")

    def execute_turn(self):
        """
        Executes a single turn in the battle.
        """
        current_character = self.turn_order.get_next_turn()
        if current_character.is_alive():
            action = current_character.choose_action(self.battle_state)
            action.execute()

    def check_battle_outcome(self):
        """
        Checks if the battle is over by evaluating the health of all parties.
        """
        if all(not char.is_alive() for char in self.enemy_party):
            return "Player Wins!"
        elif all(not char.is_alive() for char in self.player_party):
            return "Enemy Wins!"
        return "Battle is ongoing."

    def run_battle(self):
        """
        Runs the full battle loop, iterating through turns until a win condition is met.
        """
        self.start_battle()
        while self.check_battle_outcome() == "Battle is ongoing.":
            self.execute_turn()

        print(self.check_battle_outcome())
