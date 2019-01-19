t = 1
while t<=20:

	print("Tabla del ",t)

	for i in range(13):
		print(t," x ",i," = ",(t*i))

	print("\n")	

	t = t+1	

def power(x,y):
	if y==0:
		return 1
	else:
		return x*power(x,y-1)


print(power(2,3))			
