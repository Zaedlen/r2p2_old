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


# ----------------------------------------------------------------------------------------------------------------------



from PIL import Image
import numpy as np
import math
import time

from numpy.core.fromnumeric import shape

# Funciones auxiliares =================================================================================================
def cargarArray(ruta:str):
    with Image.open(ruta).convert('RGB') as aux:
        array = np.array(aux)

    return array


def cargarArray_pygame(ruta:str):
    array = cargarArray(ruta)
    # print(array.shape)
    array = np.rot90(array)
    array:np.ndarray = np.flipud(array)
    # print(array.dtype)
    # print(array.shape)
    return array


def guardarArray(array:np.ndarray, ruta:str):
    resultado = Image.fromarray(array)
    resultado.save(ruta)


def guardarArray_pygame(array:np.ndarray, ruta:str):
    array = np.rot90(array)
    array:np.ndarray = np.flipud(array)

    guardarArray(array, ruta)


# PINTAR LINEA =========================================================================================================
def pintarLinea(angle, ruta="lienzo.png", save="lienzo_pintado.png", x0=250, y0=250, large=50, thickness=5, color = (0,0,0)):
    array = cargarArray_pygame(ruta)
    shape = array.shape
    
    # print(array[0,0]) # pygame = (255,0,0)
    # print(array[0,-1]) # pygame = (0,0,0)
    # print(array[-1,0]) # pygame = (0,0,255)
    # print(array[-1,-1]) # pygame = (0,255,0)

    # # print(array)
    # # print(array.T)

    # # array[array != 0] = 100
    # # print(array)

    start = time.time()

    # Mario & me´s algorithm -------------------------------------------------------------------------------------------
    perpend = math.radians(angle+90)
    angle = math.radians(angle)
    perpend_cos = math.cos(perpend)
    perpend_sin = math.sin(perpend)
    angle_cos = math.cos(angle)
    angle_sin = math.sin(angle)

    pixels = [[],[]]
    for i in range(-(thickness//2), (thickness//2)+1):
        for j in range(large):
            aux_x = round((x0 + (perpend_cos * i)) + (angle_cos * j))
            aux_y = round((y0 + (perpend_sin * i)) + (angle_sin * j))
            if (aux_x >= 0) and (aux_x < shape[0]) and (aux_y >= 0) and (aux_y < shape[1]):
                pixels[0].append(aux_x)
                pixels[1].append(aux_y)
            else: break
            # print('  '*(i+2),pixels[-1])
    # print(len(pixels))
    # pixels = np.array(pixels)
    # print(pixels.shape)



    # # Bresenham's line algorithm ------------------------------------------------------------- no me convence --------
    # x1:int = round(x0 + (math.cos(angle) * large))
    # y1:int = round(y0 + (math.sin(angle) * large))

    # dx:int = abs(x1 - x0)
    # sx:int = 1 if x0 < x1 else -1
    # dy:int = -abs(y1 - y0)
    # sy:int = 1 if y0 < y1 else -1
    # err = dx + dy
    # x = x0
    # y = y0

    # pixels = [[],[]]
    # while (x0 != x1) or (y0 != y1):
    #     pixels[0].append(x0)
    #     pixels[1].append(y0)

    #     e2 = 2*err
    #     if e2 >= dy:
    #         err += dy
    #         x0 += sx
    #     if e2 <= dx:
    #         err += dx
    #         y0 += sy
     


    # # Digital Differential Analyzer algorithm ----------------------------------------------- no me convence ---------
    # x1 = x0 + (math.cos(angle) * large)
    # y1 = y0 + (math.sin(angle) * large)

    # dx = x1 - x0
    # dy = y1 - y0

    # if abs(dx) >= abs(dy):
    #     step = abs(dx)
    # else:
    #     step = abs(dy)
    # dx = dx / step
    # dy = dy / step
    # x = x0
    # y = y0

    # pixels = [[],[]]
    # i = 0
    # while i <= step:
    #     pixels[0].append(round(x))
    #     pixels[1].append(round(y))
    #     x += dx
    #     y += dy
    #     i += 1

    array[pixels[0], pixels[1]] = color
    # print(array[pixels[0][0],pixels[1][0]])
    # print(array[[3,4],[4,5]])

    # print(np.array_equal(array[pixels[0][0],pixels[1][0]],  np.array((0,0,0), dtype=np.uint8)))
    # print(np.array_equal(array[pixels[0][0],pixels[1][0]],  (0,0,0))) # Compara forma y valor de dos arrays
    # array[(array[:,:,0] == 0) & (array[:,:,1] == 0) & (array[:,:,2] == 0)] = (255,0,255) # teñir negro de magenta
    

    stop = time.time()
    print('Time:', stop-start,'s')

    guardarArray_pygame(array, save)

    return (stop - start)


# PRUEBAS PINTAR LINEA =================================================================================================

# # pintarLinea(0)
# # pintarLinea(90,ruta="lienzo_pintado.png", save="lienzo_pintado.png", color=(255,0,0))
# # pintarLinea(180,ruta="lienzo_pintado.png", save="lienzo_pintado.png", color=(0,255,0))
# # pintarLinea(270,ruta="lienzo_pintado.png", save="lienzo_pintado.png", color=(0,0,255))
# # pintarLinea(45,ruta="lienzo_pintado.png", save="lienzo_pintado.png", color=(255,255,0))

# inicio = time.time()

# pintarLinea(0, color=(255,255,255))
# count = 0
# for i in range(0,360,360//60):
#     # count += pintarLinea(i,ruta="lienzo_pintado.png", save="lienzo_pintado.png", thickness=40, large=450, color=(round((i/360)*255),round((1-(i/360))*255),round((i/360)*255)))
#     count += pintarLinea(i,ruta="lienzo_pintado.png", save="lienzo_pintado.png", thickness=1, large=200)

# print('Total time:',count,'s')

# fin = time.time()
# print('Run time:',fin-inicio,'s')



# ARRAY DE TUPLAS ======================================================================================================
def arrayTuplas(carga:str, guardado:str):
    with Image.open(carga).convert('RGB') as aux:
        array = np.array(aux)

    array = np.rot90(array)
    array:np.ndarray = np.flipud(array)

    # a = np.zeros((array.shape[0],array.shape[1]),dtype=[('R', 'u1'),('G', 'u1'),('B', 'u1')])
    a = np.zeros((array.shape[0],array.shape[1]),dtype=tuple)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            a[i,j] = (array[i,j,0], array[i,j,1], array[i,j,2])
    array = a
    print(type(array[0,0]))
    
    # a[0,0] = (255,255,255)
    # a[1,0][0] = 126
    # print(a)
    # print(a['R'])

    # print(array.T.shape)
    # array = array.T
    # array = np.array(array, dtype=dt)
    # print(array.shape)
    # print(array[0,0])

    # array.resize(400,600)
    # print(array.shape)

    # array = np.rot90(array)
    # array:np.ndarray = np.flipud(array)
    # print(array.shape)

    print(array[0,0]) # pygame = (255,0,0)
    print(array[0,-1]) # pygame = (0,0,0)
    print(array[-1,0]) # pygame = (0,0,255)
    print(array[-1,-1]) # pygame = (0,255,0)

    # lista = [[y == (255,0,0) for y in x] for x in array]
    # array[lista] = np.array((255,0,255), dtype=tuple)
    # print(array[0,0])
    aux = np.empty(1,dtype=object)
    aux[:] = [(255,0,0)]
    aux2 = np.empty(1,dtype=object); aux2[0] = (255,0,255)
    print(aux2[0])
    array[array == aux] = aux2
    print(array)

# PRUEBAS ARRAY DE TUPLAS ==============================================================================================
# arrayTuplas("lienzo.png", "lienzo_pintado.png")



# Procesar imagen para obtener objetos =================================================================================
import sys
loggedData = ""

def loggear(*args):
    global loggedData
    for a in args:
        loggedData += str(a) + ' '
    loggedData += '\n'

class Objeto():
    def __init__(self, initialPixel, id=0) -> None:
        self.pixeles = []
        self.pixeles.append(initialPixel)
        self.id = id
        loggear('      Pixel', initialPixel, 'added to Objecto', self.id)

    def addPixel(self, pixel:tuple):
        self.pixeles.append(pixel)

    def isIn(self, pixel:tuple):
        return pixel in self.pixeles

    def canBeAdded(self, pixel, image:np.ndarray):
        preX = (pixel[0] - 1) if (pixel[0] != 0) else pixel[0]
        posX = (pixel[0] + 1) if (pixel[0] != (image.shape[0]-1)) else pixel[0]
        preY = (pixel[1] - 1) if (pixel[1] != 0) else pixel[1]
        posY = (pixel[1] + 1) if (pixel[1] != (image.shape[1]-1)) else pixel[1]
        for i in range(preX, posX+1):
            for j in range(preY, posY+1):
                if ((i,j) in self.pixeles) and (pixel not in self.pixeles): return True
        return False

    def addPixel(self, pixel, image:np.ndarray):
        if self.canBeAdded(pixel, image):
            self.pixeles.append(pixel)
            loggear('      Pixel', pixel, 'added to Objecto', self.id)
            return True
        else:
            return False

    def getCoord(self):
        coordX = []
        coordY = []
        for p in self.pixeles:
            coordX.append(p[0])
            coordY.append(p[1])
        return coordX, coordY

class TipoColision():
    def __init__(self, color:tuple, pixel=None) -> None:
        self.objetos = []
        if pixel:
            self.objetos.append(Objeto(pixel))
        self.color = color
        loggear('   Created new type:', self.color)

    # def addTo
    def addPixel(self, pixel, color:tuple, image:np.ndarray):
        if self.color == color:
            added = False
            for obj in self.objetos:
                obj:Objeto
                if obj.addPixel(pixel, image):
                    added = True
                    loggear('   Type:', self.color, ' Added pixel', pixel, 'to existing Objeto', obj.id)
                    break
            if not added:
                self.objetos.append(Objeto(pixel, len(self.objetos)))
                loggear('   Type:', self.color, ' Added pixel', pixel, 'to new Objeto', len(self.objetos)-1)
            return True
        else:
            return False



def procesarImagen(carga, guardado):
    array = cargarArray_pygame(carga)
    colisiones = []
    for i in range(0, array.shape[0]):
        for j in range(0, array.shape[1]):
            if tuple(array[i,j]) != (255,255,255):
                added = False
                for tipo in colisiones:
                    tipo:TipoColision
                    if tipo.addPixel((i,j), tuple(array[i,j]), array):
                        added = True
                        loggear('Added Pixel', (i,j), 'to existing Tipo', tipo.color)
                        break
                if not added:
                    colisiones.append(TipoColision(tuple(array[i,j]), (i,j)))
                    loggear('Added Pixel', (i,j), 'to new Tipo', tuple(array[i,j]))
    

    # print(array[(0,0)])
    # print(array[(-1,-1)])
    # print(array[[0,-1],[0,-1]])
    
    
    for tipo in colisiones:
        tipo:TipoColision
        fraccion = 1 / len(tipo.objetos)
        print(255*fraccion)
        for i in range(len(tipo.objetos)):
            x,y = tipo.objetos[i].getCoord()
            array[x,y] = tuple(int(c*(i+1)*fraccion) for c in tipo.color)
            print(tuple(int(c*i*fraccion) for c in tipo.color))

    guardarArray_pygame(array, guardado)

    return colisiones
            
                        

colisiones = procesarImagen('lienzo_obstaculos.png', 'lienzo_pintado.png')
print(len(colisiones))

with open('logs.txt', 'w') as logg:
    print(loggedData, file=logg)





