
import pygame

pygame.init()

class game:

    def __init__(self):
        self.block_size = 50
        self.screen_width = 10 * self.block_size
        self.screen_height = 20 * self.block_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.done = False

        self.grid = [[0 for i in range(self.screen_width // self.block_size)]
                    for j in range(self.screen_height // self.block_size)]
        self.X_image = pygame.image.load("images/X.png")
        print(self.grid)
        
    
    def display_background(self, x, y):
        self.screen.blit(pygame.transform.scale(self.X_image, (20, 20)), (x, y))

    def play(self):
        while not self.done:
            for i in range(10):
                for j in range(20):
                    self.display_background(i*self.block_size, j*self.block_size)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                
                pygame.display.flip()

if __name__ == "__main__":
    g = game()
    g.play()
