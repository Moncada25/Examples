# clase que tiene un objeto tipo matriz
class Matriz:

    # constructor y atributos de la clase Matriz
    def __init__(self, filas, columnas):
        self.matriz = []
        self.filas = filas
        self.columnas = columnas

    # método que llena la matriz
    def llenarMatriz(self):
        for i in range(self.filas):
            self.matriz.append([])
            for j in range(self.columnas):
                self.matriz[i].append(int(input("[%d][%d]: " % (i, j))))
                print("-----------")

    # método que muestra la matriz
    def mostrarMatriz(self):

    	print("-------------------")
    	for i in range(self.filas):
    		print(self.matriz[i])
    	print("-------------------")
    	
    # método que muestra la diagonal principal
    def diagonalP(self):

    	if self.filas == self.columnas:
    		diagonal = []

    		for i in range(self.filas):
     	  		diagonal.append(self.matriz[i][i])

    		print("\nDiagonal principal: " + str(diagonal[:]) + "\n")
    	else:
    		print("\nLa matriz no es cuadrada...\n")

   	# método que muestra la diagonal secundaria
    def diagonalS(self):

    	if self.filas == self.columnas:

    		cont = self.filas

    		diagonal = []

    		for i in range(self.filas):
 	 	 		cont -= 1
 	 	 		diagonal.append(self.matriz[i][cont])

    		print("\nDiagonal secundaria: "+str(diagonal[:])+"\n")
    	else:
    		print("\nLa matriz no es cuadrada...\n")
    
    # método que devuelve la matriz del objeto matriz
    #(la clase Matriz tiene una matriz como atributo)
    def getMatriz(self):
        return self.matriz

    # método que devuelve el numero de filas de la matriz
    def getFilas(self):
        return self.filas

    # método que devuelve el numero de columnas de la matriz
    def getColumnas(self):
        return self.columnas

    # método que recibe como parámetro una matriz que modificará a la matriz
    # del objeto
    def setMatriz (self, matriz):
        self.matriz = matriz

    # metodo que multiplica dos matrices
    def multiplicarMatriz(self, matrizB):

        matrizRes = []
        for i in range(self.filas):
        	list_a = []
        	for j in range(matrizB.columnas):
        		mult = 0
        		for k in range(matrizB.filas):
        			mult += self.matriz[i][k]*matrizB.matriz[k][j]
        		list_a.append(mult)
        	matrizRes.append(list_a)

        return matrizRes

def salir():
    exit(0)

print("Crear matriz...\n")

filA = int(input("Digite el número de filas: "))
colA = int(input("Digite el número de columnas: "))

print("\nNOTA: no olvide llenar la matriz antes que nada...")

#objeto de la clase Matriz
matrizA = Matriz(filA, colA)    

colB = 0
filB = 0
op = 25

while op != 0:

    print("|---------------------------------------------|")
    print("|	         * Menú de Matrices *             |")
    print("|---------------------------------------------|")
    print("| 1.Llenar             | 6.                   |")
    print("| 2.Mostrar            | 7.                   |")
    print("| 3.Multiplicar        | 8.                   |")
    print("| 4.Diagonal Principal | 9.                   |")
    print("| 5.Diagonal Secundaria| 0.Salir              |")
    print("|----------------------|----------------------|")

    op = int(input("\nIngrese una opción: \n"))

    if op == 1:

        matrizA.llenarMatriz()
        print("\nMatriz creada...\n")

    elif op == 2:

    	try:
    		Matriz.mostrarMatriz(matrizA)
    	except Exception as e:
    		print("La matriz está vacía...")

    elif op == 3:

        filB = int(input("Digite el número de filas de la segunda matriz: "))
        colB = int(input("Digite el número de columnas de la segunda matriz: "))

        if filA == filB and colA == colB:
        	matrizB = Matriz(filB , colB)
        	matrizB.llenarMatriz()
        	matrizC = Matriz(filA , colB)
        	matrizResultado = matrizA.multiplicarMatriz(matrizB)
        	matrizC.setMatriz(matrizResultado)
        	print("\nMatrices multiplicadas...\n")
        	matrizC.mostrarMatriz()
        else:
        	print("\nLas matrices no pueden multiplicarse\n")

    elif op == 4:

    	try:
    		Matriz.diagonalP(matrizA) 
    	except Exception as e:
    		print("La matriz está vacía...")
    	 
    elif op == 5:

    	try:
    		Matriz.diagonalS(matrizA)
    	except Exception as e:
    		print("La matriz está vacía...")
    
    elif op == 0:
    	print("\nPrograma finalizado...")
    	salir()

    else:
        print("\nOpción inválida, intente de nuevo.\n")