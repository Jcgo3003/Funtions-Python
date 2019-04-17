import sqlite3
import time
import os.path

# nombre BD fecha
nombrebd = time.strftime('%d%m%y',time.localtime()) + ".db"

# Vueltas por BD
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

    # Recuperando datos de la DB
    # sen1
    c.execute("SELECT sen1_a FROM dir_a")
    bd = c.fetchall()
    ron_a[0] = len(bd)

    # sen2
    c.execute("SELECT sen2_a FROM dir_a")
    bd = c.fetchall()
    cuenta = 0
    for i in range (len(bd)):
        if ( str(bd[i][0]) != 'None'):
            cuenta += 1
    ron_a[1] = cuenta

    # sen3
    c.execute("SELECT sen3_a FROM dir_a")
    bd = c.fetchall()
    cuenta = 0
    for i in range (len(bd)):
        if ( str(bd[i][0]) != 'None'):
            cuenta += 1
    ron_a[2] = cuenta
    print('Las vueltas comienzan asi', ron_a)


else:
    print("Creando BD ...")
    # Creando BD
    conexion = sqlite3.connect(nombrebd)
    print ("Base de datos creada: ", nombrebd)

    # Cursor
    c = conexion.cursor()

    # creando tablas
    #crear tabla dir a
    c.execute(''' CREATE TABLE "dir_a" ('num_a' INTEGER PRIMARY KEY , 'sen1_a' TIME, 'sen2_a' TIME, 'sen3_a' TIME )''')
    #crear tabla dir b
    c.execute(''' CREATE TABLE "dir_b" ('num_b' INTEGER PRIMARY KEY , 'sen3_b' TIME, 'sen2_b' TIME, 'sen1_b' TIME )''')


###############################################################################
########################### Sensores direcion A ###############################

# Insertando tiempos a dir a #####
ron_a[0] += 1
c.execute('''INSERT INTO "dir_a" ("num_a","sen1_a","sen2_a","sen3_a") VALUES ( ?,'12:00:06',NULL,NULL)''', (ron_a[0], ))

# insertando datos para sensor 2 y 3 a #######
ron_a[1] += 1
c.execute('''UPDATE "dir_a" SET "sen2_a" = '12:05:06' where num_a = ?''', (ron_a[1], ))
ron_a[2] += 1
c.execute('''UPDATE "dir_a" SET "sen3_a" = '12:10:06' where num_a = ?''', (ron_a[2], ))


########### aqui terminia una vuelta ##############
############## segunda vuelta ####################
# varibles que llegaran desde el http request ESTA INSTRUCCION ES SOLO PARA SEN1
ron_a[0] += 1
hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
#insertando segunda ronda tiempo sensor1
c.execute('''INSERT INTO dir_a ("num_a","sen1_a","sen2_a","sen3_a") VALUES ( ? , ? ,NULL,NULL)''', (ron_a[0], hora_now) )

## sen 2
ron_a[1] += 1
hora_1 = (time.strftime('%H:%M:%S',time.localtime())  )
c.execute('''UPDATE "dir_a" SET "sen2_a" = ? where num_a = ?''', (hora_1 ,ron_a[1] ) )
### sen 3
ron_a[2] += 1
hora_2 = (time.strftime('%H:%M:%S',time.localtime())  )
c.execute('''UPDATE "dir_a" SET "sen3_a" = ? where num_a = ?''', (hora_2 ,ron_a[2] ) )



########### tercer vuelta queda incompleta ################
# varibles que llegaran desde el http request ESTA INSTRUCCION ES SOLO PARA SEN1
ron_a[0] += 1
hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
#insertando segunda ronda tiempo sensor1
c.execute('''INSERT INTO dir_a ("num_a","sen1_a","sen2_a","sen3_a") VALUES ( ? , ? ,NULL,NULL)''', (ron_a[0], hora_now) )

print('asi quedo rondas', ron_a)



###########################   imprimiendo                  ###########################
#### fetchall devuelve un tuple dentro de otro tuple!!!!!###
c.execute("SELECT sen1_a FROM dir_a")
bd = c.fetchall()
print('asi quedo BD 1', bd)
print('Sen1 tiene ', len(bd))

### para contar las entradas de las otras columnas se debe hacer un conteo uno por uno
c.execute("SELECT sen2_a FROM dir_a")
bd = c.fetchall()
print()
print('asi quedo BD 2 ', bd)
cuenta = 0
for i in range (len(bd)):
    if ( str(bd[i][0]) != 'None'):
        cuenta += 1
print('Sen2 tiene ', cuenta)
# guardando la vuelta en ron_a
ron_a[1] = cuenta
###### Imp sen3 #######
print()
c.execute("SELECT sen3_a FROM dir_a")
bd = c.fetchall()
cuenta = 0
for i in range (len(bd)):
    if ( str(bd[i][0]) != 'None'):
        cuenta += 1
# guardando la vuelta en ron_a
ron_a[2] = cuenta
print('asi quedo BD 3', bd)
print('Sen3 tiene ', cuenta)

# impriendo la lista de vueltas
print('las rodas quedaron asi',ron_a)


##### para recuperar el numero correcto de vueltas #####





