import modulo as m

circulo = m.Circulo(7)
perimetro = circulo.calcular_perimetro()
# está con minúscula porque hace referencia a la variable circulo de la línea anterior

area = circulo.calcular_area()
print("El perímetro del círculo es:", str(perimetro),"y el área es:", str(area))
