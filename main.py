import sys
import pygame
import math

from pygame.locals import *
from settings import *
from sprite_objects import *

from drawing import Drawing
from player import Player
from map import world_map
from raycasting import ray_casting


class App:
    def __init__(self):
        pygame.init()
        self.sc = pygame.display.set_mode(SCREEN_SIZE)
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Voxel RC Training")
        pygame.display.toggle_fullscreen()
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        pygame.mixer.music.load("assets/music/forYou.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=6, fade_ms=3)

        self.sprites = Sprites()
        self.player = Player()
        self.drawing = Drawing(self.sc)

    def main(self):
        while True:
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit(0)
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        sys.exit(0)
            self.update()

    def gen_map(self):
        pass

    def update(self):
        self.player.movement()

        self.sc.fill(BLACK)

        self.drawing.background(self.player.angle)
        # self.drawing.world(self.player.pos, self.player.angle)
        walls = ray_casting(self.player, self.drawing.textures)
        self.drawing.world(walls + [obj.object_locate(self.player) for obj in self.sprites.list_of_objects])
        self.drawing.fps(self.clock)
        pygame.display.flip()
        self.clock.tick(60)


if __name__ == '__main__':
    print("Made by KlenoviySirop. Timofey Maltsev 2021")
    app = App()
    app.main()