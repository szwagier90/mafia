#!/usr/bin/env python
# -*- coding: utf-8 -*-

class IOWrapper:
    def input(self, text):
        return raw_input(text)
    
    def output(self, text):
        print text
