'''En un hospital existen tres áreas: Ginecología, Pediatría, Traumatologia. El presupuesto
anual del hospital se reparte conforme a la sig. tabla:
Área Porcentaje del presupuesto
Ginecología 40%
Traumatologia 30%
Pediatría 30%'''

presupuesto = int(input("Ingrese el presupuesto: "))
gp = presupuesto * 0.40
tp = presupuesto * 0.30
pp = presupuesto * 0.30
print(f"El presupuesto de Ginecologia es: {gp} El presupuesto de Traumatologia: {tp} El presupuesto de Pediatria es: {pp}")