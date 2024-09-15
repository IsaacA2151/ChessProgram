# Player: -1 = White 1 = Black
import board

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
    

    def getAllMoves(self, board):
        pass

    def initName(self):
        self.spriteName = self.pieceName + self.colour

    def setSprite(self):
        self.initName()
        self.sprite = spriteFiles[self.spriteName]

    def getSpriteFn(self):
        return self.sprite
    
    def getPieceName(self):
        return self.pieceName
    
    def getValidMoves(self, possibleMoves, board):
        moves = []
        for i in possibleMoves:
            if self.isValidMove(i, board):
                moves.append(i)

        return moves

    def isValidMove(self, coord, board):
        if board.isWithinBounds(coord[0], coord[1]):
                if board.isOccupied(coord[0], coord[1]):
                    if board.getCell(coord[0], coord[1]).player != self.player:
                        return True
                else:
                    return True



class Pawn(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "pawn"
        self.hasMoved = False
        self.setSprite()
        self.numMoves = 0

    def getAllMoves(self, board):
        self.x, self.y = self.coord[1], self.coord[0]
        moves = []
        leftDiag, rightDiag = [self.y+self.player, self.x-1], [self.y+self.player, self.x+1]
        oneForward, twoForward = [self.y+self.player, self.x], [self.y + (self.player * 2), self.x]
        
        if board.isWithinBounds(leftDiag[0], leftDiag[1]) and board.isOccupied(leftDiag[0], leftDiag[1]):
            if board.getCell(leftDiag[0], leftDiag[1]).player != self.player:
                moves.append(leftDiag)

        if board.isWithinBounds(rightDiag[0], rightDiag[1]) and board.isOccupied(rightDiag[0], rightDiag[1]):
            if board.getCell(rightDiag[0], rightDiag[1]).player != self.player:
                moves.append(rightDiag)


        if board.isWithinBounds(oneForward[0], oneForward[1]) and board.isOccupied(oneForward[0], oneForward[1]) == False:
            moves.append(oneForward)

        if self.numMoves == 0 and board.isOccupied(twoForward[0], twoForward[1]) == False and board.isOccupied(oneForward[0], oneForward[1]) == False:
            moves.append(twoForward)

        return moves


class Knight(Piece):
    def __init__(self,player, coord):
        super().__init__(player, coord)
        self.pieceName = "knight"
        self.setSprite()

    def getAllMoves(self, board):
        self.x, self.y = self.coord[1], self.coord[0]
        possibleMoves = [[self.y+1, self.x-2], [self.y-1, self.x-2], [self.y+2, self.x-1], [self.y+2, self.x+1], [self.y-2, self.x-1], [self.y-2, self.x+1], [self.y+1, self.x+2], [self.y-1, self.x+2]]
        moves = self.getValidMoves(possibleMoves, board)

        return moves




class Bishop(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "bishop"
        self.setSprite()

    def getAllMoves(self, board):
        self.x, self.y = self.coord[1], self.coord[0]
        moves = []

        # [y, x]
        directions = [[-1, 1], [1,1], [1,-1], [-1,-1]]
        
        for y,x in directions:
            ny,nx = self.y + y, self.x+x
            while board.isWithinBounds(ny, nx):
                if board.isOccupied(ny, nx):
                    if board.getCell(ny, nx).player != self.player:
                        moves.append([ny,nx])
                    break
                else:
                    moves.append([ny,nx])

                ny += y
                nx += x

        return moves
        



class Rook(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "rook"
        self.setSprite()

    def getAllMoves(self, board):
        self.x, self.y = self.coord[1], self.coord[0]
        moves = []

        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        for y,x in directions:
            ny,nx = self.y + y, self.x+x
            while board.isWithinBounds(ny, nx):
                if board.isOccupied(ny, nx):
                    if board.getCell(ny, nx).player != self.player:
                        moves.append([ny,nx])
                    break
                else:
                    moves.append([ny,nx])

                ny += y
                nx += x

        return moves




class Queen(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "queen"
        self.setSprite()

    def getAllMoves(self, board):
        self.x, self.y = self.coord[1], self.coord[0]
        moves = []

        directions =[[-1,0], [1,0], [0,1], [0,-1], [-1, 1], [1,1], [1,-1], [-1,-1]]

        for y,x in directions:
            ny,nx = self.y + y, self.x+x
            while board.isWithinBounds(ny, nx):
                if board.isOccupied(ny, nx):
                    if board.getCell(ny, nx).player != self.player:
                        moves.append([ny,nx])
                    break
                else:
                    moves.append([ny,nx])

                ny += y
                nx += x

        return moves



class King(Piece):
    def __init__(self, player, coord):
        super().__init__(player, coord)
        self.pieceName = "king"
        self.setSprite()

    def getAllMoves(self, board):
        self.x, self.y = self.coord[1], self.coord[0]   
        possibleMoves = []
        for i in range(-1,2,1):
            for k in range(-1,2,1):
                if not (i==0 and k==0):
                    possibleMoves.append([self.y+i, self.x+k])
        moves = self.getValidMoves(possibleMoves, board)

        return moves

        