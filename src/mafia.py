#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Game:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.is_started = False

    def set_name(self, new_name):
        self.name = new_name

    def set_players(self, players):
        self.players = players

    def start_game(self):
        self.is_started = True
