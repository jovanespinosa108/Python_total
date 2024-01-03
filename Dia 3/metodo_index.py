"""El metodo index sirve para investigar que numero de indice tiene cierto caracter
se hace por medio del metodo index(), pude buscar un caracter, una palabra, 
es sensible a mayusculas, indices negativos se cuentan de derecha a izquireda
pero el cero simpre es el primer caracter y despues va de atras hacia delante"""

mi_texto = "Esta es una prueba de texto"
resultado = mi_texto[-7]
print(resultado) # resultado "e"

texto2 = "segunda prueba de texto"
resultado2 = texto2.index("p", 4,15) #subindex tiene 3 parametros, el caracter a buscar, el indice donde empezar y el indice donde terminar
print(resultado2) #resultado 6

texto3 = "tercer texto para la ultima prueba"
resultado3 = texto3.rindex("prueba")#right index empiza a buscar el indice de derecha a izquierda
print(resultado3) #resultado 28

texto4 = "texto donde no existe el caracter"
resultado4 = texto4.index("p")
print(resultado4) #  resultado4 = texto4.index("p")
#ValueError: substring not found

#Ejecicios
"""Encuentra y muestra en pantalla qué caracter ocupa 
la quinta posición dentro de la siguiente palabra: "ordenador"""

palabra = "ordenador"
resultado5 = palabra[4]
print(resultado5) #resultado "n"


'''Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."'''

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado6 = frase.index("práctica")
print(resultado6) # resultado: 26


'''Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."'''

frase2 = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado7 = frase2.rindex("práctica")
print(resultado7)