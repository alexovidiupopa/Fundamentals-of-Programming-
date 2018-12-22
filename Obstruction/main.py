
from models.board import Board 
from models.game import Game
from ui.gameSettings import Settings

settings = Settings()
boardDimensions = settings.getDimensions()

print(boardDimensions)

board = Board(boardDimensions.boardX,boardDimensions.boardY)

game = Game(board)

game.playGame()

