'''Leer un numero y escribir el valor absoluto del mismo.'''

num = int(input("Ingrese un numero: "))
if (num < 0 ):
    valab = -(num)
    print(f"El valor absoluto es: {valab}")
else:
    print(f"El valor absoluto es: {num}")