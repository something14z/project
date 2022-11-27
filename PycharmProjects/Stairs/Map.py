import pygame as pg
import sys
from random import randint


class Map():
    def __init__(self, map):
        self.mapup = {}
        self.mapdown = {}

    def generate(self,pos):
        s = []
        s.append(pos)
        l = randint(1, 10)
        s.append(l)
        if pos < 0:
            bg = randint(1, 5)
        else:
            bg = randint(5, 10)
        s.append(bg)
        return s


