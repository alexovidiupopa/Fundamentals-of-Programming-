from errors.errors import BoardError, CoordError

class boardValidator(object):
    '''
    class for the board validator
    '''
    def validate(self, boardX, boardY):
        '''
        The function validates a x and a y, to see if they can be the dimensions of the 
        board
        in-boardX,boardY-integers
        out:-
        raises:BoardError if either one of them is negative, signaling that the 
        board dimensions cannot be negative.
        '''
        if boardX <= 0 or boardY <= 0: 
            raise BoardError("Incorrect dimensions! Must be greater than 0!")
    
    def validateCoordinates(self,boardX,boardY,board):
        '''
        The function validates if the two coordinates boardX and boardY are correctly 
        chosen on the board <board>
        in: boardX,boardY-integers
            board- an object of type Board()
        out:-
        raises: CoordError in case the coordinates are invalid
        '''
        errors = ""
        if boardX<0 or boardX>=board.getWidth() or boardY<0 or boardY>=board.getHeight():
            errors+="Coordinates must be between 0 and width/height - 1."
        if errors!="":
            raise CoordError("Coordinates error!"+errors)
        if board._board[boardX][boardY]!=0: 
            errors+="Square already taken!"
        if errors!="": 
            raise CoordError("Coordinates error!"+errors)
    