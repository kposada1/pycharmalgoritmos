'''Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas
invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con
respecto a la cantidad total invertida.'''

inv1 = int(input("Primera inversion 1: "))
inv2 = int(input("Primera inversion 2: "))
inv3 = int(input("Primera inversion 3: "))
invtot = inv1+inv2+inv3
porcent1 = inv1 / invtot * 100
porcent2 = inv2 / invtot * 100
porcent3 = inv3 / invtot * 100
print(f"La inversion 1 tiene un porcentaje del: {porcent1}% La inversion 2 tiene un porcentaje del: {porcent2}% La inversion 3 tiene un porcentaje del: {porcent3}%")