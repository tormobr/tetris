
import pygame
from t import T
pygame.init()

class game:

    def __init__(self):
        self.current_id = 1
        self.block_size = 50
        self.grid_width = 10
        self.grid_height = 20
        self.screen_width = self.grid_width * self.block_size
        self.screen_height = self.grid_height * self.block_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.done = False
        self.spawn = True

        self.grid = [[0 for i in range(self.screen_width // self.block_size)]
                    for j in range(self.screen_height // self.block_size)]
        self.X_image = pygame.image.load("images/X.png")
        self.pieces = []
        
    
    def display_background(self, x, y):
        self.screen.blit(pygame.transform.scale(self.X_image, (self.block_size, self.block_size)), (x, y))

    def display_pieces(self):
        for piece in self.pieces:
            for rect in piece.rects:
                draw_rect = pygame.Rect(rect.left*50, rect.top*50, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, piece.color,  draw_rect)
    
    def legal_move(self, x, y, current):
        ret_val = True
        stopped = False

        for rect in current.rects:
            if rect.left + x > self.grid_width-1 or rect.left + x < 0:
                ret_val = False
            elif rect.top + y > self.grid_height-1 or rect.top + y < 0:
                ret_val = False
                stopped = True
            elif self.grid[rect.top + y][rect.left + x] != 0:
                ret_val = False
                if x == 0:
                    stopped = True

        if stopped:
            for rect in current.rects:
                self.spawn = True
                self.grid[rect.top][rect.left] = current.ID

            for i, y in enumerate(self.grid):
                filled = True
                for x in y:
                    if x == 0:
                        filled = False
                if filled:
                    for piece in self.pieces:
                        if piece.ID in y:
                            self.pieces.remove(piece)
                    self.grid[i] = [0 for i in range(self.grid_width)]

        return ret_val

    def play(self):
        clock = pygame.time.Clock()
        move_down = pygame.USEREVENT + 1
        pygame.time.set_timer(move_down, 1000)
        current = None
        move_right = False
        move_left = False
        
        while not self.done:
            clock.tick(50)
            if self.spawn:
                self.pieces.append(T(self.current_id))
                self.current_id += 1
                current = self.pieces[-1]
                self.spawn = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == move_down:
                    if self.legal_move(0,1, current):
                        current.move(0, 1)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        move_right = False
                    if event.key == pygame.K_LEFT:
                        move_left = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.legal_move(-1, 0, current):
                            current.move(-1, 0)
                        #move_left = True
                    if event.key == pygame.K_RIGHT:
                        if self.legal_move(1, 0, current):
                            current.move(1, 0)
                        #move_right = True
                    if event.key == pygame.K_DOWN:
                        if self.legal_move(0, 1, current):
                            current.move(0, 1)
                    if event.key == pygame.K_UP:
                        current.rotate()
                    if event.key == pygame.K_SPACE:
                        while self.legal_move(0, 1, current):
                            current.move(0, 1)

            for i in range(10):
                for j in range(20):
                    self.display_background(i*self.block_size, j*self.block_size)

            if move_left:
                if self.legal_move(-1, 0, current):
                    current.move(-1, 0)
            if move_right:
                if self.legal_move(1, 0, current):
                    current.move(1, 0)
            self.display_pieces()
                
            pygame.display.flip()

if __name__ == "__main__":
    g = game()
    g.play()
