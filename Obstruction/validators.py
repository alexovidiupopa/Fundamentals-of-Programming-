from errors.errors import BoardError, CoordError

class boardValidator(object):
    
    def validate(self, boardX, boardY):
        if boardX <= 0 or boardY <= 0: 
            raise BoardError("Incorrect dimensions! Must be greater than 0!")
    
    def validateCoordinates(self,boardX,boardY,board):
        errors = ""
        if boardX<0 or boardX>=board.getWidth() or boardY<0 or boardY>=board.getHeight():
            errors+="Coordinates must be between 0 and width/height - 1."
        if errors!="":
            raise CoordError("Coordinates error!"+errors)
        #board = board._board
        if board._board[boardX][boardY]!=0: 
            errors+="Square already taken!"
        if errors!="": 
            raise CoordError("Coordinates error!"+errors)
    