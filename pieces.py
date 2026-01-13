import pygame

BLACK = (0, 0, 0)
GRAY = (180, 180, 180)

## Black Circles
def _draw_piece_1(surface, x, y):

    pygame.draw.circle(surface, BLACK, (x, y), 20)

def _draw_piece_2(surface, x, y):

    pygame.draw.circle(surface, BLACK, (x, y), 35)

def _draw_piece_3(surface, x, y):

    pygame.draw.circle(surface, BLACK, (x, y), 20, 3)

def _draw_piece_4(surface, x, y):
    pygame.draw.circle(surface, BLACK, (x, y), 35, 3)

def _draw_black_circles(surface, x, y, spacing):
        _draw_piece_1(surface, x, y + 2*spacing)
        _draw_piece_2(surface, x + spacing, y + 2*spacing)
        _draw_piece_3(surface, x + 2*spacing, y + 2*spacing)
        _draw_piece_4(surface, x + 3*spacing, y + 2*spacing)

### Gray Circles
def _draw_piece_5(surface, x, y):
    pygame.draw.circle(surface, GRAY, (x, y), 20)

def _draw_piece_6(surface, x, y):
    pygame.draw.circle(surface, GRAY, (x, y), 35)

def _draw_piece_7(surface, x, y):
    pygame.draw.circle(surface, GRAY, (x, y), 20, 3)

def _draw_piece_8(surface, x, y):
    pygame.draw.circle(surface, GRAY, (x, y), 35, 3)

def _draw_gray_circles(surface, x, y, spacing):
        _draw_piece_5(surface, x, y + 3*spacing)
        _draw_piece_6(surface, x + spacing, y + 3*spacing)
        _draw_piece_7(surface, x + 2*spacing, y + 3*spacing)
        _draw_piece_8(surface, x + 3*spacing, y + 3*spacing)

def draw_circles(surface, x, y, spacing):
        _draw_black_circles(surface, x, y, spacing)
        _draw_gray_circles(surface, x, y, spacing)

## Black Squares
def _draw_piece_9(surface, x, y):
    pygame.draw.rect(surface, BLACK, (x-20, y-20, 40, 40))

def _draw_piece_10(surface, x, y):
    pygame.draw.rect(surface, BLACK, (x-35, y-35, 70, 70))

def _draw_piece_11(surface, x, y):
    pygame.draw.rect(surface, BLACK, (x-20, y-20, 40, 40), 3)

def _draw_piece_12(surface, x, y):
    pygame.draw.rect(surface, BLACK, (x-35, y-35, 70, 70), 3)

def _draw_black_squares(surface, x, y, spacing):
        _draw_piece_9(surface, x, y + 2*spacing)
        _draw_piece_10(surface, x + spacing, y + 2*spacing)
        _draw_piece_11(surface, x + 2*spacing, y + 2*spacing)
        _draw_piece_12(surface, x + 3*spacing, y + 2*spacing)

## Gray Squares
def _draw_piece_13(surface, x, y):
    pygame.draw.rect(surface, GRAY, (x-20, y-20, 40, 40))

def _draw_piece_14(surface, x, y):
    pygame.draw.rect(surface, GRAY, (x-35, y-35, 70, 70))

def _draw_piece_15(surface, x, y):
    pygame.draw.rect(surface, GRAY, (x-20, y-20, 40, 40), 3)

def _draw_piece_16(surface, x, y):
    pygame.draw.rect(surface, GRAY, (x-35, y-35, 70, 70), 3)

def _draw_gray_squares(surface, x, y, spacing):
        _draw_piece_13(surface, x, y + 3*spacing)
        _draw_piece_14(surface, x + spacing, y + 3*spacing)
        _draw_piece_15(surface, x + 2*spacing, y + 3*spacing)
        _draw_piece_16(surface, x + 3*spacing, y + 3*spacing)

def draw_squares(surface, x, y, spacing):
        _draw_black_squares(surface, x, y, spacing)
        _draw_gray_squares(surface, x, y, spacing)