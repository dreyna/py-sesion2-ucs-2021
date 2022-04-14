'''
Una panadería vende barras de pan a S/. 3.50 cada una. El pan que no es el día tiene un 
descuento del 60%. Escribir un programa que comience leyendo el número de barras 
vendidas que no son del día. Después el programa debe mostrar el precio habitual de 
una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

'''
nb = int(input("N° de Barras: "))
ph = 3.50
desc = nb*0.6
ft = nb*ph-desc

print("Precio: "+str(ph))
print("Descuento: "+str(desc))
print("Coste Final: "+str(ft))



