print("Programa de evaluacion de notas de alumnos...\n")

nota_alumno = input("Digite la nota del alumno: ")

def evaluacion(nota):
	valoracion = "aprovado"
	if nota<3:
		valoracion = "reprovado"
	return valoracion
	
print(evaluacion(int(nota_alumno)))

#########################################

print("Verificación de acceso...")

edad = int(input("Introduce tu edad: "))

if edad<18:
	print("No puedes pasar.")
else:
	print("Puedes pasar")