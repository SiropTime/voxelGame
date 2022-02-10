import math

import pygame
from settings import *
from collections import deque

class Sprites:
    def __init__(self):
        self.sprite_parameters = {
            'sprite_barrel': {
                'sprite': pygame.image.load('assets/sprites/items/barrel.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': 0.4,
                'animation': deque(
                    [pygame.image.load('assets/sprites/items/barrel.png').convert_alpha() for i in range(12)]),
                'animation_dist': 600,
                'animation_speed': 10,
            }
        }

        self.list_of_objects = [
            SpriteObect(self.sprite_parameters['sprite_barrel'], (7.1, 2.1)),
            SpriteObect(self.sprite_parameters['sprite_barrel'], (5.9, 2.1)),
            # SpriteObect(self.sprite_types['pedestal'], True, (8.8, 2.5), 1.6, 0.5),
            # SpriteObect(self.sprite_types['pedestal'], True, (8.8, 5.6), 1.6, 0.5)
        ]


class SpriteObect:
    def __init__(self, parameters, pos):
        self.object = parameters['sprite']
        self.viewing_angles = parameters['viewing_angles']
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation']
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.animation_count = 0

        if self.viewing_angles:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_locate(self, player):
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and distance_to_sprite > 30:
            proj_height = min(int(PROJ_COEFF / distance_to_sprite * self.scale), DOUBLE_HEIGHT)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            if self.viewing_angles:
                if theta < 0:
                    theta += DOUBLE_PI
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break
            # ANIMATION
            sprite_object = self.object
            if self.animation and distance_to_sprite < self.animation_dist:
                sprite_object = self.animation[0]
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1
                else:
                    self.animation.rotate()
                    self.animation_count = 0
            sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return (distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)









