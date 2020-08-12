'''Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el
vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
base y comisiones.'''

sb = int(input("Ingrese sueldo base: "))
v1 = int(input("Ingrese venta 1: "))
v2 = int(input("Ingrese venta 2: "))
v3 = int(input("Ingrese venta 3: "))
totventa = v1 + v2+ v3
com = totventa * 0.10
tpag = sb + com
print(f"Sueldo base mas comisiones es el siguiente: {tpag}")