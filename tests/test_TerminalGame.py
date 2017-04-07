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

        game = TerminalGame(io=io_mock)


if __name__ == '__main__':
    unittest.main()
