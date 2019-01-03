from random import choice
from validators import boardValidator

class Game(object):

    '''
    Class for the game entity
    '''
    def __init__(self, board):
        self.__board = board
        self.__moveValidator = boardValidator()
        
    def getBoard(self):
        return self.__board
    
    def moveHuman(self,move):
        self.__moveValidator.validateCoordinates(move,self.__board)
        self.__board.move(move,'X')
    
    def moveComputer(self):
        pass 



