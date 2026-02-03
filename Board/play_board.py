from .square import Square
from .piece import Piece

class PlayBoard:
    def __init__(self, win_on_board=False):
        self.grid = [[Square(row, col) for col in range(4)] for row in range(4)]
        self.win_on_board = win_on_board

    def _check_line(self, line):
        if line is None or len(line) != 4:
            return False
        for piece in line:
            if piece is None:
                return False

        attrs = [p.get_attributes() for p in line]

        for i in range(4):
            vals = [a[i] for a in attrs]
            if all(v is True for v in vals) or all(v is False for v in vals):
                return True

        return False

    def _rows(self):
        return [[self.grid[r][c].piece for c in range(4)] for r in range(4)]

    def _cols(self):
        return [[self.grid[r][c].piece for r in range(4)] for c in range(4)]

    def _diagonals(self):
        return [
            [self.grid[i][i].piece for i in range(4)],
            [self.grid[i][3 - i].piece for i in range(4)]
        ]

    def place_piece(self, attributes, row, col):
        piece = Piece(attributes)
        self.grid[row][col].place(piece)

    def check_win(self):
        lines = []
        lines.extend(self._rows())
        lines.extend(self._cols())
        lines.extend(self._diagonals())

        for line in lines:
            if self._check_line(line):
                return True

        return False

    def check_row(self, row):
        return self._check_line([self.grid[row][c].piece for c in range(4)])

    def check_col(self, col):
        return self._check_line([self.grid[r][col].piece for r in range(4)])

    def check_diagonal(self, which):
        if which == 0:
            return self._check_line([self.grid[i][i].piece for i in range(4)])
        return self._check_line([self.grid[i][3 - i].piece for i in range(4)])

    def check_line(self, kind, index, attr_index, value):
        if kind == "row":
            return self._claimed_match([self.grid[index][c].piece for c in range(4)], attr_index, value)
        if kind == "col":
            return self._claimed_match([self.grid[r][index].piece for r in range(4)], attr_index, value)
        if kind == "diag":
            if index == 0:
                return self._claimed_match([self.grid[i][i].piece for i in range(4)], attr_index, value)
            return self._claimed_match([self.grid[i][3 - i].piece for i in range(4)], attr_index, value)
        return False

    def _claimed_match(self, line, attr_index, value):
        if line is None or len(line) != 4:
            return False
        for piece in line:
            if piece is None:
                return False
        attrs = [p.get_attributes() for p in line]
        return all(a[attr_index] == value for a in attrs)

    def has_any_win(self):
        for r in range(4):
            if self.check_row(r):
                return True
        for c in range(4):
            if self.check_col(c):
                return True
        if self.check_diagonal(0):
            return True
        if self.check_diagonal(1):
            return True
        return False
