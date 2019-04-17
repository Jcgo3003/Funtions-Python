import sqlite3
import time
# comprobar si existe un archivo
import os.path

### esta base de datos teoricamente solamente se abrira solo una vez PERO
# si llega a haver un problema con el servidor que la base de datos sea recuperable y
# pueda arrancar leyendo los datos en caso de error

# Nombrando la BD de acuerdo con el dia
# Obteniedo dia + '.db '
# nombrebd = time.strftime('%d%m%y_%H%M%S',time.localtime()) + ".db"### con fecha y hora
nombrebd = time.strftime('%d%m%y',time.localtime()) + ".db" ##solo fecha

# esto es para la libreria de cs50 no es necesario
#dir = "sqlite:///" + nombrebd

print(nombrebd)

# declarando la lista que llevara la cuenta de las veces que ha pasado el metroy su estado
# un numero para cada sensor
ron_a = [ 0 , 0 , 0 ]
ron_b = [ 0 , 0 , 0 ]

# Comprobar si un archivo existe
if (os.path.isfile(nombrebd)):
    print("base existe")
    ## por lo mismo tiene que leer los datos de los turnos en que se quedo la bd
    # leyendo veces en que ha pasado el metro


else:
    print("Creando BD ...")
    # Creando BD
    conexion = sqlite3.connect(nombrebd)
    print ("Base de datos creada: ", nombrebd)

    # Cursor
    c = conexion.cursor()

    # creando tablas
    #crear tabla con direciona a   ###################
    c.execute(''' CREATE TABLE "sens_dir_a" ('num' INTEGER PRIMARY KEY , 'sen1_a' TIME, 'sen2_a' TIME, 'sen3_a' TIME )''')
    #crear tabla con direcion b
    c.execute(''' CREATE TABLE "sens_dir_b" ('num' INTEGER PRIMARY KEY , 'sen1_b' TIME, 'sen2_b' TIME, 'sen3_b' TIME )''')



# Conectando la BD
conexion = sqlite3.connect(nombrebd)
print ("Leyendo BD: ", nombrebd)

# Cursor
c = conexion.cursor()

########################### Sensores direcion A ###############################

#insertando primer tiempo sensor1 a ################################
# c.execute('''INSERT INTO "sens_dir_a" ("num","sen1_a","sen2_a","sen3_a") VALUES ('1','12:00:06',NULL,NULL)''', )
dire = 'sens_dir_a'
ron_a = 1
hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
c.execute('''INSERT INTO {} ("num","sen1_a","sen2_a","sen3_a") VALUES ( ? , ? ,NULL,NULL)'''.format( dire ), (ron_a, hora_now) )



# insertando datos para sensor 2 y 3 a
c.execute('''UPDATE "sens_dir_a" SET "sen2_a" = '12:05:06' where num = 1''')
c.execute('''UPDATE "sens_dir_a" SET "sen3_a" = '12:10:06' where num = 1''')


##################################################################################
### solo de esta menera acepta los datos - aunque puede ser inseguro  lo dudo
### todos nuestros datos vienen del programa en ningun momento hay un usuario directamente
### conectado a la BD

ronda = [ 1 , 0 , 0 ]
ronda[0] += 1
print (ronda[0])
hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
#insertando segunda ronda tiempo sensor1 a
c.execute('''INSERT INTO sens_dir_a ("num","sen1_a","sen2_a","sen3_a") VALUES ( ? , ? ,NULL,NULL)''', (ronda[0], hora_now) )

# asi funciona
# c.execute('''INSERT INTO sens_dir_a ("num","sen1_a","sen2_a","sen3_a") VALUES ( ? ,'12:05:06',NULL,NULL)''', ronda)
#c.execute('''INSERT INTO sens_dir_a ("num","sen1_a","sen2_a","sen3_a") VALUES ( 2 , ? ,NULL,NULL)''', hora_now )

# insertando datos para sensor 2 y 3 a
c.execute('''UPDATE "sens_dir_a" SET "sen2_a" = '12:10:06' where num = 2''')
c.execute('''UPDATE "sens_dir_a" SET "sen3_a" = '12:19:06' where num = 2''')

########################### Sensores direcion B ###############################
#insertando primer tiempo sensor1 b
c.execute('''INSERT INTO "sens_dir_b" ("num","sen1_b","sen2_b","sen3_b") VALUES ('1','12:01:06',NULL,NULL)''')

# insertando datos para sensor 2 y 3 a
c.execute('''UPDATE "sens_dir_b" SET "sen2_b" = '12:07:06' where num = 1''')
c.execute('''UPDATE "sens_dir_b" SET "sen3_b" = '12:11:06' where num = 1''')

