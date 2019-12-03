# Copylight(c) 2019 NakagamiYuta
# LICENCE : MIT

from random import randint
from copy import deepcopy
from simulator.common import gen_2d_list, transpositon_2d_list


# Generate Board Options
LINE_SYMMETRY_HALF = 0
LINE_SYMMETRY_QUARTER = 1
POINT_SYMMETRY_HALF = 2


# Public
class Board:
    def __init__(self, width, height, points, tiled):
        self.width = width
        self.height = height
        self.points = points
        self.tiled = tiled


    def __str__(self):
        points_str = "\n".join([str(elem) for elem in self.points])
        tiled_str = "\n".join([str(elem) for elem in self.tiled])
        return  "--Points--\n" + points_str + "\n\n" +\
                "--Tiled--\n" + tiled_str + "\n"
