"""#una lista es una secuencia ordenada de objetos que se guarda en una variable
y pueden contener cualquier tipo de datos, incluso revueltas (string, boolean, int, float etc.)
se escriben en [] y los elemento se separan con ",", tambien pueden contener listas dentro del la lista
se pueden indexar y fraccionarlas, son manipulables(no inmutables)"""

a = ['c', 'f', 'g']
b = ["auto", 3, 4.5]
c = ["barco", "ave", "leon"]
c[0] = "foca"
d = ["amarillo", "rojo", "verde"]
d.append("blanco")


print(type(a)) #imprime el tipo de dato de la variable a
print(type(b)) #imprime el tipo de dato de la variable a
print(len(a)) #imprime el length de a
print(b[0]) #imprime el objeto con index 0 "auto"
print(a + b) #suma la lista a con la lista b
print(c) #re-emplaza el objeto "foca" por "barco" en la lista c
print(d) #añade el objeto "blanco" al principio de la lista

colores = ["morado", "anaranjado", "rosa", "rojo"]
colores2 = ["azul", "verde", "purpura", "negro"]
colores3 = colores + colores2

colores3.pop()

print(colores3) #elimina el ultimo objeto de la lista f

eliminado = colores3.pop()
print(eliminado) #imprime el objeto eliminado en lista f


lista = ["f", "h", "p", "x", "b", "m"]
lista.sort() #el metodo sort() ordena los objetos en la lista en orden alfabetico

print(lista)  #regresa ['b', 'f', 'h', 'm', 'p', 'x']

lista2 = ["f", "h", "p", "x", "b", "m"]
lista2.reverse() #el metodo reverse() ordena los objetos en la lista de atras hacia adelante

print(lista2)  #regresa ['m', 'b', 'x', 'p', 'h', 'f']


#ejercicios

'''Crea una lista con 5 elementos, dentro de la variable mi_lista. 
Puedes incluir strings, booleanos, números, etc.'''

mi_lista = ["amarillo", 5, "pato", 4.56, "avion"]


'''Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
No debes modificar la línea de código ya suministrada, 
sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.'''

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")


'''Utiliza el método pop() para quitar el tercer elemento de la siguiente lista 
llamada frutas, y almacénalo en una variable llamada eliminado. 
Utiliza métodos de listas sin alterar la línea de código ya suministrada.

manzana

banana

mango

cereza

sandía'''

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]

eliminado = frutas.pop(2)

print(eliminado) #regresa "mango"