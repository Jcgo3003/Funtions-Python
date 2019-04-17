import sqlite3
import time
import os.path
from datetime import datetime, timedelta

# nombre BD fecha
nombrebd = time.strftime('%d%m%y',time.localtime()) + ".db"

# Vueltas
ron_a = [ 0 , 0 , 0 ]
ron_b = [ 0 , 0 , 0 ]

# Comprobar si un archivo existe
if (os.path.isfile(nombrebd)):
    print("BD existente")

    # Conectando la BD
    conexion = sqlite3.connect(nombrebd)
    print ("Leyendo BD: ", nombrebd)
    # Cursor
    c = conexion.cursor()

    ### Recuperando datos de la DB direccion A #####
    # sen1
    c.execute("SELECT sen1_a FROM a")
    bd = c.fetchall()
    ron_a[0] = len(bd)

    # sen2
    c.execute("SELECT sen2_a FROM a")
    bd = c.fetchall()
    cuenta = 0
    for i in range (len(bd)):
        if ( str(bd[i][0]) != 'None'):
            cuenta += 1
    ron_a[1] = cuenta

    # sen3
    c.execute("SELECT sen3_a FROM a")
    bd = c.fetchall()
    cuenta = 0
    for i in range (len(bd)):
        if ( str(bd[i][0]) != 'None'):
            cuenta += 1
    ron_a[2] = cuenta

    ### Recuperando datos de la DB  para la vuelta  direccion B #####
    # sen3
    c.execute("SELECT sen3_b FROM b")
    bd = c.fetchall()
    ron_b[2] = len(bd)

    # sen2
    c.execute("SELECT sen2_b FROM b")
    bd = c.fetchall()
    cuenta = 0
    for i in range (len(bd)):
        if ( str(bd[i][0]) != 'None'):
            cuenta += 1
    ron_b[1] = cuenta

    # sen1
    c.execute("SELECT sen1_b FROM b")
    bd = c.fetchall()
    cuenta = 0
    for i in range (len(bd)):
        if ( str(bd[i][0]) != 'None'):
            cuenta += 1
    ron_b[0] = cuenta

else:
    print("Creando BD ...")
    # Creando BD
    conexion = sqlite3.connect(nombrebd)
    print ("Base de datos creada: ", nombrebd)

    # Cursor
    c = conexion.cursor()

    # creando tablas
    #crear tabla dir a
    c.execute(''' CREATE TABLE "a" ('num_a' INTEGER PRIMARY KEY , 'sen1_a' TIME, 'sen2_a' TIME, 'sen3_a' TIME )''')
    #crear tabla dir b
    c.execute(''' CREATE TABLE "b" ('num_b' INTEGER PRIMARY KEY , 'sen3_b' TIME, 'sen2_b' TIME, 'sen1_b' TIME )''')

########################### Sensores Menu ###############################
res = input('Comenzar?...')
while ( res == 'y'):
    print('Las vueltas comienzan asi A', ron_a)
    print('Las vueltas comienzan asi B', ron_b)
    print("    Menu principal   ")
    # direccion
    dir = input("Direccion: ")
    ## aqui obtengo el nombre del sensor ejem... sen1_a
    sensor = input("Sensor numero: ")# ejem... sen1_a
    # de nuevo # de sensor
    num_sen = int(input("Numero: "))
    print("...")

# insertando datos en la BD
    if ( dir == 'a'):
        if (num_sen == 1 ):
            print("Guardando sen1 Direccion A")
            # Insertando tiempos a sen1
            ron_a[0] += 1
            hora_now = (time.strftime('%H:%M:%S',time.localtime()))
            c.execute('''INSERT INTO a ("num_a","sen1_a","sen2_a","sen3_a") VALUES ( ? , ? ,NULL,NULL)''', (ron_a[0], hora_now) )
        else:
            print("Guardando sen", num_sen)
            print("Direccion A")
            # para que las rondas se guarden correctamente
            num_sen -= 1
            ron_a[num_sen] += 1

            hora_now = (time.strftime('%H:%M:%S',time.localtime()))
            c.execute('''UPDATE a SET {} = ? where num_a = ? '''.format( sensor), (hora_now, ron_a[num_sen] ) )
    else:
        if (num_sen == 3 ):
            print("Guardando sen3 Direccion B")
            # Insertando tiempos a sen3
            ron_b[2] += 1
            hora_now = (time.strftime('%H:%M:%S',time.localtime()))
            c.execute('''INSERT INTO b ("num_b","sen3_b","sen2_b","sen1_b") VALUES ( ? , ? ,NULL,NULL)''', (ron_b[2], hora_now) )
        else:
            print("Guardando sen", num_sen)
            print("Direccion B")

            # para que las rondas se guarden correctamente
            num_sen -= 1

            ron_b[num_sen] += 1
            hora_now = (time.strftime('%H:%M:%S',time.localtime()))
            c.execute('''UPDATE b SET {} = ? where num_b = ? '''.format(sensor), (hora_now, ron_b[num_sen] ) )

    # Guardando los registros
    conexion.commit()

    res = input("Quieres continuar: ")

print()
print('Las vueltas terminan asi A', ron_a)
print('Las vueltas terminan asi B', ron_b)
print()

#### haciendo promedios de los tiempos ###
# Limitando numero de muestra / ron_a[2] por que es el ultimo en recibir senal
if (ron_a[2] > 5):
    # si hubo mas de 5 vueltas
    ini_a = ron_a[2] - 4
else:
    ini_a = 1

if (ron_b[0] > 5):
    # si hubo mas de 5 vueltas/ - 4 para que sea un muestra de 5
    ini_b = ron_b[0] - 4
else:
    ini_b = 1

# Leyendo cada columna Dir a
# sensores
l_sen_a = [ 'sen1_a', 'sen2_a', 'sen3_a']
# tiempos obtenidos de la BD
lista_a = []


# lista de tiempos despues de la sustracion t2- t1, t3 -t2 , etc.
lista_t = []

#promedios
pro_a = []

# valores para deltatime
FMT = '%H:%M:%S'

# iterando sobre sensores
for n in range (len(l_sen_a)):
    print('n es ', n)
    print('sensor', l_sen_a[n])

    # Leyendo la ultima fila en columna l_sen_a [ n ]
    for i in range ( ini_a ,ron_a[2] +1 ):
        c.execute('SELECT {} FROM a WHERE num_a = ?'.format( l_sen_a[n]), ( i , ))
        bd = c.fetchone()
        print('bd ', bd)
        lista_a.append( bd[0] )
        print('i = ', i)
    print('Lista_a', lista_a )

    # sacando promedio de la lista
    print()
    print("inicio llenado lista t")

    for y in range (len(lista_a) -1):
        # Obteniendo la sustracion de t2 - t1 para cada valor en lista_a
        tdel = datetime.strptime(lista_a[y+1], FMT) - datetime.strptime(lista_a[y], FMT)
        # Guardando el valor en segundos
        t_float = tdel.total_seconds()
        # Guardando el valor en la lista_t
        lista_t.append( t_float )

    print('lista t = ', lista_t)
    pro_a.append( sum(lista_t)/ len(lista_t) )
    print('promedio', pro_a)
    #borrando la listas
    lista_a.clear()
    lista_t.clear()
    print('Lista borrada lista_t', lista_t)
    print('Lista borrada lista_a', lista_a)
    print()

print('Promedios finales pro_a',pro_a)






# bd = c.fetchone()
# lista_a.append( bd[0] )

# print("Esta es la lista sen1_a",lista_a)





# cerrando conexiones
conexion.close()