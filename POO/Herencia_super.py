class Persona():

	def __init__(self,nombre,edad,residencia):
		self.nombre = nombre
		self.edad = edad
		self.residencia = residencia

	def descripcion(self):
		print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nResidencia: ",self.residencia)

class Empleado(Persona):
	
	def __init__(self,salario,tiempo,nombre_empleado,edad_empleado,lugar_empleado):
		super().__init__(nombre_empleado,edad_empleado,lugar_empleado)
		self.salario = salario
		self.tiempo = tiempo

	def descripcion(self):
		super().descripcion()

		print("Salario: ",self.salario,"\nTiempo en la empresa: ",self.tiempo)	


Santiago = Empleado(1000,15,"Santiago",20,"Colombia")
Santiago.descripcion()
print(isinstance(Santiago, Persona))			