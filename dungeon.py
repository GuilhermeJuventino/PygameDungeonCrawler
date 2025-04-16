import pygame


class Dungeon:
    def __init__(self):
        self.side_walls = []
        self.front_walls = []
        self.corner_walls = []
        self.side_front_walls = []

        self.map = [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1]
        ]

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

    def draw_left_wall(self, surface):
        # Offset X position between each segment of the wall
        offset = 0

        # Index counter for the walls list, important due to the
        # reverse for loop, as i will be inverted because of it.
        counter = 0

        # Starting from the top of the map to the bottom,
        # for every point in the map
        # Check if it's 1, if so,
        # draw appropriate side wall sprite based on counter index
        # Else, if 0, check if any of the adjacent points are 1,
        # if so draw corner wall in that position
        # Else, draw nothing.
        for i in range(2, -1, -1):
            if i > len(self.map) + 1:
                break

            if self.map[i][0] == 0:
                if self.map[i - 1][0] == 1 or self.map[i][1] == 1:
                    surface.blit(self.corner_walls[counter], (offset, 0))
            elif self.map[i][0] == 1:
                surface.blit(self.side_walls[counter], (offset, 0))

            offset += 16
            counter += 1

    def draw(self, surface):
        self.surface = surface

        self.draw_left_wall(self.surface)

        """
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
        """
