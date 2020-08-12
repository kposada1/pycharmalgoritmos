'''Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los
tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer la
ruta en una semana cualquiera.'''

tiemplu = int(input("Escriba el tiempo obtenido el lunes: "))
tiempmi = int(input("Escriba el tiempo obtenido el martes: "))
tiempvi = int(input("Escriba el tiempo obtenido el viernes: "))
prom = (tiemplu+tiempmi+tiempvi)/3
print(f"El tiempo que tarda en recorrer la ruta una semana cualquiera es: {prom}")