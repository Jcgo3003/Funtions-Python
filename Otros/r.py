
lista = [ 6, 0, 0 ]
long_real = 0
suma = 0
for i in lista:
    if (i != 0 and i != 6):
        long_real += 1
        suma += i

print('long_real', long_real)
print('suma', suma)
if (suma == 0):
    final = 6
else:
    final = round(suma/long_real)

print('Evaluacion final', final)