# ########################### Sensores direcion B ###############################
# #insertando primer tiempo sensor1 b
# c.execute('''INSERT INTO "sens_dir_b" ("num","sen1_b","sen2_b","sen3_b") VALUES ('1','12:01:06',NULL,NULL)''')

# # insertando datos para sensor 2 y 3 a
# c.execute('''UPDATE "sens_dir_b" SET "sen2_b" = '12:07:06' where num = 1''')
# c.execute('''UPDATE "sens_dir_b" SET "sen3_b" = '12:11:06' where num = 1''')

# #insertando segunda ronda sensor2
# c.execute('''INSERT INTO "sens_dir_b" ("num","sen1_b","sen2_b","sen3_b") VALUES ('2','12:05:06',NULL,NULL)''')

# ###################################################
# # insertando datos con tiempo real
# # dir nombre la BD a insertar 'Direccion de la BD'
# dir = 'sens_dir_b'
# # Sensor que inserta la informacion
# sen = 'sen3_b'
# # hora en que se da el registro
# up = (time.strftime('%H:%M:%S',time.localtime()),  )
# # Insertando todo eso una sola orden
# c.execute('''UPDATE {} SET {} = ? where num = 2 '''.format( dir, sen), up )

# # Una orden regular
# c.execute('''UPDATE "sens_dir_b" SET  "sen2_b"  =  '12:07:06' where num = 2''')



# # Imprimiendo datos de manera segura ########
# print("Imp solol sen1_a de dir A en el numero 1")
# num = ('1',)
# c.execute('SELECT sen1_a FROM sens_dir_a WHERE num =?', num)
# time = c.fetchone()
# print(time[0])
# print()

# # Imprimiendo datos de manera segura
# print("Imp ' * todo ' de sens dir B en el numero 1 ")
# t = ('1',)
# c.execute('SELECT * FROM sens_dir_b WHERE num =?', t)
# print(c.fetchone())


# #insertando tercera ronda sensor2
# c.execute('''INSERT INTO "sens_dir_b" ("num","sen1_b","sen2_b","sen3_b") VALUES ('3','12:05:06',NULL,NULL)''')


# ############### leyendo los datos ####################
# # Imprimiendo datos de manera segura
# print("Este es el ultimo registro de la tabla Sens dir b ")
# n = ('1',)
# c.execute("SELECT * FROM sens_dir_b WHERE  num = (SELECT MAX(num) FROM sens_dir_b)")
# # Imprimiendo el maximo valor de sens_dir_b
# print('Este es el maximo valor de sens_dir_b')
# bd = c.fetchone()
# # este es bd
# print("asi queda " , bd)

# #### Leyendo la BD para colocar los turnos ##############
# # reglas
# # para sens dir b  sen3 siempre obtendra el maximo nume
# ron_b[2] = bd[0]
# # para sen d



# Guardando los registros
conexion.commit()
# cerrando conexiones
conexion.close()


# ###pero como leer los datos????
# # solo obtendria nulo en los datos que no han sido introducidos
# # por lo que tendria que hacer algo asi como una funcion que diga:
# # pero el rellenador de datos incluso deberia ir incluso mas lejos y leer los datos
# # de base de datos hasta que en todos los datos sean diferente de NULO
# ###########################################################################
# # obtener datos sobre la tabla es decir necesito saber el ultimo numero introducido a la tabla
# #   Cuantas entradas tiene la tabla y cual es el valor de num en la ultima entradaT
#     # if NUll = 0




# # # insertando primer tiempo sensor2
# # # aqui tendria que formular nuevas reglas para hacer que los datos obtenidos de
# # # request sea correctos en plan si hora de sen_2 es anterior que sen_1 marcar error
# # # o ni si quiera aceptarla hasta obtener una hora mas tarde
# # # ademas de que cada vez que se registre un  request post tendra una variable
# # # por cada sensor que se dedicara a contar las veces que ha sido activado dicho sensor
# # # y tal vez ahi mismo se debe tener existir las reglas como la anterior y una vez que
# # # los datos obtenidos esten 'limpios' se pueden agregar a la bd
# # # Limpiando los datos
# # # - antes de subirlos a la bd
# # # sensor2 no puede ser activado antes que sensor1 y asi sucesivamente con cada numero
# # # - Despues de subirlos a la bd
# # # los datos obtenidos de un solo sensor se deben comparar entre si y encotrar un punto medio
# # #           es decir si casi todos los datos de la muestra estan cerca de '10' desechar los datos con
# # #           numeros menores o mayores en un rago de 5 < 10 y 10 > 15 para mantener limpia la base de datos
# # #           y lograr un promedio 'real'


# # CREATE TABLE 'table' ('num' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'sen1' DATETIME, 'sen2' DATETIME, 'sen3' DATETIME)


### seleccionando una sola columna ####
# c.execute("SELECT sen1_a FROM dir_a")
# bd = c.fetchall()
# print('asi quedo BD 1', bd)

# c.execute("SELECT sen2_a FROM dir_a")
# bd = c.fetchall()
# print('asi quedo BD 2 ', bd)

# c.execute("SELECT sen3_a FROM dir_a")
# bd = c.fetchall()
# print('asi quedo BD 3', bd)
