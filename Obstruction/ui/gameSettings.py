from validators import boardValidator
from errors.errors import BoardError
#import unittest
from models.dimension import Dimension

class Settings(object):
    
    def getDimensions(self):
        print("Board width: ")
        try: 
            boardX = int(input())
            print("Board height: ")
            boardY = int(input())
            boardValidator.validate(boardX,boardY)
            return Dimension(boardX,boardY)
        except ValueError: 
            print("Incorrect dimensions! Must be integers! ")
        except BoardError as be: 
            print(be)
    

