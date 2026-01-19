class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.occupied = False
        self.piece = None
    
    def get_piece(self):
        return self.piece.get_attribute