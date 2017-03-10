#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.player import Player

class TestPlayer(unittest.TestCase):
    def test_create_player(self):
        player = Player()

if __name__ == '__main__':
    unittest.main()
