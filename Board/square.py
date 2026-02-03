class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.piece = None
    
    def place(self, piece):
        if self.piece == None:
            self.piece = piece
        else:
            raise ValueError("Square occupied")
    
    def is_empty(self):
        # Might be unnecessary with the checker in place but we can remove later if so
        return self.piece == None
    