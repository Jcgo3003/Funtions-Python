import time
from datetime import datetime, timedelta

# Listas para guardar Estados
est_a = [ 0, 0, 0 ]
est_b = [ 0, 0, 0 ]


# Listas para guardar promedios
prom_a = [ 0, 0, 0 ]
prom_b = [ 0, 0, 0 ]

# lista para identificar # vueltas
ron_a = [ 0, 0, 0 ]
ron_b = [ 0, 0, 0 ]

# Lista para guardar hora_esp
hora_esp_a = [ 0, 0, 0 ]
hora_esp_b = [ 0, 0, 0 ]

# valores para delta time, hora, minuto, segundos
FMT = '%H:%M:%S'

# Var. para saber si ya estan los promedios dentro
listo  = 0

#Var. Identificar sensor
direc = 'N'
num_sen = 0

# Funcion para determinar tipos de datos
print('Menu')
print('1 - Promedios')
print('2 - Sensor')
print('3 - Terminar programa')
tipo = input('Introducir tipo de dato')


while ( tipo != 3 and listo == 0 ):
    if (tipo == 1):
        prom_a[0] = input('Promedio sensor 1 ')
        prom_a[1] = input('Promedio sensor 2 ')
        prom_a[2]= input('Promedio sensor 3 ')
        print()
        prom_b[0] = input('Promedio sensor 1 ')
        prom_b[1] = input('Promedio sensor 2 ')
        prom_b[2] = input('Promedio sensor 3 ')

        listo = 1
    elif (tipo == 2):
            #   Indentificando el sensor
            direc = input('Direccion ')
            num_sen = input('Numero de sensor ')

            # Identificando Num. sen en la lista
            num_sen -= 1

            # Registro/inicio de toma de tiempo
            # Direccion
            if (direc == 'a'):
                #Leer el num. de ronda por sensor
                ron = ron_a[num_sen]

                # Activando hora_esp por primera vez
                if ron == 0:
                    # tomar la hora actual
                    hora_now = (time.strftime('%H:%M:%S',time.localtime()))

                    # Creando hora_esp
                    hora_esp_a[num_sen]= hora_now + prom_a[num_sen]
                    print('Primer regitro')
                    print('A sen', num_sen + 1)
                    print('Hora esperada', hora_esp_a[num_sen])

                # Para sacar el tiempo que se tardo en activar la alarmas
                else:
                    # Tomar la hora actual
                    hora_now = (time.strftime('%H:%M:%S',time.localtime()))

                    # Delta de la hora actual
                    tdel = datetime.strptime(hora_now, FMT) - datetime.strptime(hora_esp_a[num_sen], FMT)

                    # Evaluando desempeno
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

                    est_a[num_sen] = estado_actual
                    print('Estado actual', est_a[num_sen])

                    hora_esp_a[num_sen] = hora_now + prom_a[num_sen]
                    print('Hora esperada', hora_esp_a[num_sen])

            # Direccion b
            elif (direc == 'b'):
                #Leer el num. de ronda por sensor
                ron = ron_b[num_sen]

                # Activando hora_esp por primera vez
                if ron == 0:
                    # tomar la hora actual
                    hora_now = (time.strftime('%H:%M:%S',time.localtime()))

                    # Creando hora_esp
                    hora_esp_b[num_sen]= hora_now + prom_b[num_sen]
                    print('Primer regitro')
                    print('B sen', num_sen + 1)
                    print('Hora esperada', hora_esp_a[num_sen])
                # Para sacar el tiempo que se tardo en activar la alarmas
                else:
                    # Tomar la hora actual
                    hora_now = (time.strftime('%H:%M:%S',time.localtime()))

                    # Delta de la hora actual
                    tdel = datetime.strptime(hora_now, FMT) - datetime.strptime(hora_esp_b[num_sen], FMT)


                    # Evaluando desempeno
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

                    est_b[num_sen] = estado_actual
                    print('Estado actual', est_b[num_sen])

                    hora_esp_b[num_sen] = hora_now + prom_b[num_sen]
                    print('Hora esperada', hora_esp_b[num_sen])


    tipo = input('Quieres continuar')





# Funcion para obtener datos Promedio



# Funcion para utilizar datos Promedio y comenzar a contar tiempo


# Funcion para Evaluar esos datos