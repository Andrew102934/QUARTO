from square import Square

class Board:
    def __init__(self, win_on_board=False):
        self.grid = [[Square(row, col) for col in range(4)] for row in range(4)] # I may have gotten mixed up here but i think this works
        print(self.grid) #just to make sure, haven't gotten to check yet
        self.win_on_board = win_on_board
    
    def _check_line(self):
        # will likely call rows and cols
        pass

    def _rows(self):
        return self.grid

    def _cols(self):
        pass

    def _diagonals(self):
        pass

    def place_piece(self, piece, row, col):
        pass
    
    def check_win(self):
        pass