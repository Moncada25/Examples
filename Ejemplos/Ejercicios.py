def datos():
	nombre = input("Introduce el nombre: ")
	apellido = input("Introduce el apellido: ")
	telefono = input("Introduce el telefono: ")

	lista = [nombre,apellido,telefono]

	print("Los datos personales son: "+lista[0] + " " +lista[1] + " " + lista[2])

#datos()
#############################################################################

def promedio():
	n1 = int(input("Ingrese un número: "))
	n2 = int(input("Ingrese un número: "))
	n3 = int(input("Ingrese un número: "))	

	print("El promedio es: "+str((n1+n2+n3)/3))

#promedio()	

##############################################################################

from random import randint, uniform,random

#print (randint(0,10))#numero entero aleatorio entre el rango dado
#print (uniform(0,10))#numero real aleatorio entre el rango dado
#print (random())#numero aleatorio entre 0 y 1

def adivinar_numero(min,max):
	
	numero_aleatorio = randint(min,max)
	numero_usuario = 0
	cont = 0

	print("Adivina el número, está entre el "+str(min)+" y el "+str(max))

	while numero_usuario != numero_aleatorio:

		numero_usuario = int(input("\n¿En qué número estoy pensando?"))
		cont += 1
		if(numero_usuario>numero_aleatorio):
			print("El número que buscas es menor")
		elif(numero_usuario<numero_aleatorio):	
			print("El número que buscas es mayor")
				
	
	print("Lo has encontrado, el número era "+str(numero_aleatorio)+"\nTe ha tomado "+str(cont)+" intentos.")


#adivinar_numero(1,100)

##################################################################################
for i in range(1000):
	print(i)
