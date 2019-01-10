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
        '''
        overwrites the print() method for the board coordinates
        '''
        return str(self.boardX) + "  " + str(self.boardY)
    
    def __eq__(self,toCheck):
        '''
        overwrites the == operator, to check if two board coordinates are equal
        '''
        return self.__boardX == toCheck.getBoardX() and self.__boardY == toCheck.getBoardY()
    
    boardX = property(getBoardX, None, None, None)
    boardY = property(getBoardY, None, None, None)



