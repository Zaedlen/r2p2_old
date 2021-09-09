import pygame
import sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((300,300))

BLACK = pygame.Color(0,0,0)

# Game Loop Begin
while True:
    pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



