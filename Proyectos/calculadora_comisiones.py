"""Este projecto preguntara a un emplado su nombre 
y la cantidad de ventas que ha hecho en el mes, 
despues regresara la information del 13% de comisiones que le corresponden 
en base a sus ventas"""

nombre = input("ingresa tu nombre: ")
ventas = input(f"Hola {nombre}, ingresa la cantidad haz vendido este mes: ")
porcentage_ventas = float(ventas) * round(13,2) / 100 
print(f"Felicidades {nombre}!! este mes ganaste: ${porcentage_ventas}")