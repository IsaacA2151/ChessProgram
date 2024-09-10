import pygame
from pygame.locals import *


pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


Music = pygame.mixer.Sound("src/Sprites/Music.Mp3")
Music.set_volume(0.03)
Music.play()


# Image
black_bishop = pygame.image.load("src/Sprites/bishop-b.png")
chess_board = pygame.image.load("src/Sprites/chess-board.png")

running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0

  mouse_x, mouse_y = pygame.mouse.get_pos() # Get coordinates of mouse cursor
  screen.fill((100, 100, 100))
  screen.blit(chess_board, (91, 90))
  screen.blit(black_bishop, (90, 90))
  pygame.display.flip()
  

pygame.quit()