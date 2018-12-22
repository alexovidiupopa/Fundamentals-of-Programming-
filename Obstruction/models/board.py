class Board(object):
    
    '''
    Class for the Board entity
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__board = []
        self.__boardInitialize()
    
    def __boardInitialize(self):
        for i in range(self.__width): 
            row = []
            for j in range(self.__height): 
                row.append("[]")
            self.__board.append(row)
        self.boardPrint()

    def boardPrint(self):
        for i in range(self.__width): 
            for j in range(self.__height): 
                print(self.__board[i][j])
            print("\n")


