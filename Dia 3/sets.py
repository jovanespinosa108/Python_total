"""Los Sets se declaran de 2 maneras,
set(1,2,3,4,5) o solo { 1,2,3,4,5 } declarando las llaves
sin palabra clave, cuando se usa set() python solo aceptara un argumento
si queremos mas de un argumento deben de estar dentro de unos corchetes o cualquier tipo de llaves
set([1,2,3,4]), cuando declaras {} python acepta multiples parametros
los set tienen objetos unicos, son inmutables, los duplicados son descartados
automaticamente, no se ordenan en index, se almacenan diferentes tipos de datos
no admiten listas ni diccionarios, pero tuples si acepta"""

set1 = set([1,2,3,4])
print(type(set1))
print(set1)

set2 = set({1,2,3,4,5})
print(type(set2))
print(set2)

set3 = set((6,7,8,9))
print(type(set3))
print(set3)



#en los set no se puede saber el length pero si se puede saber 
# si el elemento existe

set4 = set((10, 20, 21, 22, 23))
print(10 in set4) # regresa true

#union de sets
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#agregar elementos a un set
s4 = {6,7,8,9}
s4.add(10)
print(s4)

#eleiminar y descartar
s5 = {10,11,12,13}
s5.remove(10)
print(s5) #{11, 12, 13}

s6 = {14,15,16,17}
s6.discard(17)
print(s6) #{16, 14, 15}

#pop() es un tanto peligroso usarlo en set, ya que no los objetos no tienen index
#entonces eligira un objeto aleatoriamente, normalemente se pueden usar para algun sorteo
s7 = {4,5,6,7,8,9}
sorteo = s7.pop()
print(sorteo)

#clear() limpia o elimina todo lo que haya en la variable
s8 = {'aqui', "no", 'hay', 'nada'}

s8.clear()
print(s8) #regresa set() vacio

#ejercicios

"""Une los siguientes sets en uno solo, llamado mi_set_3:"""

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

mi_set_3 = mi_set_1.union(mi_set_2)

print(mi_set_3) #regresa {1, 2, 'cuatro', 'tres', 4, 5}

"""Elimina un elemento al azar del siguiente set, utilizando métodos de sets."""

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo1 = sorteo.pop()

print(sorteo1) #eliminara random cualquier elemento

"""Agrega el nombre Damián al siguiente set, utilizando métodos de sets:"""

nombres = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

nombres.add("Damián")

print(nombres) # regresa {'Camila', 'Axel', 'Mónica', 'Jorge', 'Miguel', 'Damián', 'Margarita'}

