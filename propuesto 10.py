'''Un alumno desea saber cual será su promedio general en las tres materias mas difíciles
que cursa y cual será el promedio que obtendrá en cada una de ellas. Estas materias se
evalúan como se muestra a continuación:
La calificación de Matemáticas se obtiene de la sig. manera:
Examen 90%
Promedio de tareas 10%
En esta materia se pidió un total de tres tareas.
La calificación de Física se obtiene de la sig. manera:
Examen 80%
Promedio de tareas 20%
En esta materia se pidió un total de dos tareas.
La calificación de Química se obtiene de la sig. manera:
Examen 85%
Promedio de tareas 15%
En esta materia se pidió un promedio de tres tareas.'''

examenm = float(input("Escriba la calificacion del examen de matematicas: "))
tarem1 = float(input("Escriba la calificacion de la tarea 1 de matematicas: "))
tarem2 = float(input("Escriba la calificacion de la tarea 2 de matematicas: "))
tarem3 = float(input("Escriba la calificacion de la tarea 3 de matematicas: "))
examenf= float(input("Escriba la calificacion del examen de fisica: "))
taref1 = float(input("Escriba la calificacion de la tarea 1 de fisica: "))
taref2 = float(input("Escriba la calificacion de la tarea 2 de fisica: "))
examenq = float(input("Escriba la calificacion del examen de quimica: "))
tareq1 = float(input("Escriba la calificacion de la tarea 1 de quimica: "))
tareq2 = float(input("Escriba la calificacion de la tarea 2 de quimica: "))
tareq3 = float(input("Escriba la calificacion de la tarea 3 de quimica: "))

pem = examenm * 0.90
promtarem = (tarem1 + tarem2 + tarem3) / 3
porcenttm = promtarem * 0.10
totalm = pem + porcenttm

pef = examenf * 0.80
promtaref = (taref1 + taref2 ) / 2
porcenttf = promtaref * 0.20
totalf = pef + porcenttf

peq = examenq * 0.85
promtareq = (tareq1 + tareq2 + tareq3) / 3
porcenttq = promtareq * 0.15
totalq = peq + porcenttq

prommat = (totalm + totalf + totalq)/3

print(f"La calificacion final de matematicas es: {totalm}")
print(f"La calificacion final de fisica es: {totalf}")
print(f"La calificacion final de quimica es: {totalq}")
print(f"El promedio de las tres materias es: {prommat}")
