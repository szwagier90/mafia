#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.mafia import Game


class TestMafiaGame(unittest.TestCase):

    def setUp(self):
        self.test_name = 'testname'
        self.game = Game(self.test_name)

    def test_new_game_name_correctyly_set(self):
        self.assertEqual(self.game.name, self.test_name)

    def test_game_name_changed(self):
        changed_name = 'testname2'

        self.game.set_name(changed_name)

        self.assertEqual(self.game.name, changed_name)


if __name__ == '__main__':
    unittest.main()
