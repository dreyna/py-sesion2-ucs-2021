import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
p = b-4*a*c
if(p>0):
    x1 = (-b + math.sqrt(p))/2*a
    x2 = (-b - math.sqrt(p))/2*a
    print(x1)
    print(x2)
else:
    print("No se puede calcular")
