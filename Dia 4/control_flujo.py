#control de flujo ayuda a Python a tomar decisiones y entonces dar un resultado
#para esto usamos "if", "elif", "else"

x = 2

if x == 3:
    print("numero correcto")
else:
    print("numero incorrecto")

# el programa iterara en cada comparacion hasta encontrar el correcto
#si no encuentra el valor declarado en la variable entonces imprimira else:
mascota = "Quetzal" 

if mascota == "camello":
    print("Tu mascota es un Camello")
elif mascota == "canario":
    print("Tu mascota es un Canario")
elif mascota == "Quetzal":
    print("Tu mascota es un Quetzal")
else:
    print("No se cual es tu mascota")


#se pueden comparar 2 valores de 2 variables

edad = 17
calificacion = 9

if edad < 18:
    print("Eres Menor de Edad")
    if calificacion >= 7:
        print(f"Aprobado tu calificacion es: {calificacion}")
else:
    print("Eres un Adulto")

#Ejercicios

"""Utilizando las variables num1 y num2, que se alimentan con el input 
del usuario (tal como en el código ya proporcionado):
Crea una estructura de control de flujo que compare los valores de las variables, 
y arroje un resultado de acuerdo al caso:

"num1 es mayor que num2"
"num2 es mayor que num1"
"num1 y num2 son iguales"

Debes mostrar en pantalla el valor de las variables ingresadas 
en lugar de num1 y num2."""

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")


"""Las leyes de un país establecen que un adulto puede conducir 
si tiene licencia para hacerlo, y para optar por una licencia para conducir, 
debe de tener 18 años o más.

Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:

"Puedes conducir"
"No puedes conducir aún. Debes tener 18 años y contar con una licencia"
"No puedes conducir. Necesitas contar con una licencia"

Utiliza la base de código ya proporcionada para plantear 
la estructura de control de flujo apropiada y verificar dichas condiciones."""

edad = 16
tiene_licencia = False

if edad >= 18:
    print("Puedes conducir")
    if tiene_licencia == False:
        print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")


"""Para acceder a un determinado puesto de trabajo, el candidato debe 
ser capaz de programar en Python y tener conocimientos de inglés.

Crea una estructura condicional para evaluar a un candidato dadas estas 
condiciones, y muestra el mensaje correspondiente en pantalla:

"Cumples con los requisitos para postularte"
"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
"Para postularte, necesitas tener conocimientos de inglés"
"Para postularte, necesitas saber programar en Python"

Utiliza la base de código ya proporcionada para plantear la estructura 
de control de flujo apropiada y verificar dichas condiciones. 
Evalúa a un candidato que sabe inglés, pero no programa en Python."""

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif sabe_python == True and habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles == True and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")