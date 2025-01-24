# word = input("Ingresa una palabra para saber si es palíndromo: ")
word = input("Ingrese una palabra para saber si es un palindromo: ")
letras = list(word)
# for i in word:

medio = len(letras) // 2

primera_mitad = letras[:medio]

if ((len(word) % 2)==1):
  segunda_mitad = letras[medio + 1:]
else:
  segunda_mitad = letras[medio:]

segunda_mitad_invertida = segunda_mitad[::-1] # utilizando este reverse no necesito dividir el array

esPalindromo = primera_mitad == segunda_mitad_invertida

if esPalindromo:
  print(f"la palabra --{word}-- es un palindromo")
else:
  print(f"la palabra --{word}-- NO ES un palindromo")
  
# Alternativa https://github.com/kuzmicheff/palindrome/blob/master/palindrome.py