#insertando segunda ronda sensor2
c.execute('''INSERT INTO "sens_dir_b" ("num","sen1_b","sen2_b","sen3_b") VALUES ('2','12:05:06',NULL,NULL)''')

###################################################
# insertando datos con tiempo real
# dir nombre la BD a insertar 'Direccion de la BD'
dir = 'sens_dir_b'

# Sensor que inserta la informacion
sen = 'sen3_b'
num_sen = 3
# hora en que se da el registro
hora_now = (time.strftime('%H:%M:%S',time.localtime()) )
# Insertando todo eso una sola orden
c.execute('''UPDATE {} SET {} = ? where num = ? '''.format( dir, sen), (hora_now, num_sen ) )



# c.execute('''UPDATE "dir_a" SET {} = ? where num = ? '''.format( sen), ( hora_now, ron_a[num_sen]))
# Una orden regular
c.execute('''UPDATE "sens_dir_b" SET  "sen2_b"  =  '12:07:06' where num = 2''')



# Imprimiendo datos de manera segura ########
print("Imp solol sen1_a de dir A en el numero 1")
num = ('1',)
c.execute('SELECT sen1_a FROM sens_dir_a WHERE num =?', num)
time = c.fetchone()
print(time[0])
print()

# Imprimiendo datos de manera segura
print("Imp ' * todo ' de sens dir B en el numero 1 ")
t = ('1',)
c.execute('SELECT * FROM sens_dir_b WHERE num =?', t)
print(c.fetchone())


#insertando tercera ronda sensor2
c.execute('''INSERT INTO "sens_dir_b" ("num","sen1_b","sen2_b","sen3_b") VALUES ('3','12:05:06',NULL,NULL)''')


############### leyendo los datos ####################
# Imprimiendo datos de manera segura
print("Este es el ultimo registro de la tabla Sens dir b ")
n = ('1',)
c.execute("SELECT * FROM sens_dir_b WHERE  num = (SELECT MAX(num) FROM sens_dir_b)")
# Imprimiendo el maximo valor de sens_dir_b
print('Este es el maximo valor de sens_dir_b')
bd = c.fetchone()
# este es bd
print("asi queda " , bd)

#### Leyendo la BD para colocar los turnos ##############
# reglas
# para sens dir b  sen3 siempre obtendra el maximo nume
ron_b[2] = bd[0]
# para sen d



# Guardando los registros
conexion.commit()



###pero como leer los datos????
# solo obtendria nulo en los datos que no han sido introducidos
# por lo que tendria que hacer algo asi como una funcion que diga:
# pero el rellenador de datos incluso deberia ir incluso mas lejos y leer los datos
# de base de datos hasta que en todos los datos sean diferente de NULO
###########################################################################
# obtener datos sobre la tabla es decir necesito saber el ultimo numero introducido a la tabla
#   Cuantas entradas tiene la tabla y cual es el valor de num en la ultima entradaT
    # if NUll = 0




# # insertando primer tiempo sensor2
# # aqui tendria que formular nuevas reglas para hacer que los datos obtenidos de
# # request sea correctos en plan si hora de sen_2 es anterior que sen_1 marcar error
# # o ni si quiera aceptarla hasta obtener una hora mas tarde
# # ademas de que cada vez que se registre un  request post tendra una variable
# # por cada sensor que se dedicara a contar las veces que ha sido activado dicho sensor
# # y tal vez ahi mismo se debe tener existir las reglas como la anterior y una vez que
# # los datos obtenidos esten 'limpios' se pueden agregar a la bd
# # Limpiando los datos
# # - antes de subirlos a la bd
# # sensor2 no puede ser activado antes que sensor1 y asi sucesivamente con cada numero
# # - Despues de subirlos a la bd
# # los datos obtenidos de un solo sensor se deben comparar entre si y encotrar un punto medio
# #           es decir si casi todos los datos de la muestra estan cerca de '10' desechar los datos con
# #           numeros menores o mayores en un rago de 5 < 10 y 10 > 15 para mantener limpia la base de datos
# #           y lograr un promedio 'real'


# CREATE TABLE 'table' ('num' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'sen1' DATETIME, 'sen2' DATETIME, 'sen3' DATETIME)

############# bdpart4 agregando un query a una lista #############
# c.execute('SELECT sen1_a FROM a WHERE num_a = ?', (i, ))
# bd = c.fetchone()
# lista_a.append(  bd[0] )


# c.execute('SELECT {} FROM a WHERE num_a = ?'.format( lis[0]), ( i , ))