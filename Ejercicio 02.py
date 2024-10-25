# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

dividendo = float(input("Ingrese el dividendo\n"))
divisor = float(input("Ingrese el divisor\n"))

if divisor != 0:
    print(round(dividendo / divisor ,2))
else:
    print("Error: el divisor es 0")
