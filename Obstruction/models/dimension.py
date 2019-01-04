class Dimension(object):
    '''
    class for the dimension/square entity
    '''
    def __init__(self, boardX, boardY):
        self.__boardX = boardX
        self.__boardY = boardY

    def getBoardX(self):
        return self.__boardX


    def getBoardY(self):
        return self.__boardY

    
    def __str__(self):
        return str(self.boardX) + "  " + str(self.boardY)
    
    boardX = property(getBoardX, None, None, None)
    boardY = property(getBoardY, None, None, None)



