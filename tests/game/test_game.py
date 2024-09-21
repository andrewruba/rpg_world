import time
import pytest
from rpg_world import Game

class TestGame:
    
    def test_game_initialization(self, mocker):
        """
        Test game initialization to ensure the game state is set up correctly.
        """
        mock_init_game = mocker.patch.object(Game, 'init_game')
        game = Game(game_state='mock_game_state', target_fps=60, max_run_time=2)
        
        assert game.is_running, "Game should start in running state."
        assert game.target_fps == 60, "Target FPS should be 60."
        assert game.max_run_time == 2, "Max run time should be 2 seconds."
        mock_init_game.assert_called_once(), "init_game should be called during initialization."

    def test_game_run_internal_timer(self, mocker):
        """
        Test that the game runs for the correct duration using the internal timer.
        """
        mocker.patch.object(Game, 'update_game')

        game = Game(game_state='mock_game_state', target_fps=60, max_run_time=1)
        
        start_time = time.time()
        game.run()  # Run the game loop
        end_time = time.time()

        elapsed_time = end_time - start_time

        assert elapsed_time >= 1, f"Game should have run for at least 1 second, but ran for {elapsed_time} seconds."
        assert not game.is_running, "Game should be stopped after run."

    def test_game_run_external_timer(self, mocker):
        """
        Test that the game uses the external timer correctly and runs for the correct duration.
        """
        def mock_external_timer():
            return time.time()

        mocker.patch.object(Game, 'update_game')

        game = Game(game_state='mock_game_state', external_timer=mock_external_timer, target_fps=60, max_run_time=1)
        
        start_time = time.time()
        game.run()
        end_time = time.time()

        elapsed_time = end_time - start_time

        assert elapsed_time >= 1, f"Game should have run for at least 1 second using external timer, but ran for {elapsed_time} seconds."
        assert not game.is_running, "Game should be stopped after run."

    def test_game_updates_state(self, mocker):
        """
        Test that update_game is called with the correct delta time.
        """
        mock_update_game = mocker.patch.object(Game, 'update_game')

        game = Game(game_state='mock_game_state', target_fps=60, max_run_time=1)
        game.run()

        assert mock_update_game.call_count > 0, "update_game should be called at least once during the game loop."
        args, _ = mock_update_game.call_args
        delta_time = args[0]
        assert delta_time > 0, "delta_time should be greater than 0."

    def test_game_stop(self, mocker):
        """
        Test that the game stops running after max_run_time has been reached.
        """
        mocker.patch.object(Game, 'update_game')

        game = Game(game_state='mock_game_state', target_fps=60, max_run_time=1)
        game.run()

        assert not game.is_running, "Game should have stopped after max_run_time was reached."
