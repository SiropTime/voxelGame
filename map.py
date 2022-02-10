from typing import List, Any

from settings import *
from random import randint

_ = False
# matrix_map = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, 1],
#     [1, _, 2, 2, _, _, _, _, _, 2, 2, 2, _, _, _, 3, _, _, _, _, 4, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, _, 3, _, _, _, _, _, _, 1],
#     [1, _, 2, 2, _, _, _, _, _, _, _, _, 2, _, 4, _, _, 3, _, _, _, 4, _, 1],
#     [1, _, _, _, _, _, 4, _, _, 2, 2, _, 2, _, _, _, _, _, _, 4, _, _, _, 1],
#     [1, _, 3, _, _, _, 2, _, _, 2, _, _, 2, _, _, _, 4, _, _, _, _, 4, _, 1],
#     [1, _, _, 3, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, 3, _, _, _, _, _, _, _, 3, _, _, 3, 3, _, _, _, _, 3, 3, _, _, 1],
#     [1, _, 3, _, _, _, 3, 3, _, 3, _, _, _, 3, 3, _, _, _, _, 2, 3, _, _, 1],
#     [1, _, _, _, _, 3, _, 3, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, 4, _, 3, _, _, _, _, 3, _, _, 2, _, _, _, _, _, _, _, _, 2, _, 1],
#     [1, _, _, _, _, _, 4, _, _, _, _, _, 2, 2, _, _, _, _, _, _, 2, 2, _, 1],
#     [1, _, _, 4, _, _, _, _, 4, _, _, _, _, 2, 2, 2, 2, 2, 2, 2, 2, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]
matrix_map = [[_ for i in range(1025)] for j in range(1025)]
for i in range(512):
    for j in range(512):
        if i == 0 or i == 511:
            matrix_map[i][j] = 1
        elif j == 0 or j == 511:
            matrix_map[i][j] = 1
        else:
            place = randint(2, 20)
            if place >= 10:
                matrix_map[i][j] = _
            else:
                matrix_map[i][j] = place

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = {}
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4
