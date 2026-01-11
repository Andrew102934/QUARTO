import pygame 
import sys
from pieces import *


pygame.init()

WIDTH,HEIGHT = (600, 800)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
clock = pygame.time.Clock()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(WHITE)
    ##piece rendering--
        x_start = 100
        y_start = 100
        spacing = 100

        draw_piece_1(screen, x_start, y_start)
        draw_piece_2(screen, x_start + spacing, y_start)
        draw_piece_3(screen, x_start + 2*spacing, y_start)
        draw_piece_4(screen, x_start + 3*spacing, y_start)

        draw_piece_5(screen, x_start, y_start + spacing)
        draw_piece_6(screen, x_start + spacing, y_start + spacing)
        draw_piece_7(screen, x_start + 2*spacing, y_start + spacing)
        draw_piece_8(screen, x_start + 3*spacing, y_start + spacing)

        draw_piece_9(screen, x_start, y_start + 2*spacing)
        draw_piece_10(screen, x_start + spacing, y_start + 2*spacing)
        draw_piece_11(screen, x_start + 2*spacing, y_start + 2*spacing)
        draw_piece_12(screen, x_start + 3*spacing, y_start + 2*spacing)

        draw_piece_13(screen, x_start, y_start + 3*spacing)
        draw_piece_14(screen, x_start + spacing, y_start + 3*spacing)
        draw_piece_15(screen, x_start + 2*spacing, y_start + 3*spacing)
        draw_piece_16(screen, x_start + 3*spacing, y_start + 3*spacing)







        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

main()


