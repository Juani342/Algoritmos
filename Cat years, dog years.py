def human_years_cat_years_dog_years(humanYears):
    # Inicializamos las variables para los años de gato y perro
    catYears = 0
    dogYears = 0

    # Calculamos los años de gato y perro según los años humanos
    if humanYears >= 1:
        catYears += 15
        dogYears += 15
    if humanYears >= 2:
        catYears += 9
        dogYears += 9
    if humanYears > 2:
        catYears += (humanYears - 2) * 4
        dogYears += (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]

# Ejemplo de uso:
print(human_years_cat_years_dog_years(1))  # [1, 15, 15]
print(human_years_cat_years_dog_years(2))  # [2, 24, 24]
print(human_years_cat_years_dog_years(10)) # [10, 56, 64]))
