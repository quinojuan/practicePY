# print("\n...")

# numero_oculto = 42
# intentos = 0

# def pedirNumero():
#   number = int(input("Ingrese un numero entre 1 y 50: "))
#   return number

# def numero():
#   while True:
#     num = pedirNumero()
#     if 1 <= num <= 50:
#       return num
#     else:
#       print("Número fuera de rango. Intente nuevamente")


# def principal():
#   global intentos
#   intentos += 1
#   if numero() == numero_oculto:
#     print("acertaste")
#     return print(f"lo resolviste en {intentos} intentos")
#   else:
#     choice = input("Queres seguir jugando, si o no?: ").lower()
#     if choice == "si":
#       principal()
#     elif choice == "no":
#       return print("gracias por intentarlo")
#     else:
#       return print("Opcion inválida. Fin")

# principal()

import random

number = random.randrange(1, 50)
print(f"number: {number}")
guess = int(input("Adiviná el número entre 1 y 50: "))

attempts = 1

while guess != number:
  if guess < number:
    attempts += 1
    print("Un poco mas alto. Intenta de nuevo.")
    guess = int(input("\nAdiviná el número entre 1 y 50: "))
  else: 
    attempts += 1
    print("Un poco mas bajo. Intenta de nuevo.")
    guess = int(input("\nAdiviná el número entre 1 y 50: "))
    
print(f"Adivinaste y acertaste en {attempts} intentos!")