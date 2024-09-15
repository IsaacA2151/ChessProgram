import pygame # type: ignore
from pygame.locals import * # type: ignore
import board


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
LIGHT_GREY = (100,100,100)
DARK_GREY = (40, 40, 40)
TIMER_WIDTH = 100
TIMER_HEIGHT = 50
CHESS_BOARD_SPRITE = pygame.image.load("Sprites/chess-board.png")
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Game:

    def __init__(self, screen):
        self.cornerRenderOffset = 90
        self.cellSize = 90 
        self.screen = screen
        self.showingMoves = False
        self.currentlyShowing = None

        self.board = board.Board()
        self.board.makeStandardBoard()

        self.currentPiece = None
        
    def getScreenPos(self, gridX, gridY):
        return (self.cellSize * gridX) + self.cornerRenderOffset, (self.cellSize * gridY) + self.cornerRenderOffset
    
    def getGridPos(self, screenX, screenY):
        return (screenX - self.cornerRenderOffset) // self.cellSize, (screenY - self.cornerRenderOffset) // self.cellSize
    
    def getCellCentre(self, gridX, gridY):
        return (self.cornerRenderOffset * gridX) + (self.cellSize / 2) +  self.cornerRenderOffset, (self.cornerRenderOffset * gridY) + (self.cellSize / 2) +  self.cornerRenderOffset

    def wouldBeInCheck(self, move, piece, player):
        return False

    def isInCheck(self, player):
        # index 0 is whites moves, 1 is black
        allPlayerMoves = [[],[]]

        for row in self.board.grid:
            for piece in row:
                if piece != []:
                    if piece.pieceName != "king":
                        moves = piece.getAllMoves(self.board)

                        if piece.player == -1:
                            index = 0
                        else:
                            index = 1

                        for i in moves:
                            allPlayerMoves[index].append(i)

        whiteKingCoord = self.board.getKingCoord(-1)
        blackKingCoord = self.board.getKingCoord(1)
        print(allPlayerMoves[0])
        print("\n\n\n")
        print(blackKingCoord)

        if player == -1 and whiteKingCoord in allPlayerMoves[1]:
            return True
        elif player == 1 and blackKingCoord in allPlayerMoves[0]:
            return True
        else:
            return False

    def showMoves(self):
        for move in self.currentlyShowing:
            boardX, boardY = self.getCellCentre(move[1], move[0])
            pygame.draw.circle(self.screen, LIGHT_GREY, (boardX, boardY), self.cellSize*0.25)

    def findPossibleMoves(self, piece):
        moves = []
        possibleMoves = piece.getAllMoves(self.board)
        for move in possibleMoves:
            if not self.wouldBeInCheck(move, piece, -1):
                moves.append(move)

        return moves

    def switchPlayer(self, player):
        if player == -1:
            player = 1
        elif player == 1:
            player = -1
        return player

    def handleClick(self, mouseX, mouseY, player, swap):
        gridX, gridY = self.getGridPos(mouseX, mouseY)
        
        if gridX > -1 and gridX < 8 and gridY > -1 and gridY < 8:
            
            if gridX == 0 and gridY == 0:
                self.board.undoMove()

            elif self.showingMoves and [gridY, gridX] in self.currentlyShowing:
                self.board.movePiece(self.currentPiece, [gridY, gridX])
                self.showingMoves = False
                swap = True
                return swap

            else:
                if self.board.isOccupied(gridY, gridX):
                    self.currentPiece = self.board.getCell(gridY, gridX)
                    if self.currentPiece.colour == "W" and player == -1 or self.currentPiece.colour == "B" and player == 1:
                        possibleMoves = self.findPossibleMoves(self.currentPiece)                    
                        self.showingMoves = True
                        self.currentlyShowing = possibleMoves







    def renderBoard(self):
        self.screen.fill((100,100,100))
        self.screen.blit(CHESS_BOARD_SPRITE, (91,90))

        for y in range(self.board.size):
            for x in range(self.board.size):
                xCord, yCord = self.getScreenPos(x,y)

                if self.board.isOccupied(y,x):
                    loadedSprite = pygame.image.load(self.board.getCell(y,x).getSpriteFn())
                    self.screen.blit(loadedSprite, (xCord,yCord))
        
        if self.showingMoves:
            self.showMoves()

        pygame.display.flip()


pygame.init()

running = 1
player = -1
swap = False

g = Game(sc)

while running:
    for event in pygame.event.get():
        if event.type == QUIT: # type: ignore
            running = 0
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            swap = g.handleClick(mouseX, mouseY, player, swap)
            if swap:
                player = g.switchPlayer(player)
    g.renderBoard()


  
 