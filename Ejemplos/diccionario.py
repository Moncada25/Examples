#estructura clave-valor

diccionario = {"Alemania":"Berlín","Hola":15,"Fracia":"París","España":"Madrid","Colombia":"Bogotá"}

diccionario["Italia"] = "Lisboa" #agregar clave-valor

print(diccionario)

print(diccionario["Colombia"])#busca valor de la clave solicitada

diccionario["Italia"] = "Roma"#sobrescribe el valor existente

print(diccionario)
del diccionario["Colombia"]#elimina clave-valor
print(diccionario)

#asocia la tupla al diccionario
tupla = ["España","Fracia","Alemania"]
dicci = {tupla[0]:"Madrid",tupla[1]:"París",tupla[2]:"Berlín"}

print(diccionario.keys())
print(diccionario.values())
print(len(diccionario))