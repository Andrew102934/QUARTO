import pygame

class BoardRenderer:
    def __init__(self, board_rect: pygame.rect, line_width):
        self.board_rect = board_rect
        self.line_width = line_width