'''
Cuanto cuesta un mango
'''

def mango(quantity, price):
    # Calcula la cantidad de mangos que se pagan
    paid_mangos = quantity - (quantity // 3)

    # Calcula el costo total
    total_cost = paid_mangos * price

    return total_cost


# Ejemplos de uso:
print(mango(2, 3))  # Devuelve 6
print(mango(3, 3))  # Devuelve 6
print(mango(5, 3))  # Devuelve 12
print(mango(9, 5))  # Devuelve 30
