'''
Convierte las monedas
'''

def usd_to_cny(usd):
    # Tasa de conversión
    conversion_rate = 6.75

    # Convertir USD a CNY
    cny = usd * conversion_rate

    # Formatear el resultado a 2 decimales y devolver como cadena
    return f"{cny:.2f} Chinese Yuan"


# Ejemplo de uso:
print(usd_to_cny(15))  # '101.25 Chinese Yuan'
print(usd_to_cny(465))  # '3138.75 Chinese Yuan'
