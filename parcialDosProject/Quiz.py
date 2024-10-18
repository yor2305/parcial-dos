

materia = input("Ingrese el nombre de la materia: ")
calificacion1 = float(input("Ingrese la calificacion 1: "))
calificacion2 = float(input("Ingrese la calificacion 2: " ))
calificacion3 = float(input("Ingrese la calificacion 3: "))

def calcular_definitiva(calificacion1, calificacion2, calificacion3):
    return (calificacion1 * 0.3) + (calificacion2 * 0.2) + (calificacion3 * 0.5)
calificacionfinal = calcular_definitiva(calificacion1,calificacion2, calificacion3)
if calificacionfinal >= 3.0:
    print(f"La materia de {materia} .Usted la aprobó con {calificacionfinal}")
elif calificacionfinal < 0:
    print("Ingrese una calificacion Valida")
elif calificacionfinal > 5:
    print("Ingrese una calificacion validad")
else:
    print(f"la materia de {materia} .Usted la reprobó con {calificacionfinal}")