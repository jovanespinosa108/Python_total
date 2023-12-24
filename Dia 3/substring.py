"""Con los substrings podemos manipular strings extrayendo porciones de texto
seleccionando un fragmento de caracteres de la cadena y guardarlo en una variable """

#fragmentar/Slice
texto = "ABCDEFGHIJKLMN"
fragmento1 = texto[5] # regresa el 5to caracter
fragmento2 = texto[5:9] #regresa del 5to al 9no caracter
fragmento3 = texto[5:] #regresa del 5to al ultimo caracter
fragmento4 = texto[:6] #regresa del 0 al 6to caracter
fragmento5 = texto[2:9:2] #regresa del 2do al 9no caracter escogiendo cada 2 caracterer (uno si, uno no)
fragmento6 = texto[::3] #regresa del 0 al ultimo caracter escogiendo cada 3 caracteres
fragmento7 = texto[::-1] #regresa todos los caracteres empezando del ultimo al primero
print(fragmento1, fragmento2, fragmento3, fragmento4, fragmento5, fragmento6, fragmento7)


#Ejercicios
'''Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
"Controlar la complejidad es la esencia de la programación"
Pista: "Controlar" tiene un largo de 9 caracteres.'''

frase = "Controlar la complejidad es la esencia de la programación"
fragmento8 = frase[0:9]
print(fragmento8) #resultado Controlar


'''Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
"Nunca confíes en un ordenador que no puedas lanzar por una ventana"'''

frase2 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento9 = frase2[8::3]
print(fragmento9) #resultado: neeuoed eoualz rnvta


'''Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"'''

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase[::-1]
print(fragmento) 
# azevrec ut nebeb es on y odot nadreucer ol ,netucsid oN .serodanedro noc rajabart laineg sE

