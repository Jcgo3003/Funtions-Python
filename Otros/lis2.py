lis = [ 0 , 0, 1, 6 ]

print(lis)

long_real = 0
suma = 0

for i in lis:
    print(i)
    if i != 0:
        long_real += 1
        suma += i
    if i == 6:
        final = 6
        print('seis')

print(suma)
print('entre', long_real)

final = round(suma/long_real)
print('Evaluacion final', final)