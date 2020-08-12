'''Dada un cantidad en pesos, obtener la equivalencia en dólares, asumiendo que la unidad
cambiaría es un dato desconocido.'''

cantp = int(input("Ingrese la cantidad de pesos: "))
uc = float(input("Ingrese la unidad cambiaria: "))
cantd = cantp * uc
print(f"La cantidad de {cantp} pesos a dolares es: {cantd}")