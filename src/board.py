import piece

class Board:
    def __init__(self, size=8):
        self.size = size
        self.grid = []
        self.undoCoord = []
        self.justTakenPiece = None
        self.justMovedPiece = None

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

    def undoMove(self):
        self.movePiece(self.justMovedPiece, self.undoCoord)

        if self.justTakenPiece != None:
            takenPieceCoord = self.justTakenPiece.coord
            self.grid[takenPieceCoord[0]][takenPieceCoord[1]] = self.justTakenPiece
        if self.justMovedPiece.pieceName == "pawn":
            self.justMovedPiece.numMoves = self.justMovedPiece.numMoves - 1
            print(self.justMovedPiece.numMoves, self.justMovedPiece.numMoves - 1)

    def movePiece(self, selectedPiece, destination):
        pieceY, pieceX = selectedPiece.coord[0], selectedPiece.coord[1]
        destinationY, destinationX = destination[0], destination[1]

        if self.isOccupied(destinationY, destinationX):
            self.justTakenPiece = self.getCell(destinationY, destinationX)
        else:
            self.justTakenPiece = None
        self.undoCoord = [pieceY, pieceX]
        self.justMovedPiece = selectedPiece

        selectedPiece.coord = destination
        self.grid[destinationY][destinationX] = selectedPiece
        self.grid[pieceY][pieceX] = []

        if selectedPiece.pieceName == "pawn":
            selectedPiece.numMoves += 1

    def getKingCoord(self, player):
        for row in self.grid:
            for piece in row:
                if piece != []:
                    if piece.player == player and piece.pieceName == "king":
                        return piece.coord


    def getCell(self, y, x):
        return self.grid[y][x]
    
    def isOccupied(self, y, x):
        return self.getCell(y,x) != []
    
    def isWithinBounds(self, y, x):
        if x > -1 and y > -1 and x < 8 and y < 8:
            return True
        else:
            return False
    

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

    def printGrid(self):
        for i in self.grid:
            print(i)
    
    
        
