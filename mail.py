mail = input("Introduce tu email: ")
nombre = mail.split(".")[0]
dominio = mail.split("@")[1].split(".")[0]


print(f"Hola {nombre}, estoy viendo que tu email está registrado con {dominio}. ¡Eso es genial!.")
