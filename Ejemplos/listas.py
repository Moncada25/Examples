lista = ["Santiago",True,20,851.1]
#print(lista[0])
#print(lista[-1])#muestra la lista desde el final
#print(lista[:2])#muestra la lista hasta el indice indicado

#lista.append("XD") #agregar elemento
#lista.insert(1,":v") #insertar elemento después de el indice introducido
#lista.extend(["ya no"," sé qué ","escribir"])#concatena otra lista
#print(lista.index("Santiago"))#busca el índice del dato 
#lista.pop()#elimina el último dato ingresado

print(lista[:])#muestra toda la lista

lista2 = ["ana","maria"] 

lista3 = lista+lista2 #suma listas (concatena)

print(lista3[:])

print("")

##############################################

tupla = ("Santiago",25,9,1997)
tupla2 = "juan","xd",5 #tupla empaquetada

print(tupla[0])

#pasar de lista a tupla tuple() y de tupla a lista list()
listap = list(tupla)

print(listap[:])#mostrar toda la lista

print(20 in tupla)#buscar elemento
print(tupla.count(9))#contar elemento solicitado

print(len(tupla))#cuenta los elementos de la tupla

nombre,dia,mes,alo = tupla #desempaquetado de tupla

print(nombre)
print(dia)
print(alo)
print(mes)

print(tupla.index(9))#busca el indice indicado