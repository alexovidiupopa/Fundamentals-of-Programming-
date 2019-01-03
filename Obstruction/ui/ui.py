from models.dimension import Dimension
from validators import boardValidator
from errors.errors import BoardError, CoordError

class UserInterface(object):

    
    def __init__(self, game):
        self.__game = game
        self.__moveValidator = boardValidator()
    
    def __readMove(self):
        while True: 
            try: 
                coordinates = input().split(' ')
                self.__moveValidator.validateCoordinates(int(coordinates[0]),int(coordinates[1]),self.__game.getBoard())
                return Dimension(int(coordinates[0]),int(coordinates[1]))
            except ValueError: 
                print("Invalid format! Must be two integers with a space between them!")
            except BoardError as be: 
                print(be)
            except CoordError as ce:
                print(ce)
                
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