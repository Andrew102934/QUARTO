from .square import Square

class WaitBoard:
    def __init__(self):
        self.grid = [[Square(row, col) for col in range(4)] for row in range(4)]

    def _start_game(self):
        # loop through the squares and place pieces on them
        pass

    def _remove_piece(self, row, col):
        square = self.grid[row][col]
        attributes = square.piece.get_attributes()
        return attributes
    
    def export_piece(self, attributes):
        return attributes