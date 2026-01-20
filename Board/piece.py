class Piece:
    def __init__(self, is_tall, is_hollow, is_circle, is_gray):
        self.is_tall = is_tall
        self.is_hollow = is_hollow
        self.is_circle = is_circle
        self.is_gray = is_gray
    
    def get_attributes(self):
        return self.is_tall, self.is_hollow, self.is_circle, self.is_gray