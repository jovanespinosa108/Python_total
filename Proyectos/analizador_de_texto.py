"""#Proyecto donde se ingresa cualquier tipo de texto y el codigo regresara todo tipo de informacion del texto
como cuantas palabras tiene, numero de veces que se repite una letra, nombre de cuidad existe el el texto etc."""

#ingresa un texto y crea una lista para las letras
texto = input("Bienvenido!!, ingresa un texto de tu preferencia: ")
letras = [] 

#Convierte el texto en minusculas
texto = texto.lower()

#ingresa letras y guardalas en la lista "letras", conviertelas en minusculas
letras.append(input("Ingresa 3 letras para buscarlas en el texto \nla primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

#crea variables que regresen la contabilidad de las letras ingresadas
print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])


#crea un string con formato que nos de el resultado de las letras encontradas
print(f"Hemos encontrado la letra '{letras[0]}' repetida '{cantidad_letras1}' veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida '{cantidad_letras2}' veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida '{cantidad_letras3}' veces")


#crea una variable que convierta el texto en una lista y que regrese la cantidad de palabras
print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")


#Crea 2 variables que regresen la primera y la ultima letra
print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")


#imprime el texto inicial invertido
print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto alrevez va a decir: '{texto_invertido}'")

#crea una valriable que busque si python esta en el texto, usa booleanos
print("\n")
print("BUSCANDO LA PALABRA 'PYTHON'")
buscar_python = 'python' in texto
dic = {True: "si", False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en tu texto")


#metodo index(), extraer sub-strings, metodos y propiedades de string, 
# list, diccionarios, tuples, sets, booleans

#pide que ingrese un texto
#pide ingresar 3 letras a su eleccion
#el codigo hara 5 tipos de analisis y regresara:
#cuantas veces aparece cada letra (cuantas veces aparece un substring dentro de un string, almacena letras en una lista)
#puede haber mayusculas o minusculas
#pasa el texto y letras en minusculas
#el programa debe decir cuantas palabras hay en el texto, (usa metodos para transformarlo en lista de palabras y calcula su longitud)
#el programa debe decir cual es la primera y ultima letra del texto
#el sistema mostrara el texto si invirtieramos el orden de las palabras
#el sistema nos dira si la palabra "Python" aparece dentro del texto (usa bools para verificar si se encuentra y un diccionario para asociar el booleano con un string para mostrarlo al usuario)

# texto = input("Bienvenido!! Ingresa un texto: ")
# letras = input("Ingresa 3 letras de tu eleccion separadas cada una por un espacio: ")
#almacena las letras en una lista y despues usa un metodo de string que cuente cuantas veces
#aparece un substring dentro del string, al buscar letras pueden haber mayusculas y minusculas
#esto lo hace pasando el texo original y las letras a minusculas
# resultado_letras = letras.split()
# print(resultado_letras)
# cuenta_letras = resultado_letras.count(texto)
# print(cuenta_letras)
# texto_minusculas = texto.lower()
# print(texto_minusculas)
#cuantas palabras hay en el texto usa el metodo find() y la funcion len()
 
# print(len(texto))
#cual es la primera y la ultima letra del texto
# texto[0:-1]
#invierte el orden del texto y unelos con espacion intermedios .join()
# texto_invertido = texto[::-1]
# print(texto_invertido)

#la palabra Python aparece en el texto?
# print("Python" in texto)


#usa booleanos para verificar si se encuentra  y
#diccionarios para asociar el booleano con un string para mostrarlo al usuario


# texto_letras = letras.find()
# texto_lista = texto.split()
# print(texto_letras)

# print(len(texto_lista))
# contador_texto = letras.index()
# print(contador_texto)

# print(len(letras))
