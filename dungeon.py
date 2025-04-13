import pygame


class Dungeon:
    def __init__(self):
        self.side_walls = []
        self.front_walls = []
        self.corner_walls = []
        self.side_front_walls = []

    def load_graphics(self):
        self.side_walls = [
            pygame.image.load("Walls/SideWall1.png").convert_alpha(),
            pygame.image.load("Walls/SideWall2.png").convert_alpha(),
            pygame.image.load("Walls/SideWall3.png").convert_alpha()
        ]

        self.front_walls = [
            pygame.image.load("Walls/FrontWall1.png").convert_alpha(),
            pygame.image.load("Walls/FrontWall2.png").convert_alpha(),
            pygame.image.load("Walls/FrontWall3.png").convert_alpha()
        ]

        self.corner_walls = [
            pygame.image.load("Walls/CornerWall1.png").convert_alpha(),
            pygame.image.load("Walls/CornerWall2.png").convert_alpha(),
            pygame.image.load("Walls/CornerWall3.png").convert_alpha()
        ]

        self.side_front_walls = [
            pygame.image.load("Walls/SideFrontWall1.png").convert_alpha(),
            pygame.image.load("Walls/SideFrontWall2.png").convert_alpha()
        ]

    def update(self):
        pass

    def draw(self, surface):
        self.surface = surface

        self.surface.blit(self.side_walls[0], (0, 0))
        self.surface.blit(self.side_walls[1], (16, 0))
        self.surface.blit(self.side_walls[2], (32, 0))

        self.surface.blit(self.front_walls[2], (50, 0))

        self.surface.blit(pygame.transform.flip(
            self.side_walls[0], True, False), (128, 0))
        self.surface.blit(pygame.transform.flip(
            self.side_walls[1], True, False), (128 - 16, 0))
        self.surface.blit(pygame.transform.flip(
            self.side_walls[2], True, False), (128 - 32, 0))
