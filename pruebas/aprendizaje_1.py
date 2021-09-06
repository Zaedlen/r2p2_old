# Asi se hacen comentarios de una linea
"""
    Esto es un comentario multilinea al parecer
"""

# Uso de listas
fruta = ["pera", "platano", "manzana"] # definicion de la lista
numeros = [1, 2, 3, 4]
print(fruta[1]) # BIF para imprimir en consola. Accedemos al segundo elem de la lista
print(numeros[1])
print(len(fruta)) # BIF para averiguar la longitud de una lista
print(len(numeros))

fruta.append("uva") # method of list to add an element at the end
numeros.append(50)
numeros.append("12")
print(fruta)
print(numeros)

fruta.pop() # method to remove the last element. Last in first out
numeros.pop()
print(fruta)
print(numeros)

fruta.extend(["naranja", "melocoton"]) # method to append a collection of items to the end
numeros.extend([30, "2"])
print(fruta)
print(numeros)

fruta.remove("naranja") # method that removes the first occurrence of the given value
numeros.remove("2")
numeros.remove(2)
print(fruta)
print(numeros)

fruta.insert(2, "pomelo") # metodo que inserta el elem en la posicion dada: moviendo el que estaba ahi y todos los de despues hacia el final, hacia la derecha
numeros.insert(0, 456)
numeros.insert(2, "879")
print(fruta)
print(numeros)
