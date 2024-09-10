import piece

class Board:
    def __init__(self, size=8):
        self.size = size
        self.grid = []

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

        self.grid[coord[0]][coord[1]] = newPiece

    def getCell(self, y, x):
        return self.grid[y][x]
    
    def isOccupied(self, y, x):
        return self.getCell(y,x) != []
    

    def makeStandardBoard(self):
        self.size = 8
        self.grid = [[[] for k in range(self.size)] for i in range(self.size)]

        for i in range(self.size):
            self.addPiece(1, "pawn", [1,i])
            self.addPiece(-1, "pawn", [6,i])

        self.addPiece(1,"rook", [0,0])
        self.addPiece(1,"rook", [0,7])
        self.addPiece(-1,"rook", [7,0])
        self.addPiece(-1,"rook", [7,7])

        self.addPiece(1, "knight", [0,1])
        self.addPiece(1, "knight", [0,6])
        self.addPiece(-1, "knight", [7,1])
        self.addPiece(-1, "knight", [7,6])

        self.addPiece(1, "bishop", [0,2])
        self.addPiece(1, "bishop", [0,5])
        self.addPiece(-1, "bishop", [7,2])
        self.addPiece(-1, "bishop", [7,5])

        self.addPiece(1, "queen", [0,3])
        self.addPiece(-1, "queen", [7,3])

        self.addPiece(1, "king", [0,4])
        self.addPiece(-1, "king", [7,4])
