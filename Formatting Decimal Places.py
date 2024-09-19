'''
Formato de decimales
'''

def redondear_y_formatar(numero):
    # Redondear el número a dos decimales
    numero_redondeado = round(numero, 2)

    # Formatear el número con dos decimales
    numero_formateado = "{:.2f}".format(numero_redondeado)

    return numero_formateado


# Ejemplos de uso:
print(redondear_y_formatar(5.5589))  # Devuelve "5.56"
print(redondear_y_formatar(3.3424))  # Devuelve "3.34"
