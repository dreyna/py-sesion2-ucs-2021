"""
Realizar un programa que calcule el area de un circulo.
a = PI x r*r
"""
import math

pi = math.pi

radio = float(input("radio: "))

area = pi*pow(radio,2)

print(area)