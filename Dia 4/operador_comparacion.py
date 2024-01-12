#operadores logicos son los signos de comparacion
# '=' es para agregar un valor a algo
#"==" es para hacer una comparacion que arrojara un bool 
#25 es igual a 30, 25 == 30 arrojara falso porque 25 es diferente a 30
mi_bool = 10 == 25
print(mi_bool) # False

mi_bool2 = 15 == 15
print(mi_bool2) # True

#se pueden hacer comparaciones con operaciones
mi_bool3 = 10+5 == 5*4
print(mi_bool3) # False

#se pueden comparar strings
mi_bool4 = "blanco" == "negro"
print(mi_bool4) # False

#las comparaciones son case sensitive (mayusculas y minusculas)
bool_miniscula = "azul" == "azul"
bool_mayuscula = "rojo" == "Rojo"
print(bool_miniscula, bool_mayuscula) # minuscula True, mayuscula False

#comparacion entre diferentes data types
mi_bool5 = "250" == 250
print(mi_bool5) #False

#tambien se pueden comparar diferencias
mi_bool6 = "350" != 350  #"350" es diferente a 350?
print(mi_bool6) #True

#mayor que
bool_mayor = 350 > 100
print(bool_mayor) #True

#menor o igual a
bool_menor_igual = 45 <= 58
print(bool_menor_igual) # True

#ejercicios 

"""Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. 
Verifica si num1 es mayor o igual que num2 y almacena el resultado 
de dicha comparación en una variable llamada mi_bool"""

num1 = 36
num2 = 17

mi_bool7 = num1 >= num2

print(mi_bool7) #imprime True

"""Crea dos variables (num1 y  num2):
Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25
Dentro de num2, almacena el número 5.
Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación 
en una variable llamada mi_bool."""

num1 = 25 **0.5
num2 = 5

mi_bool8 = num1 == num2

print(mi_bool8) #imprime True

"""Crea dos variables (num1 y  num2):
Dentro de num1, almacena el resultado de la operación 64 x 3
Dentro de num2, almacena el resultado de la operación 24 x 8
Verifica si num1 es diferente a num2 y almacena el resultado 
de dicha comparación en una variable llamada mi_bool."""

num1 = 64*3
num2 = 24*8

mi_bool9 = num1 != num2

print(mi_bool9) #imprime False