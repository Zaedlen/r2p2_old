# Asi se hacen comentarios de una linea
"""
    Esto es un comentario multilinea al parecer

    Parece que en python se comenta dentro: el comentario de una funcion se incluye
    despues de la sentencia def de esta y antes de la logica:
    def miFuncion():
        <Comentario (normalmente multilinea)>
        Logica de la funcion
"""

# # Uso de listas ==============================================================================================================================
# fruta = ["pera", "platano", "manzana"] # definicion de la lista
# numeros = [1, 2, 3, 4]
# print(fruta[1]) # BIF para imprimir en consola. Accedemos al segundo elem de la lista
# print(numeros[1])
# print(len(fruta)) # BIF para averiguar la longitud de una lista
# print(len(numeros))

# fruta.append("uva") # method of list to add an element at the end
# numeros.append(50)
# numeros.append("12")
# print(fruta)
# print(numeros)

# fruta.pop() # method to remove the last element. Last in first out
# numeros.pop()
# print(fruta)
# print(numeros)

# fruta.extend(["naranja", "melocoton"]) # method to append a collection of items to the end
# numeros.extend([30, "2"])
# print(fruta)
# print(numeros)

# fruta.remove("naranja") # method that removes the first occurrence of the given value
# numeros.remove("2")
# numeros.remove(2)
# print(fruta)
# print(numeros)

# fruta.insert(2, "pomelo") # metodo que inserta el elem en la posicion dada: moviendo el que estaba ahi y todos los de despues hacia el final, hacia la derecha
# numeros.insert(0, 456)
# numeros.insert(2, "879")
# print(fruta)
# print(numeros)


# Python Built In Functions or BIF ================================================================================================
# print(dir(__builtins__))
# print(len(dir(__builtins__)))


# Bucles en Python ===========================================================================================================================================================
#   FOR
# fruta = ["platano", "pera", "manzana"]
# for f in fruta:
#     print(f)

# Control de flujo ================================================================================================================================================
# IF
# numero = 3
# if numero < 5:
#     print("Numero es menor que 5")

# print(type(numero))
# print(isinstance(numero, int))

# if isinstance(numero, int): print("Numero es un int")


# # Punteros en Python (?) ===============================================================================================================================
# Al parecer Python tiene Garbage Collector. En principio Dont worry. Solo atento 
# a las buenas practicas en cuanto a naming y eso 

# Mirar info al respecto pero en principio el GC es por contador de referencias y 
# generacional:
# https://stackify.com/python-garbage-collection/
# https://docs.python.org/3/library/gc.html
# https://stackoverflow.com/questions/1316767/how-can-i-explicitly-free-memory-in-python

# ejemplo = [1,2,3,4]
# copia_mal_1 = ejemplo
# copia_mal_2 = ejemplo
# copia_bien = ejemplo[:]
# print("Ejemplo: ", ejemplo)
# print("Copia bien: ", copia_bien)
# print("Copia mal 1: ", copia_mal_1)
# print("Copia mal 2: ", copia_mal_2)

# # ejemplo.clear()
# # print("Ejemplo: ", ejemplo)
# # print("Copia bien: ", copia_bien)
# # print("Copia mal 1: ", copia_mal_1)
# # print("Copia mal 2: ", copia_mal_2)

# # ejemplo = 5
# # print("Ejemplo: ", ejemplo)
# # print("Copia bien: ", copia_bien)
# # print("Copia mal 1: ", copia_mal_1)
# # print("Copia mal 2: ", copia_mal_2)
# # copia_mal_1.clear()
# # print("Ejemplo: ", ejemplo)
# # print("Copia bien: ", copia_bien)
# # print("Copia mal 1: ", copia_mal_1)
# # print("Copia mal 2: ", copia_mal_2)

# del ejemplo
# try: print("Ejemplo: ", ejemplo)
# except: print("Ejemplo ya no existe")
# try: print("Copia bien: ", copia_bien)
# except: print("Copia bien ya no existe")
# try: print("Copia mal 1: ", copia_mal_1)
# except: print("Copia mal 1 ya no existe")
# try: print("Copia mal 2: ", copia_mal_2)
# except: print("Copia mal 2 ya no existe")

