import pygame # type: ignore
from pygame.locals import * # type: ignore
import board


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
LIGHT_GREY = (200, 200, 200)
DARK_GREY = (40, 40, 40)
TIMER_WIDTH = 100
TIMER_HEIGHT = 50
CHESS_BOARD_SPRITE = pygame.image.load("Sprites/chess-board.png")
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class GameUI:

    def __init__(self, screen):
        self.cornerRenderOffset = 90
        self.cellSize = 90 

        self.screen = screen

        self.board = board.Board()
        self.board.makeStandardBoard()
        


    def renderBoard(self):
        self.screen.fill((100,100,100))
        self.screen.blit(CHESS_BOARD_SPRITE, (91,90))

        for y in range(self.board.size):
            for x in range(self.board.size):
                xCord = (x * self.cellSize) + self.cornerRenderOffset
                yCord = (y * self.cellSize) + self.cornerRenderOffset

                if self.board.isOccupied(y,x):
                    loadedSprite = pygame.image.load(self.board.getCell(y,x).getSpriteFn())
                    self.screen.blit(loadedSprite, (xCord,yCord))

        pygame.display.flip()


pygame.init()

running = 1

g = GameUI(sc)

while running:
    for event in pygame.event.get():
        if event.type == QUIT: # type: ignore
            running = 0

    g.renderBoard()

  
 