# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Ingrese un número entero\n"))
if numero % 2 == 0:
    print("El número es par\n")
else:
    print("El número es impar\n")