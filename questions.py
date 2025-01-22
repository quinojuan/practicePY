import re

nombre = input("Ingresa tu nombre: ")
regex_nombre = r"^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$"

while not (re.match(regex_nombre, nombre)):
  nombre = input("Ingresa un nombre válido: ")
  
nacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")
regex_nacimiento = r"^(19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"

while not (re.match(regex_nacimiento, nacimiento)):
  nacimiento = input("Ingresa tu fecha de nacimiento válida: ")
  
direccion = input("Ingresa tu direccion: ")
metas = input("Ingresa tu meta más próxima: ")

resumen = f'''
- Nombre: {nombre}
- Fecha de nacimiento: {nacimiento}
- Dirección: {direccion}
- Metas personales: {metas}
'''

print(resumen)