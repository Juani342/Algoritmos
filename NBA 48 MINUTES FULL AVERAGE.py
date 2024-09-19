'''
Cual es el puntaje del jugador en un partido
'''

def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    extrapolated_ppg = (ppg / mpg) * 48
    return round(extrapolated_ppg, 1)

# Ejemplos de uso:
print(nba_extrap(12, 20))  # Devuelve 28.8
print(nba_extrap(10, 10))  # Devuelve 48.0
print(nba_extrap(5, 17))   # Devuelve 14.1
print(nba_extrap(0, 0))    # Devuelve 0
