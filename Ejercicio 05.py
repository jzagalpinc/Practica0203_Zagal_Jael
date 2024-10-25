# Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y Slytherin por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre por favor\n").capitalize()
sexo = input("Ingrese su sexo 'M' masculino o 'F' femenino\n").upper()
if (sexo == 'F' and nombre < 'M') or (sexo == 'M' and nombre > 'N'):
    print("Usted pertenece a Gryffindor")
else:
    print("Usted pertenece a Slytherin")
