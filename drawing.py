import math

import pygame
from settings import *
from raycasting import ray_casting


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {1: pygame.image.load("assets/textures/Cobble_Wall.png").convert(),
                         2: pygame.image.load("assets/textures/Brick_0.png").convert(),
                         3: pygame.image.load('assets/textures/Wood_0.png').convert(),
                         4: pygame.image.load('assets/textures/Cobble.png').convert(),
                         5: pygame.image.load('assets/textures/Cobble_Ceiling.png').convert(),
                         6: pygame.transform.scale(pygame.image.load('assets/textures/Brick_1.png'),
                                                     (128, 128)).convert(),
                         7: pygame.transform.scale(pygame.image.load('assets/textures/Metal_Plate.png'),
                                                     (128, 128)).convert(),
                         8: pygame.transform.scale(pygame.image.load('assets/textures/Tile.png'),
                                                     (128, 128)).convert(),
                         9: pygame.transform.scale(pygame.image.load('assets/textures/Dead_Ground.png'),
                                                     (128, 128)).convert(),
                         'S': pygame.transform.scale(pygame.image.load('assets/textures/sky.png'),
                                                     (1510, 880)).convert(),
                         'F': pygame.transform.scale(pygame.image.load('assets/textures/far-grounds.png'),
                                                     (1332, 220)).convert_alpha(),
                         'G': pygame.transform.scale(pygame.image.load('assets/textures/colorstone.png'),
                                                     (128, 128)).convert()
                         }

    def background(self, angle):
        sky_offset = -5 * math.degrees(angle) % WIDTH

        # SKY
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))

        # FAR LANDS
        self.sc.blit(self.textures['F'], (sky_offset, 100))
        self.sc.blit(self.textures['F'], (sky_offset - WIDTH, 100))
        self.sc.blit(self.textures['F'], (sky_offset + WIDTH, 100))

        # GROUND
        pygame.draw.rect(self.sc, DARK_GREY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps(self, clock):
        display_fps = int(clock.get_fps())
        render = self.font.render(str(display_fps), 0, RED)
        self.sc.blit(render, FPS_POS)