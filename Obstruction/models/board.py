from models.dimension import Dimension
from texttable import Texttable
import copy

class Board(object):
    
    '''
    Class for the Board entity
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self._board = []
        self.__boardInitialize()
    
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def __str__(self):
        table = Texttable()
        data = {0:" ",1:"X",2:"0",3:"#"}
        for i in range(self.__height):
            list = []
            for j in range(self.__width):
                list.append(data[self._board[i][j]])
            table.add_row(list)
        return table.draw()
    
    def __boardInitialize(self):
        for i in range(self.__height): 
            row = []
            for j in range(self.__width): 
                row.append(0)
            self._board.append(row)

    def isWon(self):
        return len(self.emptySquares()) == 0
    
    def emptySquares(self):
        emptySq = []
        for i in range(self.__height):
            for j in range(self.__width): 
                if self._board[i][j] == 0:
                    emptySq.append(Dimension(i,j))
        return emptySq[:]
    
    def copy(self):
        board = Board()
        board._board = copy.deepcopy(self._board)
        return board
    
    def move(self,dimension,symbol):
        pass