# import pygame

# class Fondo(pygame.sprite.Sprite):
#     def __init__(self, image):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = image
#         # self.image.set_colorkey('#FFFFFF')
#         self.rect = self.image.get_rect()
#         # self.mask = pygame.mask.from_surface(self.image )



# pygame.init()
# clock = pygame.time.Clock()

# image = pygame.image.load("stage_color.png")

# window = pygame.display.set_mode(image.get_size())

# fondo = Fondo(image)



# all_sprites = pygame.sprite.Group(fondo)


# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     window.fill('#00FF00')
#     all_sprites.draw(window)

#     pygame.display.update()

# pygame.quit()
# exit()

# from PIL import Image

# with Image.open("stage_color.png").convert('P') as aux:
#     # aux.convert('P')
#     # print(aux.palette.palette)
#     im = aux.load()
#     width, height = aux.size


# a = set()
# for i in range(width):
#     for j in range(height):
#         a.add(im[i,j])

# print(a)


# from PIL import Image
# import numpy as np

# PALETTE = [
#     0,   0,   0,  # black,  00
#     0,   255, 0,  # green,  01
#     255, 0,   0,  # red,    10
#     255, 255, 0,  # yellow, 11
# ]

# with Image.open("stage_color.png") as aux:
#     paleta = Image.new("P", (1, 1), 0)
#     paleta.putpalette(PALETTE)
#     aux = aux.convert('RGB')
#     im = aux.quantize(4, palette=paleta)

# a = set()
# for i in range(im.width):
#     for j in range(im.height):
#         a.add(im.load()[i,j])

# print(a)

# im.save('temp.png')



# PRUEBA = [
#     [
#         [  0,  0,  0],
#         [  0,  0,  0],
#         [  0,  0,  0],
#         [  0,  0,  0]
#     ],
#     [
#         [  0,  0,  0],
#         [255,255,  0],
#         [  0,  0,255],
#         [  0,  0,  0]
#     ],
#     [
#         [  0,  0,  0],
#         [255,  0,  0],
#         [255,255,255],
#         [  0,  0,  0]
#     ],
#     [
#         [  0,  0,  0],
#         [  0,  0,  0],
#         [  0,  0,  0],
#         [  0,  0,  0]
#     ]
# ]

# array = np.array(PRUEBA, dtype=np.uint8)
# res = Image.fromarray(array)
# res.save("prueba.png")


# with Image.open("stage_color.png").convert('RGB') as aux:
# # with Image.open("prueba.png").convert('RGB') as aux:
#     array = np.array(aux)

# print(array.shape)
# # print(array)
# # print(array.T)

# red, green, blue = array.T

# objetivo_negro = (red != 0) | (green != 0) | (blue != 0) # En este caso todo lo que no es negro (0, 0, 0)
# objetivo_rojo = (red != 255) | (green != 0) | (blue != 0) # En este caso todo lo que no es rojo (255, 0, 0)
# objetivo_amarillo = (red != 255) | (green != 255) | (blue != 0) # En este caso todo lo que no es amarillo (255, 255, 0)
# objetivo_azul = (red != 0) | (green != 0) | (blue != 255) # En este caso todo lo que no es azul (0, 0, 255)
# # print(objetivo_negro)
# negro = array.copy()
# rojo = array.copy()
# amarillo = array.copy()
# azul = array.copy()

# negro[objetivo_negro.T] = (255, 255, 255) # Si objetivo_negro es todo lo que no es negro; pues coloreamos todo lo que no es negro de blanco
# rojo[objetivo_rojo.T] = (255, 255, 255)
# amarillo[objetivo_amarillo.T] = (255, 255, 255)
# azul[objetivo_azul.T] = (255, 255, 255)

# # print(red)

# # print(array[...,:-1])

# # array[array != 0] = 100
# # print(array)


# # transformador = np.zeros([256,3], dtype=np.uint8)
# # # print(transformador)
# # # transformador[255] = 255
# # # transformador[129] = 255

# # pixels = transformador[array]
# # print(pixels.shape)
# # # print(pixels)


# resultado = Image.fromarray(negro)
# resultado.save('negro.png')
# resultado = Image.fromarray(rojo)
# resultado.save('rojo.png')
# resultado = Image.fromarray(amarillo)
# resultado.save('amarillo.png')
# resultado = Image.fromarray(azul)
# resultado.save('azul.png')


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

# class Fondo(pygame.sprite.Sprite):
#     def __init__(self, image):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = image
#         self.image.set_colorkey('#FFFFFF')
#         self.rect = self.image.get_rect()
#         self.mask = pygame.mask.from_surface(self.image)



# pygame.init()
# clock = pygame.time.Clock()

# image = pygame.image.load("negro.png")

# window = pygame.display.set_mode(image.get_size())

# moving_object = SpriteObject(0, 0, 50, 50, (128, 0, 255))

# negro = Fondo(image)
# image = pygame.image.load("rojo.png")
# rojo = Fondo(image)
# image = pygame.image.load("amarillo.png")
# amarillo = Fondo(image)
# image = pygame.image.load("azul.png")
# azul = Fondo(image)
# # fondo.rect = pygame.Rect(window.get_rect())

# moving = pygame.sprite.Group(moving_object)
# sprite_negro = pygame.sprite.Group(negro)
# sprite_rojo = pygame.sprite.Group(rojo)
# sprite_amarillo = pygame.sprite.Group(amarillo)
# sprite_azul = pygame.sprite.Group(azul)

# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     moving_object.rect.center = pygame.mouse.get_pos()
#     moving.update()
#     sprite_negro.update()
#     sprite_rojo.update()
#     sprite_amarillo.update()
#     sprite_azul.update() 
#     collide_negro = pygame.sprite.spritecollide(moving_object, sprite_negro, False, pygame.sprite.collide_mask)
#     collide_rojo = pygame.sprite.spritecollide(moving_object, sprite_rojo, False, pygame.sprite.collide_mask)
#     collide_amarillo = pygame.sprite.spritecollide(moving_object, sprite_amarillo, False, pygame.sprite.collide_mask)
#     collide_azul = pygame.sprite.spritecollide(moving_object, sprite_azul, False, pygame.sprite.collide_mask)
    
#     # window.fill((255, 0, 0) if collide else (255, 255, 255))
#     if collide_negro: window.fill('purple')
#     elif collide_rojo: window.fill('red')
#     elif collide_amarillo: window.fill('yellow')
#     elif collide_azul: window.fill('blue')
#     else: window.fill('white')
#     # if collide: print('Colision')
#     # all_sprites.draw(window)
#     sprite_negro.draw(window)
#     sprite_rojo.draw(window)
#     sprite_amarillo.draw(window)
#     sprite_azul.draw(window)
#     moving.draw(window)
#     # fondo.draw(window)
#     # moving_object.draw(window)
#     pygame.display.update()

# pygame.quit()
# exit()


parametros = {
    (255,0,0): [(4,5),(0,3),(5,8)],
    'a': 3
}

class pruebaP():
    def __init__(self) -> None:
        # # Hard copy
        # self.parametros = {**parametros}
        # self.parametros = dict(parametros)
        # self.parametros = parametros.copy()

        # Only reference:  --mejor--
        self.parametros = parametros

    def getParametro(self, key):
        return self.parametros[key]

    def setParametro(self, key, value):
        self.parametros[key] = value

a = pruebaP()

print(parametros)
print(a.getParametro((255, 0, 0)))
print(a.getParametro('a'))

a.setParametro('a', 5)

print(a.getParametro('a'))
print(parametros)
