import piece

class Board:
    def __init__(self, size=8):
        self.size = size
        self.board = []

    def addPiece(self, player, pieceName, coord):
        if pieceName == "pawn":
            newPiece = piece.Pawn(player, coord)
        elif pieceName == "knight":
            newPiece = piece.Knight(player, coord)
        elif pieceName == "bishop":
            newPiece = piece.Bishop(player, coord)
        elif pieceName == "rook":
            newPiece = piece.Rook(player, coord)
        elif pieceName == "queen":
            newPiece = piece.Queen(player, coord)
        elif pieceName == "king":
            newPiece = piece.King(player, coord)

        self.board[coord[0]][coord[1]] = newPiece

    def makeStandardBoard(self):
        self.size = 8
        self.board = [[[] for k in range(self.size)] for i in range(self.size)]

        for i in range(self.size):
            self.addPiece(1, "pawn", [i,1])
            self.addPiece(-1, "pawn", [i,6])


            
