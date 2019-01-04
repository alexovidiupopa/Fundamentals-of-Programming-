
from models.board import Board 
from models.game import Game
from ui.gameSettings import Settings
from ui.ui import UserInterface

'''
getting the board dimensions
'''
settings = Settings()
boardDimensions = settings.getDimensions()

'''
initalizing the board
'''
board = Board(boardDimensions.boardX,boardDimensions.boardY)

'''
initializing the game
'''
game = Game(board)

'''
starting the game
'''
ui = UserInterface(game)
ui.start()
