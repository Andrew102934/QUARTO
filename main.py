import pygame 
import sys
from Board import PlayBoard, BoardRenderer, Piece

pygame.init()

WIDTH,HEIGHT = (900, 700)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
clock = pygame.time.Clock()

board = PlayBoard()
play_board = BoardRenderer(pygame.Rect(480, 140, 360, 360), line_width=3)
wait_board = BoardRenderer(pygame.Rect(60, 140, 360, 360), line_width=3)

available = list(wait_board.combos)
selected_attrs = None

if __name__ == '__main__':
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        hover_cell = play_board.get_hover_cell(mouse)
        hover_piece = wait_board.get_hover_wait_piece(mouse, available)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if hover_piece is not None:
                    selected_attrs = hover_piece

                if selected_attrs is not None:
                    cell = play_board.get_hover_cell(event.pos)
                    if cell is not None:
                        r, c = cell
                        if board.grid[r][c].piece is None:
                            tall, hollow, is_circle, is_gray = selected_attrs
                            board.grid[r][c].place(Piece(tall, hollow, is_circle, is_gray))
                            if selected_attrs in available:
                                available.remove(selected_attrs)
                            selected_attrs = None

        screen.fill(WHITE)

        play_board.draw_board(screen)
        play_board.draw_pieces_from_board(screen, board)
        play_board.draw_hover_cell(screen, hover_cell)

        wait_board.draw_board(screen)
        wait_board.draw_wait_pieces_available(screen, available)
        wait_board.draw_hover_wait_piece(screen, hover_piece)
        wait_board.draw_selected_wait_piece(screen, selected_attrs)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()
