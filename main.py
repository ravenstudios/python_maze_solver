from constants import *
import pygame
import maze


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

maze = maze.Maze()

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill(BLUE)#background
    maze.draw(surface)
    pygame.display.flip()



def update():
    maze.update()



if __name__ == "__main__":
    main()
