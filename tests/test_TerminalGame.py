#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.terminal_game import TerminalGame

class TestTerminalGame(unittest.TestCase):
    def test_zero_players_game(self):
        game = TerminalGame()


if __name__ == '__main__':
    unittest.main()
