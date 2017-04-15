#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.mafia import Game
from src.io_wrapper import IOWrapper

from src.exceptions import *

class TerminalGame():
    def __init__(self, io=IOWrapper):
        self.input = io.input
        self.output = io.output

        game_name = self.input("Enter game name: ")
        number_of_players = self.input("Number of players: ")

        try:
            game = Game(game_name, [])
        except NotEnoughPlayersError:
            self.output("Not enough players to play this game")
