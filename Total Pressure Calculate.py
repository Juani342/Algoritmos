'''
Calcula la presion total
'''

def calcular_presion(M1, M2, m1, m2, V, T):
    R = 0.082  # Constante de los gases en dm^3·atm·K⁻¹·mol⁻¹

    # Convertir la temperatura de Celsius a Kelvin
    T_K = T + 273.15

    # Calcular los moles de cada gas
    moles1 = m1 / M1
    moles2 = m2 / M2

    # Calcular los moles totales
    moles_totales = moles1 + moles2

    # Calcular la presión total
    P_total = (moles_totales * R * T_K) / V

    return P_total


# Ejemplo de uso:
M1 = 28.97  # Masa molar del gas 1 (en g/mol)
M2 = 44.01  # Masa molar del gas 2 (en g/mol)
m1 = 50  # Masa del gas 1 (en g)
m2 = 100  # Masa del gas 2 (en g)
V = 10  # Volumen del recipiente (en dm^3)
T = 25  # Temperatura (en °C)

# Calcular la presión total
presion = calcular_presion(M1, M2, m1, m2, V, T)
print(f"Presión total: {presion:.2f} atm")
