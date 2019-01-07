from random import choice

class Game(object):

    '''
    Class for the game entity
    '''
    def __init__(self, board, BoardValidator):
        self.__board = board
        self.__moveValidator = BoardValidator
        
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
        Try to win. Steps: 
        -copy the board 
        -try each possible move in emptySquares
        -check if the board is won after the move
        '''
        for square in emptySquares:    
            board = self.__board.copy()
            board.move(square,'O')
            if board.isWon() == True: 
                self.__board.move(square,'O')
                return 
        '''
        Prevent the human from winning. Steps: 
        -copy the board 
        -try each possible move for X 
        -check if the board is won after the move
        '''
        for square in emptySquares: 
            board = self.__board.copy()
            board.move(square,'X')
            if board.isWon() == True: 
                self.__board.move(square,'O')
                return 
        '''
        If we're here, that means that the previous strategies didn't work, so:
        The computer will move on a random square selected from the empty ones
        '''
        self.__board.move(choice(emptySquares),'O')
