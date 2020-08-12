'''Calcular el numero de pulsaciones que una persona debe tener por cada 10 segundos de
ejercicio, si la formula es:
num. pulsaciones = (220 - edad)/10'''

edad =int(input("Ingrese su edad: "))
nump = (220 - edad)/10
print(f"El numero de pulsaciones cada 10 segundos es: {nump}")