'''
En cuanto tiempo tomare agua
para hidratarme
'''

import math
def litres(time):
    # Calcular la cantidad de litros
    litres = time * 0.5

    # Redondear hacia abajo (usar floor en lugar de truncar)
    return math.floor(litres)


# Ejemplos de uso:
print(litres(3))  # Devuelve 1
print(litres(6.7))  # Devuelve 3
print(litres(11.8))  # Devuelve 5
