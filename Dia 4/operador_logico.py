#Los operadores Logicos son "and, or, not"
#"and" las 2 partes se tienen que cumplir para ser verdadero
#"or" una de las comparaciones se tiene que cumplir para ser verdadero
#"not" la comparacion no se debe cumplir para ser verdadero

mi_comparacion1 = 25 == 25 and 35 + 15 == 50
print(mi_comparacion1) #True

mi_comparacion2 = (48 >= 45) or (15 != 15) #parentesis para que el texto sea mas legible
print(mi_comparacion2) #True

#comparamos si 27 no es igual a "perro" resultado: verdader0, como la comparacion "no" se cumple entonce se imprime Falso
mi_comparacion3 = not 27 != "perro"
print(mi_comparacion3) #False

#es verdad que 1 no es igual a 1? resultado: falso, como la comparacion se cumple entonces imprime verdadero
mi_comparacion4 = not (1 != 1)
print(mi_comparacion4) #True

#ejercicios
"""Crea tres variables (num1 ,  num2 y num3):
Dentro de num1, almacena el valor 36
Dentro de num2, almacena el resultado de la operación 72/2
Dentro de num3, almacena el valor 48

Verifica si num1 es mayor que num2, y menor que num3. 
Almacena el resultado de dicha comparación en una variable llamada mi_bool."""

num1 =36
num2 = 72/2
num3 = 48

mi_bool = num1 > num2 and num1 < num3

print(mi_bool)

print(num2)
print(num3)

"""Práctica Operadores Lógicos 2
Crea tres variables (num1 ,  num2 y num3):
Dentro de num1, almacena el valor 36
Dentro de num2, almacena el resultado de la operación 72/2
Dentro de num3, almacena el valor 48
Verifica si num1 es mayor que num2, o menor que num3. 
Almacena el resultado de dicha comparación en una variable llamada mi_bool."""

num4 =36
num5 = 72/2
num6 = 48

mi_bool2 = (num4 > num5) or (num4 < num6)

print(mi_bool2)

print(num5)
print(num6)

"""Verifica si las palabras almacenadas en las siguientes variables:
palabra1 = "éxito", y
palabra2 = "tecnología"
no se encuentran en la frase a continuación, y almacena el resultado 
de esta comprobación (un booleano) en una variable llamada mi_bool:

"Cuando algo es lo suficientemente importante, 
lo haces incluso si las probabilidades de que salga bien no te acompañan"
Elon Musk"""

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool3 = palabra1 and palabra2 not in frase

print(mi_bool3) #True por que estas palabras "no" (not) se encuentran en el texto