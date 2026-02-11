import pygame 
import sys
from Board import PlayBoard, BoardRenderer, Piece, Startup, StartButton

pygame.init()

WIDTH,HEIGHT = (900, 700)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

name_box_1 = Startup(rect=pygame.Rect(50,80,200,40))
name_box_2 = Startup(rect=pygame.Rect(50,140,200,40))
start_button = StartButton(rect=pygame.Rect(50, 200, 200, 40), text='Start', action=None, font=font)

board = PlayBoard()
play_board = BoardRenderer(pygame.Rect(480, 140, 360, 360), line_width=3)
wait_board = BoardRenderer(pygame.Rect(60, 140, 360, 360), line_width=3)

available = list(wait_board.combos)

if __name__ == '__main__':
    running = True
    state = "name_entry"
    player1_name = ""
    player2_name = ""

    selected_attrs = None
    
    def start_game():
        global state, player1_name, player2_name
        player1_name = name_box_1.text.strip() or "Player 1"
        player2_name = name_box_2.text.strip() or "Player 2"
        state = "game"

    start_button.action = start_game

    while running:
        mouse = pygame.mouse.get_pos()

        #---------- DRAW -----------
        screen.fill(WHITE)

        if state == "name_entry":
            title = font.render("Enter player names", True, (0, 0, 0))
            screen.blit(title, (50, 30))

            label1 = font.render("Player 1:", True, (0, 0, 0))
            label2 = font.render("Player 2:", True, (0, 0, 0))
            screen.blit(label1, (50, 60))
            screen.blit(label2, (50, 120))

            name_box_1.draw(screen)
            name_box_2.draw(screen)
            start_button.draw(screen)

        elif state == "game":
            p1 = font.render(player1_name, True, (0, 0, 0))
            p2 = font.render(player2_name, True, (0, 0, 0))
            screen.blit(p1, (10, 10))
            screen.blit(p2, (10, 40))

            play_board.draw_board(screen)
            play_board.draw_pieces_from_board(screen, board)
            play_board.draw_hover_cell(screen, hover_cell)

            wait_board.draw_board(screen)
            wait_board.draw_wait_pieces_available(screen, available)
            wait_board.draw_hover_wait_piece(screen, hover_piece)
            wait_board.draw_selected_wait_piece(screen, selected_attrs)

        if state == "game":
            hover_cell = play_board.get_hover_cell(mouse)
            hover_piece = wait_board.get_hover_wait_piece(mouse, available)
        else:
            hover_cell = None
            hover_piece = None
        
        #---------------------------
        #---------- PLAY -----------
        #---------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #---------- NAME ENTRY SCREEN ----------
            if state == "name_entry":
                name_box_1.handle_event(event)
                name_box_2.handle_event(event)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    start_game()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    start_button.handle_event(event)

            #---------- GAME SCREEN ----------
            elif state == "game":
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


        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()
