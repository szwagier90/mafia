#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.mafia import Game
from src.player import Player

from src.exceptions import *

from mock import Mock, MagicMock

class TestMafiaGame(unittest.TestCase):
    def test_raise_exception_if_empty_players_list(self):
        players = []
        with self.assertRaises(NotEnoughPlayersError):
            game = Game("", players)

    def test_new_game(self):
        random_mock = Mock()
        random_mock.shuffle = MagicMock()

        player1mock = Mock(
            name="Player1",
            spec=Player,
        )
        player2mock = Mock(
            name="Player2",
            spec=Player,
        )
        player3mock = Mock(
            name="Player3",
            spec=Player,
        )

        game = Game(
            name="NewGame",
            players=[
                player1mock,
                player2mock,
                player3mock,
            ],
        )

        self.assertFalse(game.active)

        game.new_game(shuffle=random_mock.shuffle)
        random_mock.shuffle.assert_called_once()
        self.assertTrue(game.active)

        self.assertEqual(game.get_player_to_kill(player1mock), player2mock)
        self.assertEqual(game.get_player_to_kill(player2mock), player3mock)
        self.assertEqual(game.get_player_to_kill(player3mock), player1mock)

if __name__ == '__main__':
    unittest.main()
