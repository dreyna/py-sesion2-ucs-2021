
cad = "Hola mundo"
print(cad)
print(type(cad))
w = 100
z = 200
s = "El valor solicitado: "+ str(w)
q = "El valor solicitado: %d" % w
print(s)
print(q)
d = "Los valores solicitados %d y %d" %(w,z)
print(d)
h = "Los valores solicitados {} y {}".format(w,z)
print(h)
p = "Los valores solicitados {a} y {b}".format(a = w,b = z)
print(p)