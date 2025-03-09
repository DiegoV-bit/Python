# listas

lista = [39595, True, 2.71, "Rottweiler"]

print(lista)

# Imprimir cada uno de los elementos de la lista

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4]) Como no existe el elemento 4 en el programa python devuelve un error

# Imprimir con los indices negativos (esto imprime desde el ultimo elemento de la lista hasta el primero)

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

# Imprimir sublista

print(lista[1:3])
print(lista[0:2])

# Cambiar un elemento existente de la lista

lista[2] = "Se cambio este elemento"
print(lista)

# Agregar un nuevo miembro a la lista

lista.append(2.71)
lista.append(39595)
print(lista)

# Veces que se repite un miembro de la lista

print(lista.count(39595))

# Saber la primera aparicion de un elemento de la lista (Esto devuelve la posicion en la lista)

print(lista.index(39595))

# Eliminar la primera aparicion de un elemento de la lista

lista.remove(39595)
print(lista)