# del copia_mal_1
# try: print("Ejemplo: ", ejemplo)
# except: print("Ejemplo ya no existe")
# try: print("Copia bien: ", copia_bien)
# except: print("Copia bien ya no existe")
# try: print("Copia mal 1: ", copia_mal_1)
# except: print("Copia mal 1 ya no existe")
# try: print("Copia mal 2: ", copia_mal_2)
# except: print("Copia mal 2 ya no existe")

# # https://realpython.com/python-pass/


# Funciones en Python ===============================================================================================
# ejemplo = ["hola", "que", "ases", ["esto", "es", "una", "lista", ["dentro", "de", "otra", ["lista"]]]]
# print(ejemplo)

# def imprimirLista(lista):
#     for elem in lista:
#         if isinstance(elem, list): imprimirLista(elem)
#         else: print(elem)

# imprimirLista(ejemplo)

# # Limite de recursividad por defecto en Python es de 1000 !!!!

# ARGUMENTOS OPCIONALES
# def funcion(argumetoObligatorio, argumentoOpcional = 3):
#     bla bla bla 



# Crear un modulo y una distribucion en python ========================================================================================
# Modulo = archivo texto con extension .py
# La libreria standard se instala con python y ya tiene muchos modulos 
# En la web existe el llamado Python Package Index o PyPI donde es incluso posible 
# publicar tus propios modulos para que cualquiera pueda usarlos 

# Distribution = coleccion de archivos que permiten hacer build, package y la distribucion del modulo 
# Pasos para crear la distribucion: 
#     1. Crear una carpeta. En principio el nombre da igual. Hacerlo con sentido 
#     Meter dentro el modulo .py 

#     2. Crear tambien el archivo setup.py con metadatos de la distribucion. Ejemplo: 
#         from distutils.core import setup # importamos funcion setup y la llamammos:

#         setup(
#             name = 'nester',
#             version = '1.0.0',
#             py_modules = ['nester'], # Se supone que el archivo .py con la funcion, el modulo, se llama nester.py
#             author = 'me',
#             author_email = 'me@sisoy.com',
#             url = 'http://www.unapaginaweb.com',
#             description = 'Una descripcion'
#         )

#     3. Buildear el archivo de distribucion. Con un termnal con python ejecutamos, dentro de la carpeta, el setup.py:
#         python setup.py sdist # investigar si hay algun otro comando para esto. Por que sdist

#     4. Instalar la distribucion en la copia local de python (similar al PIP?):
#         python setup.py install # parece que con un argumento creamos la distribucion y con el otro la instalamos ?

#     5. Tras crear la distribucion y tal, en la carpeta han aparecido otros archivos:
#         - Archivo(?) MANIFEST con lista archivos de la distribucion 
#         - Carpeta build y dentro carpeta lib y dentro una copia del modulo nester.py 
#         - Carpeta dist con una version comprimida de la distribucion 
#             nester-1.0.0.tar.gz 
#         - Archivo nester.py original
#         - Archivo setup.py original 
#         - Archivo nester.pyc con una version compilada (similar al bytecode de java) 

# Para subir nuestra distribucion a PyPI necesitamos tener una cuenta en pypi.python.org y utilizar:
#     python setup.py register 
# Nos pedira en la consola que hagamos login y tal y ya esta registrada la distribucion. Despues usamos: 
#     python setup.py sdist upload 
# Y asi subimos esa version de la distribucion y ya forma parte de PyPI

# Importar un modulo en Python ==================================================================================================
# Una vez instalada una distribucion en nuestro python local podemos usar la palabra
# import nester para importar ese modulo en concreto incluyendo asi el modulo nester.py en el programa 
# y pudiendo usar ahora las funciones aunque... 

# LOS MODULOS PYTHON IMPLEMENTAN NAMESPACES 

# El codigo de tu main program en python esta asociado al namespace __main__ 
# Las funciones de nester.py estaran en el namespae de nester, por lo que para usarlas 
# sera necesario utilizar nester.funcion() 

# Pero si usamos from nester import funcion, dicha funcion especifica es añadida 
# al namespace actual SOBREESCRIBIENDO otra del mismo nombre en ese namespace si ya la hubiera, cuidado


