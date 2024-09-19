import math


def to_16_9_aspect_ratio(x, y):
    # Calculamos el nuevo ancho (X) manteniendo el alto (Y) igual
    new_x = math.ceil(y * 16 / 9)

    return new_x, y


# Ejemplo de uso:
x, y = 374, 280
new_resolution = to_16_9_aspect_ratio(x, y)
print(f"Nueva resolución con aspecto 16:9: {new_resolution[0]} × {new_resolution[1]}")

# Otro ejemplo:
x, y = 500, 280
new_resolution = to_16_9_aspect_ratio(x, y)
print(f"Nueva resolución con aspecto 16:9: {new_resolution[0]} × {new_resolution[1]}")
