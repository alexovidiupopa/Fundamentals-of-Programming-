from errors.errors import BoardError, CoordError
import unittest

class boardValidator(object):
    
    def validate(self, boardX, boardY):
        if boardX <= 0 or boardY <= 0: 
            raise BoardError("Incorrect dimensions! Must be greater than 0!")
    
    def validateCoordinates(self,move,board):
        errors = ""
        if move.getBoardX()<0 or move.getBoardX()>=board.getWidth() or move.getBoardY()<0 or move.getBoardY()>=board.getHeight():
            errors+="Coordinates must be between 0 and width/height - 1."
        if errors!="": 
            raise CoordError("Coordinates error!"+errors)
    
class testValidators(unittest.TestCase):
    
    def setUp(self):
        self.__boardValidator = boardValidator()
        
    def testBoardValidator(self):
        x1 = -2
        y1 = -1
        self.assertRaises(BoardError,self.__boardValidator.validate,x1,y1)
        