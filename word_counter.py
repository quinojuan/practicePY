thougths = input("What are you thinking about?: ")

with open("archivo.txt", "w") as archivo:
  archivo.write(thougths)

with open("archivo.txt", "r") as archivo:
  contenido = archivo.read()
  qty_words = len(contenido.split())

print(f"OK, you showed me your thougths in {qty_words} words")