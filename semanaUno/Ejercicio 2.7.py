litros_producidos = float(input("Ingrese la cantidad de litros producidos: "))

galones_entregados = litros_producidos / 3.785
precio_por_galon = 4.50

# Cálculo del monto total
monto_total = galones_entregados * precio_por_galon

print(f"Se recibio ${monto_total} por la entrega de su producción.")