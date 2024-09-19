'''
Rangos de edades
'''

def edad_rango(edad):
    if edad > 14:
        # Usar la regla clásica
        min_edad = edad // 2 + 7
        max_edad = 2 * (edad - 7)
    else:
        # Usar la regla alternativa
        min_edad = round(edad - 0.10 * edad)
        max_edad = round(edad + 0.10 * edad)

    # Retornar el rango en formato "min-max"
    return f"{min_edad}-{max_edad}"


# Ejemplos de uso:
print(edad_rango(27))  # Devuelve "20-40"
print(edad_rango(5))  # Devuelve "4-5"
print(edad_rango(17))  # Devuelve "15-20"
