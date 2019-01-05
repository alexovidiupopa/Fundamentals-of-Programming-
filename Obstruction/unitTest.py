
from models.board import Board
from models.game import Game
from models.dimension import Dimension
from validators import boardValidator
from errors.errors import CoordError,BoardError
import unittest

class boardTests(unittest.TestCase):
    
    def setUp(self):
        self.__board = Board(5,5)
    
    def testInitialize(self):
        width = self.__board.getWidth()
        height = self.__board.getHeight()
        for i in range(height):
            for j in range(width):
                self.assertEqual(self.__board._board[i][j],0)
    def testGetters(self):
        self.assertEqual(self.__board.getWidth(),5)
        self.assertEqual(self.__board.getHeight(),5)
        
    def testMove(self):
        self.__board.move(Dimension(4,4),'X')
        self.assertEqual(self.__board._board[4][4],1)
        self.assertEqual(self.__board._board[3][4],3)
        self.assertEqual(self.__board._board[0][0],0)
    
    def testEmptySquares(self):
        emptySquares = self.__board.emptySquares()
        self.assertEqual(len(emptySquares),25)
        self.__board.move(Dimension(2,2),'O')
        emptySquares = self.__board.emptySquares()
        self.assertEqual(len(emptySquares),16)
        self.assertEqual(emptySquares[0],Dimension(0,0))
        
    def testWin(self):
        newBoard = Board(3,3)
        newBoard.move(Dimension(1,1),'X')
        self.assertEqual(newBoard.isWon(),True)
        

class gameTests(unittest.TestCase):
    def setUp(self):
        self.__game = Game(Board(5,5),boardValidator())
        
    def testMoveHuman(self):
        move = Dimension(1,1)
        self.__game.moveHuman(move)
        board = self.__game.getBoard()
        self.assertEqual(board._board[1][1],1)
        self.assertEqual(board._board[1][0],3)
        self.assertEqual(board._board[4][4],0)
        move = Dimension(-1,-1)
        self.assertRaises(CoordError,self.__game.moveHuman,move)
        move = Dimension(1,2)
        self.assertRaises(CoordError,self.__game.moveHuman,move)
    
    def testMoveComputer(self):
        self.__game.moveComputer()
        board = self.__game.getBoard()
        self.assertLess(len(board.emptySquares()),25)
        self.assertGreaterEqual(len(board.emptySquares()),16)
        
class testValidators(unittest.TestCase):
    
    def setUp(self):
        self.__boardValidator = boardValidator()
        self.__board = Board(4,4)
        
    def testBoardValidator(self):
        self.assertRaises(BoardError,self.__boardValidator.validate,-2,-1)
        
    def testCoordinatesValidator(self):
        self.assertRaises(CoordError,self.__boardValidator.validateCoordinates,1,5,self.__board)
        self.assertRaises(CoordError,self.__boardValidator.validateCoordinates,5,1,self.__board)
        self.__board.move(Dimension(0,0),'X')
        self.assertRaises(CoordError,self.__boardValidator.validateCoordinates,1,1,self.__board)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()