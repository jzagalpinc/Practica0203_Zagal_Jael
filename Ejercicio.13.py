# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    frase = input("Introduce algún texto. Para salir escribir (salir): ")
    if frase.lower() == "salir":  # Convertir a minúsculas para comparar
        break
    print(frase)