"""
Escribir un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos
por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. 
Mostrar el consumo de combustible por kilómetro.
"""
km = float(input("Kilometros: "))
comb = float(input("Combustible: "))
consumo = km/comb
print("Consume de combustible "+ str(consumo))