# Introduccion de datos en lista registro BD

num_sen = 5
print("Guardando registro a sen%s_a" % (num_sen))

# lista a la que se le asignaran los registros
ron_a = [ 0 , 0 , 0 ]

res = input("Quieres comenzar? ")
while res == 'y' :
    print('Introducce un numero del 1-3 para rellenar la lista')
    r = int(input('A donde quieres agregar un numero '))

    if r == 1:
        # agregando el numero a la lista para depues comparar ese paramentro
        ron_a[0] += 1

        # el lugar uno tiene casi entradas ilimitadas al ser el que lleva a todos
        # igual le pondre un limite de maximo 5 entradas arriva que el resto solo por precauicion
        if (ron_a[0] == (ron_a[1] + 5)):
            print('Error, no se puede guardar el registro - 1 ya tiene demasiados registros')
            ron_a[0] -= 1
        else:
            print('Guardado')

        print(ron_a)

    elif r == 2:
        # Sumando a lista 2
        ron_a[1] += 1
        # protegiendo la lista
        if ((ron_a[1] > ron_a[0])):
            print('Error de registro 2 no puede ser superior a 1')
            ron_a[1] -= 1
        else:
            print('Guardando')

        print(ron_a)
    else:
        # Sumando a lista 3
        ron_a[2] += 1
        # protegiendo la lista
        if ((ron_a[2] > ron_a[1])):
            print('Error de registro 3 no puede ser superior a 2')
            ron_a[2] -= 1
        else:
            print('Guardando')

        print(ron_a)



    res = input("Quieres continuar? ")

# ahora debo agragar la funcion que se encargue de revisar que la lista esta en correcto orden
# listo hora de implementar en la bdfinal7.py