import pygame

class BoardRenderer:
    def __init__(self, board_rect: pygame.rect, line_width):
        self.board_rect = pygame.Rect(board_rect)
        self.line_width = line_width

        # 4x4
        self.square_size = min(self.board_rect.w, self.board_rect.h) // 4
        width, height = self.square_size * 4, self.square_size * 4

        self.grid_rect = pygame.Rect(0, 0, width, height)
        self.grid_rect.center = self.board_rect.center

    def draw(self, surface):
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