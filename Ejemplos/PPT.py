# Juego de PIEDRA, PAPEL Y TIJERA
# contra la CPU

# El jugador escoje entre
# Piedra, Papel o Tijera.
# Opción: 1, 2, o 3, 
# respectivamente

from random import* 

# El usuario escoje
def opcionJugador():
 print("\t\t\tEscoje una opción\n")
 print("\t\t1). Piedra. 2). Papel. 3). Tijera.", end=' ')
 opcion = int(input("---> "))
 if opcion == 1:
  return "PIEDRA"
 elif opcion == 2:
  return "PAPEL"
 else :
  return "TIJERA"

# La maquina escoje
def opcionMaquina():
 opcion = randint(1, 3)
 if opcion == 1:
  return "PIEDRA"
 elif opcion == 2:
  return "PAPEL"
 else :
  return "TIJERA"
# Se define el ganador
def ganador(player, machine):
 if player == machine:
  return "EMPATE"
 # -----------------------------
 if player == "PIEDRA" and machine == "PAPEL":
  return "La maquina GANA!"
 if player == "PIEDRA" and machine == "TIJERA":
  return "GANASTE!"
 # -----------------------------
 if player == "PAPEL" and machine == "PIEDRA":
  return "GANASTE!"
 if player == "PAPEL" and machine == "TIJERA":
  return "La maquina gana!"
 # -----------------------------
 if player == "TIJERA" and machine == "PIEDRA":
  return "La maquina gana!"
 if player == "TIJERA" and machine == "PAPEL":
  return "GANASTE!"
# Muestra el resultado
def resultado():

  j = opcionJugador()
  m = opcionMaquina()
  g = ganador(j, m)
   print("--------------------------------------")
  print("      |JUGADOR| VS |MAQUINA|")
  print("--------------------------------------")
  print("\t  ", j, "\t   ", m)
  print("\n\t\t    ", g)
  print("--------------------------------------")


