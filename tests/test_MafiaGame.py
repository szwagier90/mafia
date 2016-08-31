#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.mafia import Game


class TestMafiaGame(unittest.TestCase):

    def test_new_game(self):
        game = Game()

if __name__ == '__main__':
    unittest.main()
