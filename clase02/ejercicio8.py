""" 
Realizar un programa que calcule el area de un triangulo escaleno
"""
import math
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
s = (a+b+c)/2
area = math.sqrt(s * (s-a)*(s-b)*(s-c))
print(area)