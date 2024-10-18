def calcular_bonificacion(salario_base, cargo, nivel_des):
    cargo = cargo.lower()
    nivel_des = nivel_des.lower()

    bonificacion = 0

    if cargo == "directivo":
        if nivel_des == "alto":
            bonificacion = salario_base * 0.20
        elif nivel_des == "medio":
            bonificacion = salario_base * 0.10

    elif cargo == "operativo":
        if nivel_des == "alto":
            bonificacion = salario_base * 0.15
        elif nivel_des == "medio":
            bonificacion = salario_base * 0.05

    total_a_recibir = salario_base + bonificacion

    return bonificacion, total_a_recibir

def generar_resumen_pago(cargo, nivel_des, salario_base, bonificacion, total_a_recibir):
    print("\n-----Resumen del Pago-----")
    print(f"Cargo: {cargo.capitalize()}")
    print(f"Nivel de Desempeño: {nivel_des.capitalize()}")
    print(f"Salario Base: ${salario_base}")
    print(f"Bonificación: ${int(bonificacion)}")
    print(f"Total a Recibir: ${int(total_a_recibir)}")
    print("------------------------------------")

salario_base = float(input("Ingrese el salario base mensual: "))
cargo = input("Ingrese el cargo del empleado : ")
nivel_des = input("Ingrese el nivel de desempeño : ")

bonificacion, total_a_recibir = calcular_bonificacion(salario_base, cargo, nivel_des)

generar_resumen_pago(cargo, nivel_des, salario_base, bonificacion, total_a_recibir)