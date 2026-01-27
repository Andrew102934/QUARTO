import pygame 
import sys
from Board import PlayBoard, BoardRenderer, Piece
from pieces import draw_circles, draw_squares

pygame.init()

WIDTH, HEIGHT = (1200, 700)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
clock = pygame.time.Clock()

board = PlayBoard()
play_board = BoardRenderer(pygame.Rect(700, 200, 400, 400), line_width=3)
wait_board = BoardRenderer(pygame.Rect(100, 200, 400, 400), line_width=3)

if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(WHITE)
        play_board.draw_board(screen)
        wait_board.draw_board(screen, pieces=True)
        
        x_start = 150
        y_start = 50
        spacing = 100

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()