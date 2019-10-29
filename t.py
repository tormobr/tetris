import pygame

class T:
    def __init__(self):
        self.size = 50
        self.height = 0
        self. width = 5
        self.position = [[0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0]]
        self.rects = [pygame.Rect(3*self.size, 1*self.size, self.size, self.size),
                     pygame.Rect(4*self.size, 1*self.size, self.size, self.size),
                     pygame.Rect(5*self.size, 1*self.size, self.size, self.size),
                     pygame.Rect(4*self.size, 0*self.size, self.size, self.size)]
        self.color = (255, 0, 0)

    def move(self, x, y):
        for i in range(len(self.rects)):
            self.rects[i].top += y*self.size

        for i in range(len(self.rects)):
            self.rects[i].left += x*self.size
    

    def rotate(self):
        pass

