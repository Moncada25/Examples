"""upper()#convierte a mayúsculas la cadena
lower()#convierte a minúsculas la cadena
capitalize()#pone la primera letra en mayúscula
count()#cuenta una letra cuántas veces aparece
find()#busca el índice del caracter
isdigit()#comprueba si hay solo números
isalum()#comprueba que sea alfanumérico
isalpha()#comprueba si hay solo letras
split()#separa por palabras utilizando espacios
strip()#borra espacios en blanco
replace()#cambia una letra por otra
rfind()#busca el índice del caracter desde atrás
"""

correo = input("Introduce un correo: ")

arroba = correo.count('@')

if(arroba != 1 or correo.rfind('@')==(len(correo)-1) or correo.find('@')==0):
	print("Correo incorrecto")
else:
	print("Correo correcto")				