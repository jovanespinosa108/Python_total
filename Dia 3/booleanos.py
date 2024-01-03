#los booleanos tienen 2 valores, solo True or False, 
#es un tipo de dato para comparar, o si algun elementos se encuentra o no en el contenido
#son la base de las decisiones logicas en los programas

numero = 5 > 2+3
print(type(numero))
print(numero)

numero2 = 10 == 5+1+2+2
print(type(numero2))
print(numero2)

numero3 = bool(6 != 4) # se puede usar el metodo bool()
print(numero3)

#si se usa el metodo bool() solo quiere decir que es falso

#construir un valor booleano en una lista
lista = [1,2,3,4]
control = 5 in lista # se asigna la variable "lista" dentro de "control"
print(type(control)) #se convierte en typo bool
print(control) #regresa False


#ejercicios

"""Realiza una comparación que arroje como resultado un booleano y almacena 
el resultado (True/False) en una variable llamada prueba"""

prueba = 12 >= 13
print(prueba) #False


"""Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) 
en pantalla utilizando print()"""

operacion = 17834/34 > 87*56
print(operacion) #False


"""Verifica si la raíz cuadrada de 25 es igual a 5 y muestra 
el resultado (booleano) en pantalla utilizando print()"""

a = 25
b = 5
raiz_cuadrada = a**0.5
comparacion = b == raiz_cuadrada
print(raiz_cuadrada)
print(comparacion)