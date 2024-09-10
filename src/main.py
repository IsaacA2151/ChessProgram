import pygame
from pygame.locals import *


pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Images
black_bishop = pygame.image.load("src/Sprites/bishop-b.png")
chess_board = pygame.image.load("src/Sprites/chess-board.png")

running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0


  screen.fill((100, 100, 100))
  screen.blit(chess_board, (100, 100))
  screen.blit(black_bishop, (100, 100))
  pygame.display.flip()

pygame.quit()