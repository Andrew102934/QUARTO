import pygame
import math
from .play_board import PlayBoard

class BoardRenderer:
    def __init__(self, board_rect: pygame.rect, line_width):
        self.board_rect = pygame.Rect(board_rect)
        self.line_width = line_width

        # 4x4
        self.square_size = min(self.board_rect.w, self.board_rect.h) // 4
        width, height = self.square_size * 4, self.square_size * 4

        self.grid_rect = pygame.Rect(0, 0, width, height)
        self.grid_rect.center = self.board_rect.center
        self.gray  =     (180, 180, 180)
        self.black =    (0, 0, 0)

        # good thing we did all those truth tables
        self.combos = [
            (False, False, False, False),
            (True,  False, False, False),
            (False, True,  False, False),
            (True,  True,  False, False),
            (False, False, True,  False),
            (True,  False, True,  False),
            (False, True,  True,  False),
            (True,  True,  True,  False),
            (False, False, False, True),
            (True,  False, False, True),
            (False, True,  False, True),
            (True,  True,  False, True),
            (False, False, True,  True),
            (True,  False, True,  True),
            (False, True,  True,  True),
            (True,  True,  True,  True),
        ]

    def draw_board(self, surface, pieces=False):
        '''Draw Board'''
        pygame.draw.rect(surface, (225, 225, 225), self.board_rect) # For a background

        # out border
        pygame.draw.rect(surface, (0, 0, 0), self.grid_rect, self.line_width)

        #  grid
        for i in range(1, 4):
            # Vertical line
            x = self.grid_rect.x + (i * self.square_size)
            
            pygame.draw.line(
                surface, (0, 0, 0),
                (x, self.grid_rect.y),
                (x, self.grid_rect.y + self.grid_rect.h),
                self.line_width
            )

            # Horizontal line
            y = self.grid_rect.y + (i * self.square_size)
            pygame.draw.line(
                surface, (0, 0, 0),
                (self.grid_rect.x, y),
                (self.grid_rect.x + self.grid_rect.w, y),
                self.line_width
            )
        if pieces:
            if pieces is True:
                self._draw_pieces(surface, start=(self.grid_rect.left, self.grid_rect.top))
            else:
                self.draw_pieces_from_board(surface, pieces)

    def _draw_pieces(self, surface, start=(100, 200)):

        cell = self.grid_rect.width // 4

        for idx, attrs in enumerate(self.combos):
            row = idx // 4
            col = idx % 4

            # top-left of the cell (doesn't work don't know why)
            x = start[0] + (col * cell)
            y = start[1] + (row * cell)

            # draw the piece centered in the cell
            center = (x + cell // 2, y + cell // 2)
            self.draw_piece(attrs, surface, center)

    def draw_pieces_from_board(self, surface, board):
        cell = self.grid_rect.width // 4
        for row in range(4):
            for col in range(4):
                sq = board.grid[row][col]
                if sq.piece is None:
                    continue
                cx = self.grid_rect.left + col * cell + cell // 2
                cy = self.grid_rect.top  + row * cell + cell // 2
                self.draw_piece(sq.piece.get_attributes(), surface, (cx, cy))

    def draw_piece(self, attributes, surface, center):
        # should make this take a square parameter so that it translates better to game board
        tall, hollow, is_circle, light = attributes
        color = self.gray if light else self.black

        if is_circle:
            radius = 35 if tall else 20
            width = 3 if hollow else 0
            pygame.draw.circle(surface, color, center, radius, width)
        else:
            size = 70 if tall else 40
            rect = pygame.Rect(0, 0, size, size)
            rect.center = center
            width = 3 if hollow else 0
            pygame.draw.rect(surface, color, rect, width)

    def _dist(self, a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])

    def get_hover_cell(self, mouse_pos, radius=40):
        cell = self.grid_rect.width // 4
        for row in range(4):
            for col in range(4):
                cx = self.grid_rect.left + col * cell + cell // 2
                cy = self.grid_rect.top  + row * cell + cell // 2
                if self._dist(mouse_pos, (cx, cy)) <= radius:
                    return (row, col)
        return None

    def draw_hover_cell(self, surface, hover_cell, color=(80, 160, 255), width=5):
        if hover_cell is None:
            return
        row, col = hover_cell
        rect = pygame.Rect(
            self.grid_rect.left + col * self.square_size,
            self.grid_rect.top  + row * self.square_size,
            self.square_size,
            self.square_size
        )
        pygame.draw.rect(surface, color, rect, width)

    def get_wait_piece_center(self, attrs):
        cell = self.grid_rect.width // 4
        idx = self.combos.index(attrs)
        row = idx // 4
        col = idx % 4
        cx = self.grid_rect.left + col * cell + cell // 2
        cy = self.grid_rect.top  + row * cell + cell // 2
        return (cx, cy)

    def get_hover_wait_piece(self, mouse_pos, available, radius=40):
        for attrs in available:
            cx, cy = self.get_wait_piece_center(attrs)
            if self._dist(mouse_pos, (cx, cy)) <= radius:
                return attrs
        return None

    def draw_wait_pieces_available(self, surface, available):
        cell = self.grid_rect.width // 4
        for attrs in available:
            idx = self.combos.index(attrs)
            row = idx // 4
            col = idx % 4

            x = self.grid_rect.left + (col * cell)
            y = self.grid_rect.top + (row * cell)

            center = (x + cell // 2, y + cell // 2)
            self.draw_piece(attrs, surface, center)

    def draw_hover_wait_piece(self, surface, hovered_attrs, color=(255, 220, 80), width=4):
        if hovered_attrs is None:
            return
        cx, cy = self.get_wait_piece_center(hovered_attrs)
        pygame.draw.circle(surface, color, (cx, cy), 45, width)

    def draw_selected_wait_piece(self, surface, selected_attrs, color=(80, 255, 140), width=5):
        if selected_attrs is None:
            return
        cx, cy = self.get_wait_piece_center(selected_attrs)
        pygame.draw.circle(surface, color, (cx, cy), 50, width)

class Startup:
    def __init__(self):
        self.player1_name = ''
        self.player2_name = ''
        # self.color_inactive = pygame.color('lightskyblue3')
        # self.color_active = pygame.color('dodgerblue2')

    def draw_text_boxes(self, surface, rectangle=pygame.Rect(50,80,200,40)):
        self.input_box1 = pygame.draw.rect(rectangle)
        self.input_box2 = pygame.draw.rect(pygame.Rect(50,140,200,40))


class StartButton:
    def __init__(self, rect, text, font, action):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.action = action

        self.color_idle = (70,130,180)
        self.color_hover = (100,170,220)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        hover = self.rect.collidepoint(mouse_pos)

        color = self.color_hover if hover else self.color_idle
        pygame.draw.rect(surface, color, self.rect)

        label = self.font.render(self.text, True, (255,255,255))
        surface.blit(label, label.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()




