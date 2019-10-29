
import pygame
from t import T
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
        self.t = T()
        self.pieces = []
        
    
    def display_background(self, x, y):
        self.screen.blit(pygame.transform.scale(self.X_image, (50, 50)), (x, y))

    def display_pieces(self):
        for piece in self.pieces:
            for rect in piece.rects:
                pygame.draw.rect(self.screen, piece.color,  rect)

    def play(self):
        clock = pygame.time.Clock()
        move_down = pygame.USEREVENT + 1
        pygame.time.set_timer(move_down, 1000)
        spawn = True
        current = None
        
        while not self.done:
            clock.tick(50)
            if spawn:
                self.pieces.append(T())
                current = self.pieces[-1]
                spawn = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == move_down:
                    current.move(0, 1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current.move(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        current.move(1, 0)
                    if event.key == pygame.K_DOWN:
                        current.move(0, 1)
                    if event.key == pygame.K_UP:
                        current.move(0, -1)
            for i in range(10):
                for j in range(20):
                    self.display_background(i*self.block_size, j*self.block_size)

            self.display_pieces()
                
            pygame.display.flip()

if __name__ == "__main__":
    g = game()
    g.play()
