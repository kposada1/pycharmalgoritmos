'''Un maestro desea saber que porcentaje de hombres y que porcentaje de mujeres hay en
un grupo de estudiantes.'''

nh = int(input("Ingrese el numero de hombres: "))
nm = int(input("Ingrese el numero de mujeres: "))
ta = nh + nm
ph = (nh * 100)/ta
pm = (nm * 100)/ta
print(f"El porcentaje de hombres es: {ph} y el porcentaje de mujeres es: {pm}")