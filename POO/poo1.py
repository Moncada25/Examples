class Coche():

	def __init__(self):

		self.__largoChasis = 250
		self.__anchoChasis = 120
		self.__ruedas = 4
		self.__enMarcha = False

	def arrancar(self,arrancamos):
		
		self.__enMarcha = arrancamos

		if (self.__enMarcha):
			chequeo = self.__chequeo_interno()

		if (self.__enMarcha and chequeo):
			return "El coche está en marcha."
		elif (self.__enMarcha and chequeo == False):
			return "Algo ha ido mal en el chequeo, no se puede arrancar..."	
		else:
			return "El coche está parado."	

	def estado(self):
		print ("El coche tiene ",self.__ruedas," ruedas\nUn ancho de ",self.__anchoChasis, "\nUn largo de ",self.__largoChasis)

	def __chequeo_interno(self):
		print("Realizando chequeo interno...\n")

		self.gasolina = "ok"
		self.aceite = "ok"
		self.puertas = "cerradas"

		if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
			return True
		else:
			return False	


miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("\nCreamos otro objeto...\n")

miCoche2 = Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()
