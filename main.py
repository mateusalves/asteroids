# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        '''
            1. Check for player inputs
            2. Update the game world
            3. Draw the game to the screen
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        screen.fill(000)
        pygame.display.flip()

