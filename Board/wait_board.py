from .square import Square

class WaitBoard:
    def __init__(self):
        self.grid = [[Square(row, col) for col in range(4)] for row in range(4)]
        

