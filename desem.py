estado_actual = 0

res  = 'y'

while( res == 'y'):
    tdel = int(input("Introducir un valor para ser evaluado "))
    #  Evaluando desempeno del metro
    if tdel < 10:
        estado_actual = 'a'
    elif( tdel >= 10 and tdel < 20):
        estado_actual = 'b'
    elif( tdel >= 20 and tdel < 30):
        estado_actual = 'c'
    elif( tdel >=30 and tdel < 40):
        estado_actual = 'd'
    elif ( tdel >= 40 and tdel < 50):
        estado_actual = 'f'
    else:
        print('Super retrasado')
        estado_actual = 'No service'

    print('El estado actual es ', estado_actual)

    res = input('Quieres continuar ')
