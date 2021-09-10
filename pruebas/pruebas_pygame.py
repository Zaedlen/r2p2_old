import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 30
FramesPerSecond = pygame.time.Clock()

BLACK = pygame.Color(0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

DISPLAYSURF = pygame.display.set_mode((300,300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")

pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (130, 170))
pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (170, 170))
pygame.draw.line(DISPLAYSURF, GREEN, (130, 170), (170, 170))
pygame.draw.circle(DISPLAYSURF, BLACK, (100, 50), 30)
pygame.draw.circle(DISPLAYSURF, BLACK, (200, 50), 30)
pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))

# Game Loop Begin
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    FramesPerSecond.tick(FPS)



