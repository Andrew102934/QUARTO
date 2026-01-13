import pygame 
import sys
from pieces import draw_circles, draw_squares

pygame.init()

WIDTH,HEIGHT = (600, 800)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
clock = pygame.time.Clock()

if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(WHITE)
        
        ##Piece Rendering
        x_start = 100
        y_start = 100
        spacing = 100

        draw_circles(screen, x_start, y_start, spacing)
        draw_squares(screen, x_start, y_start + 2 * spacing, spacing)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()