# ¿Cuál es mi acrónimo?
# Vamos a pedir al usuario que ingrese el significado completo de una organización o concepto y con ello como resultado obtendremos el acrónimo. Por ejemplo:

# Entrada -> As Soon As Possible. Salida -> ASAP.
# Entrada -> World Health Organization. Salida -> WHO.
# Entrada -> Absent Without Leave. Salida -> AWOL.

def acronimo(str):
  array = str.split()
  acronimo = ""
  
  for i in array:
    acronimo+=i[0]
  
  return acronimo

cadena = input("Ingrese su nombre y apellido o razon social: ")

print(acronimo(cadena))