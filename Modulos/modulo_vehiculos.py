class vehiculos():

	def __init__(self, marca, modelo):

		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enMarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,
			"\nEn marcha: ",self.enMarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)

class Furgoneta(vehiculos):

	def cargar(self, carga):
		self.cargado = carga

		if(self.cargado):
			return "La furgoneta está cargada..."
		else:
			return "La furgoneta no está cargada..."


class Moto(vehiculos):
	
	picada = "No"

	def picar(self):
		self.picada = "Estoy picando la moto..."

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,
			"\nEn marcha: ",self.enMarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,"\nPicada: ",self.picada)


class VElectricos(vehiculos):

	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.autonomia = 100

	def cargarEnergia(self):
		self.cargando = True

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,
			"\nEn marcha: ",self.enMarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,"\nAutonomia: ",self.autonomia)	
