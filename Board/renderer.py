import pygame
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
        self.gray =     (180, 180, 180)
        self.black =    (0, 0, 0)
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
            self._draw_pieces_on_board(surface, self.board_rect, (150, 250))

    def _draw_pieces(self, surface, start=(100, 200)):
        combos = [
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

        cell = 100

        for idx, attrs in enumerate(combos):
            row = idx // 4
            col = idx % 4

            # top-left of the cell (doesn't work don't know why)
            x = start[0] + (col * cell)
            y = start[1] + (row * cell)

            # draw the piece centered in the cell
            center = (x + cell // 2, y + cell // 2)
            self.draw_piece(attrs, surface, center)

    def _draw_pieces_on_board(self, surface, board_rect, pieces_4x4, line_width=3):
        cell = board_rect.width // 4  # 100

        inset = line_width / 2

        for row in range(4):
            for col in range(4):
                attrs = pieces_4x4[row][col]
                if attrs is None:
                    continue

                cx = board_rect.left + col * cell + cell / 2 + inset
                cy = board_rect.top  + row * cell + cell / 2 + inset

                self.draw_piece(attrs, surface, (int(cx), int(cy)))


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

