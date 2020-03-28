from constants import *
import pygame
import math

class Maze:
    def __init__(self):

        self.mul = int(math.sqrt(len(MAZE_TILES)))
        self.rows = self.mul
        self.cols = self.mul


    def update(self):
        pass

    def draw(self, surface):
        for c in range(self.cols):

            for r in range(self.rows):

                pos = (r * BLOCK_SIZE , c * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

                if MAZE_TILES[c * self.mul + r] == 0:
                    pygame.draw.rect(surface, BLACK, pos)
                if MAZE_TILES[c * self.mul + r] == 1:
                    pygame.draw.rect(surface, WHITE, pos)
                if MAZE_TILES[c * self.mul + r] == 2:
                    pygame.draw.rect(surface, GREEN, pos)
                if MAZE_TILES[c * self.mul + r] == 3:
                    pygame.draw.rect(surface, RED, pos)
