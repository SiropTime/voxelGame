from settings import *
from pygame.locals import *
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.speed = player_speed
        self.angle_speed = player_angle_speed
        self.sensitivity = 0.003
        self.speed_boost = 3

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.angle %= DOUBLE_PI

    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.x += self.speed * cos_a
            self.y += self.speed * sin_a
        elif keys[K_s]:
            self.x += -self.speed * cos_a
            self.y += -self.speed * sin_a
        if keys[K_a]:
            self.x += self.speed * sin_a
            self.y += -self.speed * cos_a
        elif keys[K_d]:
            self.x += -self.speed * sin_a
            self.y += self.speed * cos_a

        if keys[K_LEFT]:
            self.angle -= self.angle_speed
        elif keys[K_RIGHT]:
            self.angle += self.angle_speed



    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity