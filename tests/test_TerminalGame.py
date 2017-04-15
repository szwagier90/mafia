#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from mock import Mock

from src.terminal_game import TerminalGame
from src.io_wrapper import IOWrapper

from src.exceptions import *

from src.io_wrapper import IOWrapper

class TestTerminalGame(unittest.TestCase):
    def test_zero_players_game(self):
        io_mock = Mock(
            name="io",
            spec=IOWrapper,
        )

        io_mock.input.side_effect = ["", 0]

        game = TerminalGame(io=io_mock)
        io_mock.input.assert_called()
        self.assertEquals(io_mock.input.call_count, 2)
        io_mock.output.assert_called_once_with("Not enough players to play this game")


if __name__ == '__main__':
    unittest.main()
