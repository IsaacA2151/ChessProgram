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

    def showMoves(self):
        for move in self.currentlyShowing:
            boardX, boardY = self.getCellCentre(move[1], move[0])
            pygame.draw.circle(self.screen, LIGHT_GREY, (boardX, boardY), self.cellSize*0.25)


    def handleClick(self, mouseX, mouseY, turn):
        gridX, gridY = self.getGridPos(mouseX, mouseY)
        
        if gridX > -1 and gridX < 8 and gridY > -1 and gridY < 8:
            
            if self.showingMoves and [gridY, gridX] in self.currentlyShowing:
                self.board.movePiece(self.currentPiece, [gridY, gridX])
                self.showingMoves = False

            else:
                if self.board.isOccupied(gridY, gridX):
                    self.currentPiece = self.board.getCell(gridY, gridX)
                    print(self.currentPiece.coord)
                    possibleMoves = self.currentPiece.getAllMoves(self.board)
                    

                    

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
turn = -1

g = Game(sc)

while running:
    for event in pygame.event.get():
        if event.type == QUIT: # type: ignore
            running = 0
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            g.handleClick(mouseX, mouseY, turn)

    g.renderBoard()


  
 