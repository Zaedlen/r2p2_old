# import numpy as np

# a = [1,2]
# b = ([5] * len(a))

# print(a)
# print(b)

# def get_discrete_size(state):
#         discrete_state = (np.array(state) - b) / [2, 2]
#         return discrete_state.astype(np.int).tolist()

# print(get_discrete_size(a))


# def get_discrete_velocities(high, low = 0.0):
#     discrete_actions_number = 4
#     veloc = [low]
#     for i in range(1, discrete_actions_number):
#         veloc.append(i * (high/(discrete_actions_number - 1)))
#     return veloc

# print(get_discrete_velocities(7))

# def combine_actions(veloc_list, ang_list):
#         resultado = []
#         for i in veloc_list:
#             for j in ang_list:
#                 resultado.append([i, j])
#         return resultado

# actions = combine_actions([1,2,3], [4,5,6])
# print(actions)
# for i in actions:
#     print(i)

# print(actions[0])

# a = 5
# print(a)
# print(type(a))
# a = 'a'
# print(a)
# print(type(a))


# import sys
# for line in sys.stdin:
#     if 'Exit' == line.rstrip():
#         break
#     print(f'Processing Message from sys.stdin *****{line}*****')
# print("Done")


# from sys import argv
# print(__name__)
# print(argv)



# dic1 = {'a': 3, 'b': 4}
# dic2 = {'c': 1, 'd': 2}
# dic3 = {**dic1, **dic2}

# print(dic1)
# print(dic2)
# print(dic3)
# print(*dic1)



# import json

# with open('pruebaJson.json', 'r') as f:
#     lectura:dict = json.loads(f)

# for key in lectura:
#     print(key, type(lectura[key]))
#     print(lectura[key] == None)
#     if not lectura[key]: print("Cachis")




# import aprendizaje_1
# from subdirectorio import modulo

# # modulo.hola()

# # print(aprendizaje_1.uno)
# a = aprendizaje_1.Carla()
# # print(a.tres)

# all_v = dir()
# b = eval('aprendizaje_1')
# # print(dir(aprendizaje_1))



import inspect as i
import typing as t
import functools as f

class ejemplo():
    def __init__(self) -> None:
        self.saludo = 'soy ejemplo'

    # def hola(self, primero:int, segundo:t.Union[t.Any, int]) -> None: 
    #     print(self.saludo)

    def hola(self): 
        print(self.saludo)

class ejemplo2(ejemplo):
    def __init__(self) -> None:
        ejemplo.__init__(self)
        self.saludo = 'soy ejemplo 2'
        self.otro = 'just 2'

    # def hola(self, primero: int, segundo: t.Union[t.Any, int]) -> None:
    #     print(self.)

    def hola(self):
        ejemplo.hola(self)
        print(self.otro)


# signatura = i.signature(ejemplo.hola)
# print(signatura.parameters)


a = ejemplo2()          # instanciamos a como ejemplo2
a.hola()                # hola() de ejemplo2 -> imprime 'soy ejemplo 2' y 'just 2'
b = ejemplo()           # instanciamos b como ejemplo
b.hola()                # hola() de ejemplo -> imprime 'soy ejemplo'
ejemplo.hola(a)         # accedes al metodo desde fuera because I dont give a f*** dando la referencia para que funcionen los calls a self -> imprime 'soy ejemplo' porque llamamos al hola() de ejmplo con una referencia a ejemplo2 (a) que hereda de ejemplo
ejemplo.hola(b)         # lo mismo pero ahora le referencia a self es b, por lo que el hola() es de b -> imprime 'soy ejemplo'
ejemplo2.hola(a)        # accedes al metodo hola() de ejemplo2 con a, una instancia de ejemplo2, todo correcto. b con esto falla porque usa hola de ejemplo2 como dice y a el le falta el atributo otro
ejemplo2.__init__(b)    # como con b no funciona, pues lo metemos en el constructor de ejemplo2 y a b se le añaden o sobreescriben todas las cosas para ser ejemplo2. A tomar por c***
ejemplo2.hola(b)        # ahora si llamamos a hola() de ejmplo2 con la instancia de b, no peta
b.hola()                # y si vemos cual es ahora su hola() pues resulta que se ha sobreescrito y ahora es el hola() ejemplo2



