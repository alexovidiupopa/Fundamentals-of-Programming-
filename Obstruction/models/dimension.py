class Dimension(object):
    
    
    def __init__(self, boardX, boardY):
        self.boardX = boardX
        self.boardY = boardY
    
    def __str__(self):
        return str(self.boardX) + "  " + str(self.boardY)



