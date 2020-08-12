'''Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
saber cuanto deberá pagar finalmente por su compra.'''

tc = int(input("Ingrese total compra: "))
d = tc * 0.15
tp = tc - d
print(f"Total a pagar con un decuento del 15%: {tp}")