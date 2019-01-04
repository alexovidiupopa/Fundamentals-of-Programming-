from validators import boardValidator
from errors.errors import BoardError
from models.dimension import Dimension

class Settings(object):
    '''
    class to handle the board dimensions before the game starts.
    '''
    def __init__(self):
        self.__boardValidator = boardValidator()
        
    def getDimensions(self):
        '''
        in: - 
        out: a Dimension of (x,y) width and height 
        the method handles valueErrors as well as BoardErrors in case the input is incorrect.
        '''
        while True:
            print("Board width: ")
            try: 
                boardX = int(input())
                print("Board height: ")
                boardY = int(input())
                self.__boardValidator.validate(boardX,boardY)
                return Dimension(boardX,boardY)
            except ValueError: 
                print("Incorrect dimensions! Must be integers! ")
            except BoardError as be: 
                print(be)
    