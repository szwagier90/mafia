#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Game:
    def __init__(self, name):
        self.name = name
        self.players = []

    def set_name(self, new_name):
        self.name = new_name
