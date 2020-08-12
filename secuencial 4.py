'''Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha
calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.'''

c1= int(input("Ingrese nota 1: "))
c2= int(input("Ingrese nota 2: "))
c3= int(input("Ingrese nota 3: "))
ef= int(input("Ingrese nota examen final: "))
tf= int(input("Ingrese nota trabajo final: "))
prom = (c1 + c2 + c3)/3
ppar = prom * 0.55
pef = ef * 0.30
ptf = tf * 0.15
cf = ppar + pef + ptf
print(f"Calificacion final: {cf}")