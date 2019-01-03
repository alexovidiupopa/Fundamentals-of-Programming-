from errors.errors import BoardError, CoordError
import unittest

class boardValidator(object):
    
    def validate(self, boardX, boardY):
        if boardX <= 0 or boardY <= 0: 
            raise BoardError("Incorrect dimensions! Must be greater than 0!")
    
    def validateCoordinates(self,boardX,boardY,board):
        errors = ""
        if boardX<0 or boardX>=board.getWidth() or boardY<0 or boardY>=board.getHeight():
            errors+="Coordinates must be between 0 and width/height - 1."
        board = board._board
        if board[boardY][boardX]!=0: 
            errors+="Square already taken!"
        if errors!="": 
            raise CoordError("Coordinates error!"+errors)
    
class testValidators(unittest.TestCase):
    
    def setUp(self):
        self.__boardValidator = boardValidator()
        
    def testBoardValidator(self):
        x1 = -2
        y1 = -1
        self.assertRaises(BoardError,self.__boardValidator.validate,x1,y1)
        