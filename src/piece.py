# Player: -1 = White 1 = Black

WHITE = -1
BLACK = 1

spriteFiles = {
    "pawnW":"Sprites/pawn-w.png",
    "pawnB":"Sprites/pawn-b.png",
    "bishopW":"Sprites/bishop-w.png",
    "bishopB":"Sprites/bishop-b.png",
    "knightW":"Sprites/knight-w.png",
    "knightB":"Sprites/knight-b.png",
    "kingW":"Sprites/king-w.png",
    "kingB":"Sprites/king-b.png",
    "rookW":"Sprites/rook-w.png",
    "rookB":"Sprites/rook-b.png",
    "queenW":"Sprites/queen-w.png",
    "queenB":"Sprites/queen-b.png"
}

class Piece:

    def __init__(self,player,coord):
        self.player = player
        self.coord = coord
        self.pieceName = ""
        
        if self.player == WHITE:
            self.colour = "W"
        else:
            self.colour = "B"
    

    def checkMove(self, destination):
        pass

    def initName(self):
        self.spriteName = self.pieceName + self.colour

    def setSprite(self):
        self.initName()
        self.sprite = spriteFiles[self.spriteName]

    def getSpriteFn(self):
        return self.sprite


class Pawn(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "pawn"
        self.setSprite()


class Knight(Piece):
    def __init__(self,player, coord):
        super().__init__(player, coord)
        self.pieceName = "knight"
        self.setSprite()



class Bishop(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "bishop"
        self.setSprite()



class Rook(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "rook"
        self.setSprite()



class Queen(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "queen"
        self.setSprite()



class King(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "king"
        self.setSprite()

        