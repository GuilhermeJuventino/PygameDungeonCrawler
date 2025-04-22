import pygame


class Dungeon:
    def __init__(self):
        self.side_walls = []
        self.front_walls = []
        self.corner_walls = []
        self.side_front_walls = []

        self.map = [
            [1, 1, 1],
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

        for i in range(2, -1, -1):
            if i > len(self.map):
                break

            if self.map[i][0] == 1:
                if i == 1:
                    if self.map[i + 1][0] == 0:
                        self.surface.blit(
                            self.corner_walls[counter], (offset, 0))
                    else:
                        self.surface.blit(
                            self.side_walls[counter], (offset, 0))
                elif i == 2:
                    if self.map[i - 1][0] == 0:
                        self.surface.blit(
                            self.corner_walls[counter], (offset, 0))
                    elif self.map[i - 1][0] == 1 and self.map[i][1] == 1:
                        self.surface.blit(
                            self.corner_walls[counter], (offset, 0))
                    else:
                        self.surface.blit(
                            self.side_walls[counter], (offset, 0))
                elif i == 0:
                    if self.map[i + 1][0] == 0:
                        self.surface.blit(
                            self.corner_walls[counter], (offset, 0))
                    else:
                        self.surface.blit(
                            self.side_walls[counter], (offset, 0))

            if self.map[i][1] == 1:
                break

            offset += 16
            counter += 1

    def draw_right_wall(self, surface):
        # Offset X position between each segment of the wall
        offset = 0

        # Index counter for the walls list, important due to the
        # reverse for loop, as i will be inverted because of it.
        counter = 0

        for i in range(2, -1, -1):
            if i > len(self.map):
                break

            if self.map[i][2] == 1:
                if i == 1:
                    if self.map[i + 1][2] == 0:
                        self.surface.blit(
                            pygame.transform.flip(self.corner_walls[counter], True, False), (128 - offset, 0))
                    else:
                        self.surface.blit(
                            pygame.transform.flip(self.side_walls[counter], True, False), (128 - offset, 0))
                elif i == 2:
                    if self.map[i - 1][2] == 0:
                        self.surface.blit(
                            pygame.transform.flip(self.corner_walls[counter], True, False), (128 - offset, 0))
                    elif self.map[i - 1][2] == 1 and self.map[i][1] == 1:
                        self.surface.blit(
                            pygame.transform.flip(self.corner_walls[counter], True, False), (128 - offset, 0))
                    else:
                        self.surface.blit(
                            pygame.transform.flip(self.side_walls[counter], True, False), (128 - offset, 0))
                elif i == 0:
                    if self.map[i + 1][2] == 0:
                        self.surface.blit(
                            pygame.transform.flip(self.corner_walls[counter], True, False), (128 - offset, 0))
                    else:
                        self.surface.blit(
                            pygame.transform.flip(self.side_walls[counter], True, False), (128 - offset, 0))

            if self.map[i][1] == 1:
                break

            offset += 16
            counter += 1

    def draw_center_wall(self, surface):
        offset = 0
        counter = 0

        for i in range(2, -1, -1):
            if self.map[i][1] == 1:
                self.surface.blit(self.front_walls[counter], (16 + offset, 0))
                break

            offset += 16
            counter += 1

    def get_draw_matrix(self):
        draw_matrix = [
            [],
            [],
            []
        ]

        for i in range(0, 3):
            for j in range(0, 3):
                if i > len(self.map) or j > len(self.map[i]):
                    break

                draw_matrix[i].append(self.map[i][j])

        return draw_matrix

    def draw_walls(self, surface):
        draw_matrix = self.get_draw_matrix()
        offset = 32

        index_to_draw_left = 0
        index_to_draw_right = 0
        index_to_draw_center = 0

        for i in range(0, 3):
            if i > len(draw_matrix) + 1:
                break

            if draw_matrix[i][1] == 1:
                index_to_draw_center = i

            if draw_matrix[i][0] == 1:
                index_to_draw_left == i

            if draw_matrix[i][2] == 1:
                index_to_draw_right == i

        # draw center wall
        self.surface.blit(self.front_walls[index_to_draw_center], (64, 0))

        # draw left wall
        for i in range(0, index_to_draw_left):
            if i > len(draw_matrix):
                break

            if draw_matrix[i][0] == 1:
                if i > index_to_draw_center:
                    continue

                self.surface.blit(self.side_walls[i](offset, 0))
                offset -= 16
            elif draw_matrix[i][0] == 0:
                if draw_matrix[i][1] == 1 or i > 0 and draw_matrix[i-1][0] == 1:
                    self.surface.blit(self.corner_walls[i], (offset, 0))
                    offset -= 16

        offset = 32

    def draw(self, surface):
        self.surface = surface

        self.draw_center_wall(self.surface)
        self.draw_left_wall(self.surface)
        self.draw_right_wall(self.surface)
        # self.draw_walls(self.surface)

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
