class Obj:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.piece = None
    
    def get_piece(self):
        return self.piece