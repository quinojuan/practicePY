import random
opciones = [1,2,3]

def solucion(jug1, jug2):
  if jug1 == 1 and jug2 == 1:
    return print("Empate")
  elif jug1 == 1 and jug2 == 2:
    return print("Ganaste!")
  elif jug1 == 1 and jug2 == 3:
    return print("Perdiste!")
  
  elif jug1 == 2 and jug2 == 1:
    return print("Perdiste!")
  elif jug1 == 2 and jug2 == 2:
    return print("Empate")
  elif jug1 == 2 and jug2 == 3:
    return print("Ganaste!")
  
  elif jug1 == 3 and jug2 == 1:
    return print("Ganaste!")
  elif jug1 == 3 and jug2 == 2:
    return print("Perdiste!")
  else:
    return print("Empate")

eleccion_jugador1 = random.choice(opciones)
print("\n")
eleccion_jugador2 = int(input("Elija Piedra (1), Papel (2) o Tijera (3): "))

if eleccion_jugador2 > 0 and eleccion_jugador2 < 4:
  if eleccion_jugador1 == 1:
    print("El jugador 1 eligió: Piedra")
    print(solucion(eleccion_jugador1, eleccion_jugador2))
  elif eleccion_jugador1 == 2:
    print("El jugador 1 eligió: Papel")
    print(solucion(eleccion_jugador1, eleccion_jugador2))
  else:
    print("El jugador 1 eligió: Tijeras")
    print(solucion(eleccion_jugador1, eleccion_jugador2))
else:
  print("Opcion inválida - Fin")
     
