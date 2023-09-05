# establecer los porcentajes de descuento por color
descuento_verde = 0.10
descuento_amarillo = 0.25
descuento_azul = 0.50
descuento_rojo = 1.00  # sale gratis

# Leer el color de la bolita que el cliente compró
color_bolita = input("Ingrese el color de la bolita. Los colores disponibles son: blanca, verde, amarilla, azul,  y roja): ")

# Leer el valor total de la compra
valor_compra = float(input("Ingrese el valor total de la compra: "))

# Aplicación del descuento según el color de la bolita que sacó el cliente
if color_bolita == "blanca":
    valor_final = valor_compra # no tiene descuesto alguno
elif color_bolita == "verde":
    valor_final = valor_compra - (valor_compra * descuento_verde)
elif color_bolita == "amarilla":
    valor_final = valor_compra - (valor_compra * descuento_amarillo)
elif color_bolita == "azul":
   valor_final = valor_compra - (valor_compra * descuento_azul)
elif color_bolita == "roja":
    valor_final = valor_compra - (valor_compra * descuento_rojo)
else:
    print("el color de la bolita no es valido")
    valor_final = None # "none" porque no hubo un color valido para la bolita

# Mostrar el monto final a pagar
if valor_final is not None:
    print(f"Valor total a pagar: {valor_final}") # si el color de la bolita fue valido, se hará su respectivo descuento
