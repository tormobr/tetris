import pygame
import random

COLORS = [(255, 0, 0) , (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]

class T:
    def __init__(self, ID):
        self.ID = ID
        self.size = 50
        self.height = 0
        self.width = 5
        self.current_rotation = 0
        self.rotations = [[[1,-1], [1, 1], [-1, 1], [-1, -1]],
                        [[0,0], [0, 0], [0, 0], [0,0]],
                        [[-1, 1], [-1, -1], [1, -1], [1, 1]],
                        [[1,1], [-1, 1], [-1, -1], [1, -1]]]

        self.position = [[0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0]]
        self.rects = [pygame.Rect(3, 1, self.size, self.size),
                     pygame.Rect(4, 1, self.size, self.size),
                     pygame.Rect(5, 1, self.size, self.size),
                     pygame.Rect(4, 0, self.size, self.size)]
        self.color = random.choice(COLORS)
    def move(self, x, y):
        for i in range(len(self.rects)):
            self.rects[i].top += y

        for i in range(len(self.rects)):
            self.rects[i].left += x
    

    def rotate(self):
        for i in range(len(self.rects)):
            self.rects[i].left += self.rotations[i][self.current_rotation][0]
            self.rects[i].top += self.rotations[i][self.current_rotation][1]
        self.current_rotation = (self.current_rotation + 1) % len(self.rotations)
