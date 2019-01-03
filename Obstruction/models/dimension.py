class Dimension(object):
    
    
    def __init__(self, boardX, boardY):
        self.boardX = boardX
        self.boardY = boardY

    def getBoardX(self):
        return self.__boardX


    def getBoardY(self):
        return self.__boardY

    
    def __str__(self):
        return str(self.boardX) + "  " + str(self.boardY)
    
    boardX = property(getBoardX, None, None, None)
    boardY = property(getBoardY, None, None, None)



