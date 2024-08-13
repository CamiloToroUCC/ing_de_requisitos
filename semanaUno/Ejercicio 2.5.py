b = float(input("Altura (A): "))
a = float(input("Base (B): "))
c = float(input(" Lado (C): "))

area_rectangulo = (b*c)

area_triangulo = ((a-c)*b)/2

# Salida de resultados
print(f"Área de el Rectangulo : {area_rectangulo}metrois cuadrados")
print(f"Área de  el Triangulo : {area_triangulo}metrois cuadrados")
print(f"Área Total : {area_triangulo + area_rectangulo} metrois cuadrados")
