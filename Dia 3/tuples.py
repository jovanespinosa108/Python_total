"""Los Tuples son inmutables, no se pueden cambiar, se escriben con o sin ( ) parentesis
son parecidos a las Listas pero los Tuples usan menos memoria por lo que son mas
rapidos de ejecutar, a prueba de daños, pueden tener todo tipo de objetos"""

mi_tuple = (1, 2, 3, 4)
print(type(mi_tuple)) #imprime el tipo the objeto
print(mi_tuple) #imprime el tuple
mi_tuple = list(mi_tuple) #un tuple puede cambiar de tuple a list y visceversa

#asignar el contenido de un taple a diferentes variables

asign_content = (5,6.7,9,14.35)
a,b,c,d = asign_content

print(a,b,c,d) #la cantidad de objetos en el tuple debe ser igual al de las variables para que funcione

#metodos index and count 
#count ayuda a contar el numero de apariciones en el tuple de cierto valor
#index ayuda a consulta el numero de indice del objeto buscado

count_tuple = (5,8,3,5,4,5)
print(count_tuple.count(5)) #regresa 3 por que el 5 se repite 3 veces

indice_tuple = ('perro', 'gato', 'pato', 'cabra', 'vaca')
print(indice_tuple.index('gato')) #regresa el index del objeto "gato" en este caso es el 3


#Ejercicios
"""Utiliza un método de tuplas para contar la cantidad de veces 
que aparece el valor 2 en la siguiente tupla, 
y muestra el resultado (integer) en pantalla: """

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(mi_tupla.count(2)) #regresa 6 veces aparece el numero 2

"""Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista."""

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

mi_tupla = list(mi_tupla)

print(type(mi_tupla))

mi_lista = mi_tupla

print(mi_tupla)


"""Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d"""

mi_tupla2 = (1, 2, 3, 4)

a, b, c, d = mi_tupla2

print(a,b,c,d)