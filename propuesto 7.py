'''El dueño de una tienda compra un articulo a un precio determinado. Obtener el precio
en que lo debe vender para obtener una ganancia del 30%.'''

preart = int(input("Escriba el precio del articulo: "))
porcentaje = preart * 0.30
vengana = preart + porcentaje
print(f"Debe venderlo a: {vengana}")