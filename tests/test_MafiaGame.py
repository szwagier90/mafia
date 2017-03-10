#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.mafia import Game

from mock import Mock, MagicMock

class TestMafiaGame(unittest.TestCase):
    def test_new_game(self):
        random_mock = Mock()
        random_mock.shuffle = MagicMock()

        game = Game(
            name="NewGame",
            players=["Player1", "Player2"],
        )

        self.assertFalse(game.active)

        game.new_game(shuffle=random_mock.shuffle)
        random_mock.shuffle.assert_called_once()
        self.assertTrue(game.active)

if __name__ == '__main__':
    unittest.main()
