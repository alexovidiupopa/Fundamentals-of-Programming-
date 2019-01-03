
from models.board import Board 
from models.game import Game
from ui.gameSettings import Settings
from ui.ui import UserInterface

settings = Settings()
boardDimensions = settings.getDimensions()

board = Board(boardDimensions.boardX,boardDimensions.boardY)

game = Game(board)

ui = UserInterface(game)
ui.start()
