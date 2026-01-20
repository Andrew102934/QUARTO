from square import Square

class Board:
    def __init__(self, win_on_board=False):
        self.grid = [[Square(row, col) for col in range(4)] for row in range(4)]
        self.win_on_board = win_on_board
    
    def _check_line(self, line):
        '''Takes an array (line) of pieces and compares their values to check if the line contains a win'''
        heights, fills, shapes, colors = []
        for piece in line:
            height, fill, shape, color = piece.get_attributes()
            heights.append[height]
            fills.append[fill]
            shapes.append[shape]
            colors.append[color]
        
        # There has to be a better way to do this but just need to get this done for now -Michael
        counter = 0
        while counter != 4:
            for height in heights:
                if height == True:
                    counter += 1
            counter = 0
            for fill in fills:
                if fill == True:
                    counter += 1
            counter = 0
            for shape in shapes:
                if shape == True:
                    counter += 1
            counter = 0
            for color in colors:
                if color == True:
                    counter += 1
            return False
        
        return True

    def _rows(self):
        '''Return the pieces in each row'''
        return [[sq.piece.get_attributes() for sq in row] for row in self.grid]

    # Still need to double check this -Michael
    def _cols(self):
        '''Return the pieces in each column **** NEEDS TESTING *****'''
        for row in self.grid:
            return [row[col] for col in range(4)]

    def _diagonals(self):
        '''Return the pieces in each of the two diagonals'''
        tleft_to_bright = [self.grid[i][i] for i in range(4)]
        bleft_to_tright = [self.grid[j][3-j] for j in range(4)] #[0,3][1,2][2,1],[3,0] if this works how I think I'm proud of this
        return tleft_to_bright, bleft_to_tright 

    def place_piece(self, piece, row, col):
        '''Place a piece on a square'''
        self.grid[row][col].place(piece)
    
    def check_win(self):
        '''Checks for a win on the board'''
        lines = self._rows()
        lines.append(self._cols())
        lines.append(self._diagonals())
        
        for line in lines:
            if self._check_line(line) == True:
                return True
        
        return False