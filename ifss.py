numero = int (input("Dame un numero si es 10 o 12 sera verdadero "))
print(numero)
if ( numero == 10 or numero == 12):
    print("Tu numero SI es 10 o 12")
else:
    print("Tu numero NO es 10 o 12 ")

print('Fin del programa')

# El problema fue que la variable 'numero' no era tomanda como 'int'
# Por lo que el if no reconocia el numero introducido