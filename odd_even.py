print("\n")

print("Bienvenido a PAR o IMPAR?")
try:
  choice = int(input("En qué numero estas pensando: "))
except ValueError:
  print("El programa terminó porque no ingresó un número válido")
else:  
  while isinstance(choice, int):
    if choice % 2 == 0:
      try:
        print(f"El número {choice} es PAR")
        choice = int(input("Puedes ingresar otro?: "))
      except ValueError:
        print("El programa terminó porque no ingresó un número válido")
        break
    else:
      try:
        print(f"El número {choice} es IMPAR")
        choice = int(input("Puedes ingresar otro?: "))
      except ValueError:
        print("El programa terminó porque no ingresó un número válido")
        break
      
print("FIN")