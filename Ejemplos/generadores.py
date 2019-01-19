#funcion normal
def generaPares(limite):
	
	num = 1
	lista = []

	while num<limite:

		lista.append(num*2)
		num += 1

	return lista

print(generaPares(10))

#funcion "generador" genera uno a uno los elementos
#y los guarda en un objeto iterable
def numerosPares(limite):
	
	num = 1

	while num<limite:

		yield num*2
		num += 1

pares = numerosPares(10)

#for i in pares:
	#print(i)

print(next(pares))
print("xd")
print(next(pares))
print("xd")
print(next(pares))
print("xd")