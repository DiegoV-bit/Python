# Conjuntos

# Impresion de un conjunto usando listas, tuplas y strings

print(set([5, 3, 2, 7, 1.6]))
print(set((1, 2, 3, 4, 5)))
print(set("Hola mundo"))

# Eliminacion de elementos repetidos dentro de un conjunto

conjunto = set([2, 3, 3, 4])
print(conjunto)

# Agregar un nuevo elemento al conjunto

conjunto.add(1)
print(conjunto)

# Eliminacion de un elemento del conjunto

conjunto.remove(1)
print(conjunto)

# Operaciones con conjuntos

conjunto_2 = set([5, 3, 2, 7])
conjunto_3 = set([4, 8])

# Interseccion

print(conjunto, conjunto_2, conjunto_3)
print(conjunto.intersection(conjunto_2))

# Elementos comunes en otros conjuntos

print(conjunto_2.issubset(conjunto))
print(conjunto_2.issubset(conjunto_3))


