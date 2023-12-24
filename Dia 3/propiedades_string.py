"""inmutables, concatenable, multiplicable, multilineales, calcular logintud
puede contener varias lineas de codigo"""

#los string no se pueden cambiar, son inmutables
"""cable = "rojo"
cable[0] = "R"
print(cable)"""
#cable[0] = "R"
#TypeError: 'str' object does not support item assignment

#los string son concatenables o conbinables
nombre = "Arturo"
apellido = "Ramirez"

print(nombre + " " + apellido) #Arturo Ramirez

#los Strings son multipicables
a = "caramelo"
b = "camaron"
c = a + " " + b + " "
print(c * 5)

"""Pueden tener varias lineas de codigo usando comillas triples, 
como por ejemplo un poema que sus estrofas tiene varios saltos de linea 
para ser leidos correctamente, evitando usar \n """

poema = """Mil pequeños peces blancos
como si hirviera
en color del agua"""

print(poema) #regresa las lineas con salto de linea
print("ballena" in poema) # refresara "false" valor boolean
print("zorro" not in poema) #regresera "true"
print ("peces" not in poema) #regresara "false" porque "peces" si esta en poeam (doble negacion)
print(len(poema)) #regresa la cantidad de caracteres en la variable


#ejercicios

'''Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. 
Por suerte, conoces que los strings son multiplicables 
y puedes realizar esta actividad de forma simple y elegante.'''

texto = "Repetición"

print(texto * 15)


'''Verifica si la palabra "agua" no se encuentra en el siguiente haiku. 
Debes imprimir el booleano.

Tierra mojada,
mis recuerdos de viaje
entre las lluvias'''

poema = """Tierra mojada,
mis recuerdos de viaje
entre las lluvias"""

print("agua" not in poema) # regresa "true"


"""Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista"""

word = "electroencefalografista"

print(len(word)) #regresa 23