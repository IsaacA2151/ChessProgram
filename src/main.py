import pygame
from pygame.locals import *


pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Images
black_bishop = pygame.transform.scale(pygame.image.load("Sprites/bishop-b.svg"), (250,250))
chess_board = pygame.transform.scale(pygame.image.load("Sprites/chess-board.png"), (0.8*SCREEN_WIDTH, 0.8*SCREEN_HEIGHT))

running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0


  screen.fill((120, 120, 120))
  screen.blit(chess_board, (100, 100))
  screen.blit(black_bishop, (100, 100))
  pygame.display.flip()

pygame.quit()