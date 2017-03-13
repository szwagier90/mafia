#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.mafia import Game
from src.player import Player

from mock import Mock, MagicMock

class TestMafiaGame(unittest.TestCase):
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

        game = Game(
            name="NewGame",
            players=[
                player1mock,
                player2mock,
            ],
        )

        self.assertFalse(game.active)

        game.new_game(shuffle=random_mock.shuffle)
        random_mock.shuffle.assert_called_once()
        self.assertTrue(game.active)

if __name__ == '__main__':
    unittest.main()
