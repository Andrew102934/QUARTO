class Piece:
    # Right now these are bools, they could easily be height, shape, etc with set values
    def __init__(self, is_tall, is_hollow, is_circle, is_gray):
        self.is_tall = is_tall
        self.is_hollow = is_hollow
        self.is_circle = is_circle
        self.is_gray = is_gray
    
    def get_attributes(self):
        # maybe a dictionary to reference by "height", "fill", etc
        return self.is_tall, self.is_hollow, self.is_circle, self.is_gray