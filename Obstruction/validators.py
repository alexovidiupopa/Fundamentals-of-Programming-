from errors.errors import BoardError
import unittest

class boardValidator(object):
    
    def validate(self, boardX, boardY):
        if boardX <= 0 or boardY <= 0: 
            raise BoardError("Incorrect dimensions! Must be greater than 0!")
    

class testValidators(unittest.TestCase):
    
    def setUp(self):
        self.__boardValidator = boardValidator()
        
    def testBoardValidator(self):
        x1 = -2
        y1 = -1
        self.assertRaises(BoardError,self.__boardValidator.validate,x1,y1)
        