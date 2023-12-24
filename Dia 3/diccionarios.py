"""Los Diccionarios se componere de objetos que contienen un consepto y una definicion
palabra clave: valor, estos elementos se escriben dentro de { }, y se separan con
comas "," no tienen orden especifico, no tiene index, no se  pueden buscar con el indice
los valores se buscan en base a su clave, las claves tiene que ser unicas,
pero los valores si pueden repetirse, pede tener listas o incluso diccionarios"""

diccionario = {"c1":"valor1", "c2":"valor2"}

resultado = diccionario["c1"]
print(resultado) #regresa "valor1"6


cliente = {"nombre": "Juan", "Apellido": "Fuentes", "Peso": 88, "Talla":1.76}
consulta = (cliente["Peso"])

print(consulta)


dic_mix = {"k1": "55", "k2": [1, 4, 7, 90], "k3": {"F2": "150", "F3": "300"}}
print(dic_mix["k2"] [3])

#hacer en una line de codigo, una orden que imprima la letra 'e' en mayuscula
alfabeto = {"key1":['a', 'b' ,'c'], "key2": ['d', 'e', 'f']}
print(alfabeto["key2"] [1].upper())

#para agregar un nuevo elemento a un diccionario existente
new_dic = {1: 'a', 2: 'b', 3: 'c'}
print(new_dic)
new_dic[4] = 'd'
print(new_dic)
#tambien se puede sobre escribir overwirte un valor
new_dic[2] = "Z"
print(new_dic)

#para investigar ciertos valores debemos llamar el metodo en print
print(new_dic.keys()) #nos regresa el nombre de las claves
print(new_dic.values()) #nos regresa los valores de las claves
print(new_dic.items()) #nos regresa las claves con los valores en tuples


#Ejercicios

"""Crea una función print que devuelva del segundo item de la lista llamada points2, 
dentro del siguiente diccionario. Si el valor 300 cambiara en el futuro, 
el código debería funcionar igual para devolver el valor que se encuentre 
en esa misma posición. Para ello, deberás hacer referencia a los nombres de las 
claves y/o índices según corresponda."""

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

'''Actualiza la información de nuestro diccionario llamado mi_dic  
(reasignando nuevos valores a las claves según corresponda), 
y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
nombre: Karen
apellido: Jurgens
edad: 36
ocupacion: Editora
pais: Colombia
para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios'''

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"

