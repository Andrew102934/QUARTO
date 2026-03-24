import pygame
import sys
from Board import (
    PlayBoard,
    BoardRenderer,
    Piece,
    Startup,
    StartButton,
    WinButton,
)

pygame.init()

WIDTH, HEIGHT = (900, 700)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quarto")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 42)

# UI 
name_box_1 = Startup(rect=pygame.Rect(50, 80, 200, 40), font=font)
name_box_2 = Startup(rect=pygame.Rect(50, 140, 200, 40), font=font)

# GAME OBJECTS
board = PlayBoard()
play_board = BoardRenderer(pygame.Rect(480, 140, 360, 360), line_width=3)
wait_board = BoardRenderer(pygame.Rect(60, 140, 360, 360), line_width=3)

available = list(wait_board.combos)

# STATE
state = "name_entry"
running = True

player1_name = ""
player2_name = ""
current_player = 1
winner_text = ""

selected_attrs = None
hover_cell = None
hover_piece = None

def reset_game():
    global board, available, selected_attrs, current_player, winner_text
    board = PlayBoard()
    available = list(wait_board.combos)
    selected_attrs = None
    current_player = 1
    winner_text = ""

def start_game():
    global state, player1_name, player2_name
    player1_name = name_box_1.text.strip() or "Player 1"
    player2_name = name_box_2.text.strip() or "Player 2"
    reset_game()
    state = "game"

def call_win(current_board):
    global state, winner_text
    if board.check_win():
        current_name = player1_name if current_player == 1 else player2_name
        winner_text = f"{current_name} wins!"
        state = "win"
    

start_button = StartButton(
    rect=pygame.Rect(50, 200, 200, 40),
    text="Start",
    action=start_game,
    font=font,
)

win_button = WinButton(
    rect=pygame.Rect(480, 530, 160, 45),
    text="Call Win",
    action=call_win(board),
    font=font,
)

def get_current_player_name():
    return player1_name if current_player == 1 else player2_name


while running:
    mouse = pygame.mouse.get_pos()

    # update hover BEFORE drawing
    if state == "game":
        hover_cell = play_board.get_hover_cell(mouse)
        hover_piece = wait_board.get_hover_wait_piece(mouse, available)
    else:
        hover_cell = None
        hover_piece = None

    # ---------- DRAW ----------
    screen.fill(WHITE)

    if state == "name_entry":
        title = big_font.render("Enter player names", True, BLACK)
        screen.blit(title, (50, 30))

        label1 = font.render("Player 1:", True, BLACK)
        label2 = font.render("Player 2:", True, BLACK)
        screen.blit(label1, (50, 60))
        screen.blit(label2, (50, 120))

        name_box_1.draw(screen)
        name_box_2.draw(screen)
        start_button.draw(screen)

    elif state == "game":
        # player labels
        p1 = font.render(f"Player 1: {player1_name}", True, BLACK)
        p2 = font.render(f"Player 2: {player2_name}", True, BLACK)
        turn = font.render(f"Current player: {get_current_player_name()}", True, BLACK)

        instruction_text = (
            "Select a piece from the waiting area, then click a space on the board."
            if selected_attrs is None
            else "Now place the selected piece on the play board."
        )
        instruction = font.render(instruction_text, True, BLACK)

        screen.blit(p1, (30, 20))
        screen.blit(p2, (30, 50))
        screen.blit(turn, (30, 80))
        screen.blit(instruction, (30, 110))

        # play board
        play_board.draw_board(screen)
        play_board.draw_pieces_from_board(screen, board)
        play_board.draw_hover_cell(screen, hover_cell)

        # waiting board
        wait_board.draw_board(screen)
        wait_board.draw_wait_pieces_available(screen, available)
        wait_board.draw_hover_wait_piece(screen, hover_piece)
        wait_board.draw_selected_wait_piece(screen, selected_attrs)

        win_button.draw(screen)

    elif state == "win":
        msg = big_font.render(winner_text, True, BLACK)
        restart_msg = font.render("Press ENTER to play again or ESC to quit.", True, BLACK)

        screen.blit(msg, (50, 100))
        screen.blit(restart_msg, (50, 160))

    # ---------- EVENTS ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "name_entry":
            name_box_1.handle_event(event)
            name_box_2.handle_event(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start_game()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_button.handle_event(event)

        elif state == "game":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # button click
                win_button.handle_event(event)

                # piece selection
                if hover_piece is not None:
                    selected_attrs = hover_piece

                # piece placement
                elif selected_attrs is not None:
                    cell = play_board.get_hover_cell(event.pos)
                    if cell is not None:
                        r, c = cell
                        if board.grid[r][c].piece is None:
                            tall, hollow, is_circle, is_gray = selected_attrs
                            board.grid[r][c].place(Piece(tall, hollow, is_circle, is_gray))

                            if selected_attrs in available:
                                available.remove(selected_attrs)

                            selected_attrs = None
                            current_player = 2 if current_player == 1 else 1

        elif state == "win":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_game()
                elif event.key == pygame.K_ESCAPE:
                    running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()