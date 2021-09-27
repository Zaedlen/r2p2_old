# import pygame
# import sys
# from pygame.locals import *

# pygame.init()

# FPS = 30
# FramesPerSecond = pygame.time.Clock()

# BLACK = pygame.Color(0,0,0)
# WHITE = (255,255,255)
# BLUE = (0,0,255)
# RED = (255,0,0)
# GREEN = (0,255,0)

# DISPLAYSURF = pygame.display.set_mode((300,300))
# DISPLAYSURF.fill(WHITE)
# pygame.display.set_caption("Example")

# pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (130, 170))
# pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (170, 170))
# pygame.draw.line(DISPLAYSURF, GREEN, (130, 170), (170, 170))
# pygame.draw.circle(DISPLAYSURF, BLACK, (100, 50), 30)
# pygame.draw.circle(DISPLAYSURF, BLACK, (200, 50), 30)
# pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
# pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))

# # Game Loop Begin
# while True:
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     FramesPerSecond.tick(FPS)



# import pygame

# pygame.init()
# window = pygame.display.set_mode((250, 250))

# sprite1 = pygame.sprite.Sprite()
# sprite1.image = pygame.Surface((80, 80), pygame.SRCALPHA)
# pygame.draw.circle(sprite1.image, (255, 0, 0), (40, 40), 40)
# sprite1.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(40, 40)
# sprite2 = pygame.sprite.Sprite()
# sprite2.image = pygame.Surface((80, 89), pygame.SRCALPHA)
# pygame.draw.circle(sprite2.image, (0, 255, 0), (40, 40), 40)
# sprite2.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(80, 80)

# all_group = pygame.sprite.Group([sprite2, sprite1])
# test_group = pygame.sprite.Group(sprite2)

# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     sprite1.rect.center = pygame.mouse.get_pos()
#     collide = pygame.sprite.spritecollide(sprite1, test_group, False, pygame.sprite.collide_circle)

#     window.fill(0)

#     pygame.draw.rect(window, (0,0,255), sprite2.rect)
    
#     all_group.draw(window)
#     for s in collide:
#         pygame.draw.circle(window, (255, 255, 255), s.rect.center, s.rect.width // 2, 5)

#     pygame.draw.rect(window, (0,0,255), sprite1.rect)

#     pygame.display.flip()

# pygame.quit()
# exit()




# import pygame, random

# class SpriteObject(pygame.sprite.Sprite):
#     def __init__(self, x, y, w, h, color):
#         pygame.sprite.Sprite.__init__(self)
#         self.angle = random.randrange(360)
#         self.original_image = pygame.Surface([w, h], pygame.SRCALPHA)
#         self.original_image.fill(color)
#         self.image = self.original_image
#         self.rect = self.image.get_rect(center = (x, y))
#         self.mask = pygame.mask.from_surface(self.image )
#     def update(self):
#         self.rotate()
#     def rotate(self):
#         self.angle += 0.3
#         self.image = pygame.transform.rotate(self.original_image, self.angle)
#         self.rect = self.image.get_rect(center = self.rect.center)
#         self.mask = pygame.mask.from_surface(self.image )

# pygame.init()
# clock = pygame.time.Clock()
# window = pygame.display.set_mode((400, 400))
# size = window.get_size()

# moving_object = SpriteObject(0, 0, 50, 50, (128, 0, 255))
# static_objects = [
#     SpriteObject(size[0] // 2, size[1] // 3, 100, 50, (128, 128, 128)),
#     SpriteObject(size[0] // 4, size[1] * 2 // 3, 100, 50, (128, 128, 128)),
#     SpriteObject(size[0] * 3 // 4, size[1] * 2 // 3, 100, 50, (128, 128, 128))
# ]
# all_sprites = pygame.sprite.Group([moving_object] + static_objects)
# static_sprites = pygame.sprite.Group(static_objects)

# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     moving_object.rect.center = pygame.mouse.get_pos()
#     all_sprites.update() 
#     collide = pygame.sprite.spritecollide(moving_object, static_sprites, False, pygame.sprite.collide_mask)
    
#     window.fill((255, 0, 0) if collide else (255, 255, 255))
#     all_sprites.draw(window)
#     pygame.display.update()

# pygame.quit()
# exit()




import pygame, random

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        pygame.sprite.Sprite.__init__(self)
        self.angle = random.randrange(360)
        self.original_image = pygame.Surface([w, h], pygame.SRCALPHA)
        self.original_image.fill(color)
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (x, y))
        self.mask = pygame.mask.from_surface(self.image )
    def update(self):
        self.rotate()
    def rotate(self):
        self.angle += 0.3
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.mask = pygame.mask.from_surface(self.image )

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../res/stage.png")
        self.mask = pygame.mask.from_surface(self.image )

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((400, 400))
size = window.get_size()

moving_object = SpriteObject(0, 0, 50, 50, (128, 0, 255))
fondo = Fondo()
fondo.rect = pygame.Rect(window.get_rect())
all_sprites = pygame.sprite.Group([fondo, moving_object])
static_sprites = pygame.sprite.Group([fondo])

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    moving_object.rect.center = pygame.mouse.get_pos()
    all_sprites.update() 
    collide = pygame.sprite.spritecollide(moving_object, static_sprites, False, pygame.sprite.collide_mask)
    
    window.fill((255, 0, 0) if collide else (255, 255, 255))
    # if collide: print('Colision')
    all_sprites.draw(window)
    # fondo.draw(window)
    # moving_object.draw(window)
    pygame.display.update()

pygame.quit()
exit()