#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.mafia import Game


class TestMafiaGame(unittest.TestCase):

    def test_new_game_name_correctyly_set(self):
        test_name = 'testname'

        self.game = Game(test_name)

        self.assertEqual(self.game.name, test_name)

if __name__ == '__main__':
    unittest.main()
