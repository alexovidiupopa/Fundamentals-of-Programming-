from models.dimension import Dimension
from validators import boardValidator
from errors.errors import BoardError

class UserInterface(object):

    
    def __init__(self, game):
        self.__game = game
    
    def __readMove(self):
        while True: 
            try: 
                coordinates = input().split(' ')
                boardValidator.validateCoordinates(int(coordinates[0]),int(coordinates[1]))
                return Dimension(int(coordinates[0]),int(coordinates[1]))
            except BoardError as be: 
                print(be)
                
    def start(self):
        board = self.__game.getBoard()
        human = True
        while board.isWon() == False: 
            if human: 
                print(board)
                move = self.__readMove()
                self.__game.moveHuman(move)
            else: 
                self.__game.moveComputer()
            human = not human
        print("Game over!")
        print(board)
        if human == True: 
            print("Computer wins!")
        else: 
            print("Human wins!")