def function(num1,num2):
	if num1>num2:
		print(num1+num2)
	else:
		print(num1-num2)	
	
#function(1,2)
#function(45,12)

######################################################	

def numerosPrimos(num):

	contGN = 1
	contD = 0
		
	while contGN<=num:

		if num % contGN == 0:
			contD = contD+1

		contGN = contGN + 1

	if contD == 2:
		print("Es primo")
	else:
		print("No es primo")

#numerosPrimos(15)
#numerosPrimos(3)
#numerosPrimos(5341)
#numerosPrimos(3633)

############################################

def fibonacci(cant):
	
	a = 0
	b = 1
	c = 0

	for i in range(cant):
		print(c)
		c = a+b
		b = a
		a = c


#fibonacci(10)

################################################

def hora():
	h = 0
	m = 0
	s = 0

	for h in range(24):
		for m in range(60):
			for s in range(60):
				print(h,m,s)


#hora()


resultado = 3**2-(-3**2)
print(resultado)