#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Game:
    def __init__(self, name, players, active=False):
        self.name = name
        self.players = players
        self.active = active

    def new_game(self, shuffle=random.shuffle):
        shuffle(self.players)
