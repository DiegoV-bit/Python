# Diccionario

diccionario = {1 : "Uno", 2 : "Dos", 3 : "Tres"}
print(diccionario)

# Acceder a un elemento y mostrar el valor que tiene ese elemento

print(diccionario[2])

# Agregar un nuevo elemento al diccionario

diccionario[4] = "Cuatro"
print(diccionario)

# Tambien podemos crear un diccionario con la funcion dict()

dict_lista_tuplas = dict([(1, "uno"), (2, "dos"), (3, "tres")])
print(dict_lista_tuplas)

# Para hacerlo con un string se tiene que hacer de esta forma

dict_lista_string = dict(Uno = 1, Dos = 2, Tres = 3)
print(dict_lista_string)

# Se puede poner cualquier tipo de dato como valor, pero la clave al ser un ID este debe ser inmutable

dict_tipos = {1 : "Integer", 2.2 : "Float", "Texto" : "String", (1, 2) : "Tupla"}
print(dict_tipos)

# Si la clave se repite se toma el valor de la ultima repeticion

dict_repeticion = {1 : "Primero", 2 : "Ultimo"}
print(dict_repeticion)

# Los metodos que tiene los diccionarios son 

print(diccionario, diccionario.keys(), diccionario.values(), diccionario.items())

# Si guardamos algunos de los metodos en una variable y modificamos algo del diccionario el cambio hecho se reflejara en la variable que se guardo

claves = diccionario.values()
print(claves)
diccionario[1] = "One"
print(claves)

# Si queremos eliminar una clave del diccionario usaremos
diccionario.pop(2)
print(diccionario)
