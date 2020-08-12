'''Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre su salario
anterior.'''

sa = int(input("Ingrese el salario anterior: "))
pc = sa * 0.25
sn = sa + pc
print(f"Su nuevo salario con el incremento del 25% es: {sn}")