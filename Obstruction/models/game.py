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
        '''
        class method that handles a human move
        first, the move is validated and then it is made. 
        in case the move is invalid, the error is raised up until the UI, where it is handled, and the move will not be made.
        '''
        self.__moveValidator.validateCoordinates(move.getBoardX(),move.getBoardY(),self.__board)
        self.__board.move(move,'X')
    
    def moveComputer(self):
        emptySquares = self.__board.emptySquares()
        
        '''
        Try to win
        '''
        for square in emptySquares:
            '''
            -board copy 
            -try moves 
            -check for win
            '''
            board = self.__board.copy()
            board.move(square,'O')
            if board.isWon() == True: 
                self.__board.move(square,'O')
                return 
        '''
        Prevent human win
        '''
        for square in emptySquares: 
            '''
            -board copy
            -try move for X
            -check for win
            '''
            board = self.__board.copy()
            board.move(square,'X')
            if board.isWon() == True: 
                self.__board.move(square,'O')
                return 
        '''
        Move on a random square selected from the empty ones
        '''
        self.__board.move(choice(emptySquares),'O')

