import pygame
from pygame.locals import *

pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
LIGHT_GREY = (200, 200, 200)
DARK_GREY = (40, 40, 40)
TIMER_WIDTH = 120
TIMER_HEIGHT = 50
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
text_font = pygame.font.SysFont('Calabri', 60)


# Sams Music
Music = pygame.mixer.Sound("Sprites/Music.Mp3")
Music.set_volume(0.03)
Music.play()

# Image
black_bishop = pygame.image.load("Sprites/bishop-b.png")
chess_board = pygame.image.load("Sprites/chess-board.png")

running = 1


while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0

  
  mouse_x, mouse_y = pygame.mouse.get_pos() # Get coordinates of mouse cursor
  screen.fill((100, 100, 100))
  screen.blit(chess_board, (91, 90))
  screen.blit(black_bishop, (270, 90))
  pygame.draw.rect(screen, LIGHT_GREY, (91, 25, TIMER_WIDTH, TIMER_HEIGHT))
  pygame.draw.rect(screen, DARK_GREY, (693, 825, TIMER_WIDTH, TIMER_HEIGHT))
  timer = pygame.time.get_ticks()/1000
  timer= 60 - round(timer, 2)
  p1_win_text = text_font.render(str(timer), False, (0,0,0))
  screen.blit(p1_win_text, (90,20))


  pygame.display.flip()
  

pygame.quit()