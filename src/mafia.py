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
        self.active = True

    def get_player_to_kill(self, killer):
        killer_index = self.players.index(killer)
        return self.players[killer_index+1] if killer_index+1 < len(self.players) else self.players[0]
