'''La presión, el volumen y la temperatura de una masa de aire se relacionan por la
formula:
masa = (presión * volumen)/(0.37 * (temperatura + 460))'''

presion= float(input("Ingrese presion: "))
volumen= float(input("Ingrese volumen: "))
temperatura= float(input("Ingrese temperatura: "))
masa = (presion * volumen)/(0.37 * (temperatura + 460))
print(f"El resultado es: {masa}")