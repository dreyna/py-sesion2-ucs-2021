"""
Escribir un programa que solicite al usuario que ingrese su nombre.
El nombre se debe almacenar en una variable llamada nombre. 
A continuación se debe mostrar en pantalla el 
texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” 
se reemplazará por el nombre que el usuario haya ingresado.
"""
nombre = input("Ingrese su nombre: ")

mensaje = "Ahora estás en la matrix, ["+ nombre +"]"
print(mensaje)