# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Ingrese su edad por favor\n"))
ingresos = float(input("Escriba sus ingresos mensuales por favor\n"))
if edad <= 16 or ingresos <= 1000:
    print("Usted no tiene que tributar")
else: 
        print("Usted tiene que tributar")