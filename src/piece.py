# Player: -1 = White 1 = Black

spriteFiles = {
    "Pawn":
}

class Piece:

    def __init__(self,player,coord):
        self.player = player
        self.coord = coord

    def checkMove(self, destination):
        pass


class Pawn(Piece):
    def __init__(self, spriteFn, player, coord):
        super().__init__(spriteFn, player, coord)



class Knight(Piece):
    def __init__(self, spriteFn, player, coord):
        super().__init__(spriteFn, player, coord)



class Bishop(Piece):
    def __init__(self, spriteFn, player, coord):
        super().__init__(spriteFn, player, coord)



class Rook(Piece):
    def __init__(self, spriteFn, player, coord):
        super().__init__(spriteFn, player, coord)



class Queen(Piece):
    def __init__(self, spriteFn, player, coord):
        super().__init__(spriteFn, player, coord)



class King(Piece):
    def __init__(self, spriteFn, player, coord):
        super().__init__(spriteFn, player, coord)

        