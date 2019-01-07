from models.dimension import Dimension
from texttable import Texttable
import copy

class Board(object):
    
    '''
    Class for the Board entity
    '''
    def __init__(self, width, height):
        '''
        class constructor, the board will also be initialized here
        '''
        self.__width = width
        self.__height = height
        self._board = []
        self.__boardInitialize()
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def __str__(self):
        '''
        class method to overwrite the print method.
        here, the texttable library will be used.
        '''
        table = Texttable()
        data = {0:" ",1:"X",2:"0",3:"#"}
        for rowIndex in range(self.__height):
            list = []
            for columnIndex in range(self.__width):
                list.append(data[self._board[rowIndex][columnIndex]])
            table.add_row(list)
        return table.draw()
    
    def __boardInitialize(self):
        '''
        class method that initializes the board, that is, it constructs a matrix and fills it with zeros.
        in: - 
        out:-
        '''
        for rowIndex in range(self.__height): 
            row = []
            for columnIndex in range(self.__width): 
                row.append(0)
            self._board.append(row)

    def isWon(self):
        '''
        class method that checks if the game is won (over). 
        the game is won when there are no more empty squares on the board.
        in: - 
        out : True/False depending on whether the condition described above is met.
        '''
        return len(self.emptySquares()) == 0
    
    def emptySquares(self):
        '''
        class method that appends into and returns a list containing all the empty squares on the board.
        in : - 
        '''
        emptySq = []
        for rowIndex in range(self.__height):
            for columnIndex in range(self.__width): 
                if self._board[rowIndex][columnIndex] == 0:
                    emptySq.append(Dimension(rowIndex,columnIndex))
        return emptySq
    
    def copy(self):
        '''
        class method that returns a copy of the current board. 
        in: - 
        out:a Board() type object representing the current state of the board
        '''
        board = Board(self.__width,self.__height)
        board._board = copy.deepcopy(self._board)
        return board
    
    def move(self,dimension,symbol):
        '''
        class method that handles moving a symbol to the dimension (x,y)
        in - dimension - (x,y) point on the board 
             symbol - X or O 
        out: - 
        restrictions: the dimension is already validated, so no validations will be made here.
        '''
        symbolsData = {'X':1,'O':2}
        coordX = dimension.getBoardX()
        coordY = dimension.getBoardY()
        self._board[coordX][coordY] = symbolsData[symbol]
        forI = [-1,-1,-1,0,1,1,1,0]
        forJ = [-1,0,1,1,1,0,-1,-1]
        for index in range(0,8):
            if coordX + forI[index] >=0 and coordX + forI[index]<self.__height and  coordY + forJ[index] >=0 and coordY + forJ[index]<self.__width:
                self._board[coordX+forI[index]][coordY+forJ[index]] = 3
                
                
