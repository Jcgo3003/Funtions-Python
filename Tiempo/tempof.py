# Promedios dentro
import time
from datetime import datetime, timedelta
import datetime as dt

# Listas para guardar Estados
est_a = [ 0, 0, 0 ]
est_b = [ 0, 0, 0 ]

# Listas para guardar promedios
prom_a = [ 6, 9, 12 ]
prom_b = [ 10, 7, 10 ]

# lista para identificar # vueltas
ron_a = [ 0, 0, 0 ]
ron_b = [ 0, 0, 0 ]

# Lista para guardar hora_esp
hora_esp_a = [ 0, 0, 0 ]
hora_esp_b = [ 0, 0, 0 ]

# valores para delta time
FMT = '%H:%M:%S'

# Var. para saber si ya estan los promedios dentro
listo  = 0

#Var. Identificar sensor
direc = 'N'
num_sen = 0

tipo = 'y'

while ( tipo == 'y' ):

    # Funcion para determinar tipos de datos
    print('Menu')
    print('1 - Promedios ')
    print('2 - Sensor ')
    print('3 - Datos ')
    print('N - Terminar programa ')

    tipo = int(input('Introducir seleccion '))

    if (tipo == 1):
        prom_a[0] = int(input('Promedio sensor 1 '))
        prom_a[1] = int(input('Promedio sensor 2 '))
        prom_a[2] = int(input('Promedio sensor 3 '))
        print()
        prom_b[0] = int(input('Promedio sensor 1 '))
        prom_b[1] = int(input('Promedio sensor 2 '))
        prom_b[2] = int(input('Promedio sensor 3 '))

        listo = 1

    elif (tipo == 2):
            #   Indentificando el sensor
            direc = input('Direccion ')
            num_sen = int(input('Numero de sensor '))

            # Identificando Num. sen en la lista
            num_sen -= 1

            # Registro/inicio de toma de tiempo
            # Direccion
            if (direc == 'a'):
                #Leer el num. de ronda por sensor
                ron = ron_a[num_sen]

                # Modulo 1 Activando hora_esp por primera vez
                if ron == 0:
                    #### Tiempo promedio en segundos ####
                    t_pro_s = int(round( prom_a[num_sen])) # debe ser redondeado

                    # Conversion a tiempo en h,m,s en datetime formato
                    t_pro_f = dt.timedelta(seconds = t_pro_s)

                    # Introduccion de tiempo NOW en datetime
                    t_now = dt.datetime.now()

                    # Suma de esos tiempos para crear TIEMPO ESPERADO
                    t_esp = t_pro_f + t_now
                    hora_esp_a [num_sen] = t_esp

                    # suma a rondas
                    ron_a[num_sen] += 1

                    print('Primer regitro ')
                    print('A sen', num_sen + 1)


                # Modulo 2 Para sacar el tiempo que se tardo en activar la alarmas
                else:
                    # Hora Now
                    t_now = dt.datetime.now()

                    # Conversion de TIEMPO ESPERADO a formato STR de nuevo para que pueda ser evaluado
                    t_esp = hora_esp_a[num_sen]
                    t_esp_str = t_esp.strftime('%H:%M:%S')
                    t_now_str = t_now.strftime('%H:%M:%S')

                    # Resta
                    tdel = datetime.strptime(t_now_str, FMT) - datetime.strptime(t_esp_str, FMT)
                    t_int = int(round(tdel.total_seconds()))

                    # crear TIEMPO ESPERADO
                    t_esp = t_pro_f + t_now
                    hora_esp_a [num_sen] = t_esp

                    # suma a rondas
                    ron_a[num_sen] += 1
                    print("Tiempo esperado 2 ",t_esp)

                    ####### Evaluando el tiempo esperado con los ifs
                    if ( t_int < 0) :
                        estado_actual = 'O'
                    elif( t_int >= 0 and t_int < 10):
                        estado_actual = 'a'
                    elif( t_int >= 10 and t_int < 20):
                        estado_actual = 'b'
                    elif( t_int >= 20 and t_int < 30):
                        estado_actual = 'c'
                    elif( t_int >=30 and t_int < 40):
                        estado_actual = 'd'
                    elif ( t_int >= 40 and t_int < 50):
                        estado_actual = 'f'
                    else:
                        print('Super retrasado ')
                        estado_actual = 'No service'

                    est_a[num_sen] = estado_actual
                    print('Estado actual', est_a[num_sen])

            # Direccion b
            elif (direc == 'b'):
                #Leer el num. de ronda por sensor
                ron = ron_b[num_sen]

                # Activando hora_esp por primera vez
                if ron == 0:

                    #### Tiempo promedio en segundos ####
                    t_pro_s = int(round( prom_b[num_sen])) # debe ser redondeado

                    # Conversion a tiempo en h,m,s en datetime formato
                    t_pro_f = dt.timedelta(seconds = t_pro_s)

                    # Introduccion de tiempo NOW en datetime
                    t_now = dt.datetime.now()

                    # Suma de esos tiempos para crear TIEMPO ESPERADO
                    t_esp = t_pro_f + t_now
                    hora_esp_b [num_sen] = t_esp

                    # suma a rondas
                    ron_b[num_sen] += 1

                    print('Primer regitro ')
                    print('B sen', num_sen + 1)

                # Para sacar el tiempo que se tardo en activar la alarmas
                else:
                    # Hora Now
                    t_now = dt.datetime.now()

                    # Conversion de TIEMPO ESPERADO a formato STR de nuevo para que pueda ser evaluado
                    t_esp = hora_esp_b[num_sen]
                    t_esp_str = t_esp.strftime('%H:%M:%S')
                    t_now_str = t_now.strftime('%H:%M:%S')

                    # Resta
                    tdel = datetime.strptime(t_now_str, FMT) - datetime.strptime(t_esp_str, FMT)
                    t_int = int(round(tdel.total_seconds()))

                    # crear TIEMPO ESPERADO
                    t_esp = t_pro_f + t_now
                    hora_esp_b[num_sen] = t_esp

                    # suma a rondas
                    ron_b[num_sen] += 1
                    print("Tiempo esperado ",t_esp)

                    ####### Evaluando el tiempo esperado con los ifs
                    if ( t_int < 0) :
                        estado_actual = 'O'
                    elif( t_int >= 0 and t_int < 10):
                        estado_actual = 'a'
                    elif( t_int >= 10 and t_int < 20):
                        estado_actual = 'b'
                    elif( t_int >= 20 and t_int < 30):
                        estado_actual = 'c'
                    elif( t_int >=30 and t_int < 40):
                        estado_actual = 'd'
                    elif ( t_int >= 40 and t_int < 50):
                        estado_actual = 'f'
                    else:
                        print('Super retrasado')
                        estado_actual = 'No service'

                    est_b[num_sen] = estado_actual
                    print('Estado actual', est_b[num_sen])

    elif (tipo == 3):
        print('Listas para guardar Estados')
        print('A', est_a)
        print('B', est_b)
        print('Listas para guardar promedios')
        print('A', prom_a)
        print('B', prom_b)
        print('lista para identificar # vueltas')
        print('A', ron_a)
        print('B', ron_b)
        print('Lista para guardar hora_esp')
        print('A', hora_esp_a)
        print('B', hora_esp_b)


    tipo = input('Quieres continuar ')





# Funcion para obtener datos Promedio



# Funcion para utilizar datos Promedio y comenzar a contar tiempo


# Funcion para Evaluar esos datos