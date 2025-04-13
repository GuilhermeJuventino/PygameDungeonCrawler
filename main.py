# Example file showing a basic pygame "game loop"
import pygame

from dungeon import Dungeon

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

game_window = pygame.Surface((144, 128))

"""
side_walls = [
    pygame.image.load("Walls/SideWall1.png").convert_alpha(),
    pygame.image.load("Walls/SideWall2.png").convert_alpha(),
    pygame.image.load("Walls/SideWall3.png").convert_alpha()
]

front_walls = [
    pygame.image.load("Walls/FrontWall1.png").convert_alpha(),
    pygame.image.load("Walls/FrontWall2.png").convert_alpha(),
    pygame.image.load("Walls/FrontWall3.png").convert_alpha()
]
"""

dungeon = Dungeon()
dungeon.load_graphics()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    game_window.fill("black")

    # RENDER YOUR GAME HERE
    """
    game_window.blit(side_walls[0], (0, 0))
    game_window.blit(side_walls[1], (16, 0))
    game_window.blit(side_walls[2], (32, 0))

    game_window.blit(front_walls[2], (50, 0))

    game_window.blit(pygame.transform.flip(
        side_walls[0], True, False), (128, 0))
    game_window.blit(pygame.transform.flip(
        side_walls[1], True, False), (128 - 16, 0))
    game_window.blit(pygame.transform.flip(
        side_walls[2], True, False), (128 - 32, 0))
    """

    dungeon.draw(game_window)

    scaled_window = pygame.transform.scale_by(game_window, 4)

    screen.blit(scaled_window, (0, 0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
