from models.dimension import Dimension
from errors.errors import BoardError, CoordError

class UserInterface(object):

    
    def __init__(self, game):
        self.__game = game
    
    def __readMove(self):
        while True: 
            try: 
                print("Input the move you want to make! Format must be x <space> y !!")
                print(">>>")
                coordinates = input().split(' ')
                return Dimension(int(coordinates[0]),int(coordinates[1]))
            except ValueError: 
                print("Invalid format! Must be two integers with a space between them!")
    def start(self):
        print("Let's play! Human starts!")
        board = self.__game.getBoard()
        human = True
        print(board)
        while not board.isWon(): 
            if human: 
                move = self.__readMove()
                try:
                    self.__game.moveHuman(move)
                    human = False
                    print("Human moved. Board now is:")
                    print(board)
                    print("-"*50)
                except BoardError as be: 
                    print(be)
                except CoordError as ce:
                    print(ce)
            else: 
                self.__game.moveComputer()
                human = True
                print("Computer moved. Board now is:")
                print(board)
                print("-"*50)
        print("Game over!")
        print(board)
        if human == True: 
            print("Computer wins!")
        else: 
            print("Human wins!")