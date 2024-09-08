import pygame
from pygame.locals import *

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0


  screen.fill((120, 120, 120))
  pygame.display.flip()

pygame.quit()