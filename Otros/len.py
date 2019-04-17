a = [ 0, 3, 0 ]
print(a)

#############
# creando for loop para contabilizar
# Haciendolo de esta manera i toma el valor de a en la lista
long_real = 0
suma = 0
for i in a:
    if i != 0:
        long_real += 1
        suma += i

print('La suma es',suma)
print('Entre', long_real)
print('El resultado final es', suma/long_real)
print('El resultado final es', round(suma/long_real))

    # print('a', a[i])
    # print(i)

print('Separacion')

# # Haciendolo de esta manera i solo cuenta de 0 a 2, si se conserva como contador
# for i in range(0, len(a)):
#     print('a', a[i])
#     print(i)

# print(a)

# Necesito que esta nueva funcion
# haga los promedio pero que sepa distinguir
# Reglas de distincion
#   1 Si si hay numeros 0 dentro de uno de los contenedores - Ingnorarlo
#       y hacer el promedio sin ese numero ni tomandolo en cuenta
#       si a = [1, 1, 0] solo se suman esos dos 1 y se ignora por completo el 0
#       Quedando en plan 1 + 1 / 2
# Para hacerlo tendre que hacer un for loop que recorra la lista y cuente los 0
#   si numero != 0 -  Agregar +1 al contador de numeros
#   si numero == 0 apuntar su numero en la lista y hacer no sume ese en el siguiente
#   For loop que se encargara de sumar
