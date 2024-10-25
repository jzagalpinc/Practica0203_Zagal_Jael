# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
from getpass import getpass
contraseña = getpass("Por favor cree una contraseña\n")
entrada = getpass("Introduzca su contraseña\n")
while entrada != contraseña:
    print("La contraseña es incorrecta ❌")
    entrada = getpass("Introduzca su contraseña\n")
print("La contraseña es correcta ✅")