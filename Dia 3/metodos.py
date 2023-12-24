"""Hay mas de 30 string metodos pero las mas usadas son: upper(), lower(), 
split(), join(), find(), replace()"""

texto = "Este es el texto de Mayra"
resultado1 = texto.upper() #converte todo el texto en mayusculas
resultado2 = texto.lower() #convierte todo el texto en minusculas
resultado3 = texto[8:].upper() #convierte el index 8 en mayuscula o si ":" todo el texto despues del index 8
resultado4 = texto.split() #regresa todo el texto en una lista, separando los caracteres por el espacio
resultado5 = texto.split("e") #separa todo el texto tomando el caracter "e" como referencia, este caracter no lo imprime

print(resultado1, resultado2, resultado3, resultado4, ",", resultado5)

a = "Esta"
b = "frase"
c = "usa"
d = "el"
e = "metodo"
f = "'join'"
g = " ".join([a,b,c,d,e,f]) #une multiples varibles cuando se pasan por una lista [] como parametro

print(g)

texto2 = "Esta frase usa el metodo 'find'"
resultado6 = texto2.find("m") #regresa "18" el index donde encontro el caracter
resultado7 = texto2.find("x") #cuando un caracter no existe regresa "-1"

print(resultado6, resultado7)

texto3 = "Esta frase usa el metodo replace() para reemplazar un caracter o palabra"
resultado8 = texto3.replace("frase", "cadena")

print(resultado8) #Esta cadena usa el metodo replace() para reemplazar un caracter o palabra


#ejercicios

'''Imprime el siguiente texto en mayúsculas, 
empleando el método específico de strings:'''

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
resultado = frase.upper()

print(resultado) 

'''Une la siguiente lista en un string, separando cada elemento con un espacio. 
Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.'''

lista_palabras = ["La","legibilidad","cuenta."]
resultado = " ".join(lista_palabras)

print(resultado) #resultado: La legibilidad cuenta.


'''Reemplaza en la siguiente frase:
"Si la implementación es difícil de explicar, puede que sea una mala idea."
los siguientes pares de palabras:
"difícil" --> "fácil"
"mala" --> "buena"
y muestra en pantalla la frase con ambas palabras modificadas.'''

texto1 = 'Si la implementación es difícil de explicar,'
texto2 = 'puede que sea una mala idea.'
resultado1 = texto1.replace("difícil", "fácil")
resultado2 = texto2.replace("mala", "buena")
union = " ".join([resultado1, resultado2])

print(union) 
# resultado: Si la implementación es fácil de explicar, puede que sea una buena idea.