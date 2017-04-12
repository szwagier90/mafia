#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from mock import Mock

from src.terminal_game import TerminalGame

from src.io_wrapper import IOWrapper

class TestTerminalGame(unittest.TestCase):
    def test_zero_players_game(self):
        io_mock = Mock(
            name="io",
            spec=IOWrapper,
        )

        io_mock.input.side_effect = [""]
        game = TerminalGame(io=io_mock)
        io_mock.input.assert_called_once_with("Enter game name: ")


if __name__ == '__main__':
    unittest.main()
