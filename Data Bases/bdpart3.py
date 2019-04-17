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

    ### Recuperando datos de la DB  para la vuelta  direccion A #####
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


###############################################################################
########################### Sensores direcion A ###############################


res = 'y'
while ( res == 'y'):
    print('Las vueltas comienzan asi A', ron_a)
    print('Las vueltas comienzan asi B', ron_b)
    print("    Menu principal   ")
    ## aqui obtengo el nombre del sensor ejem... sen1_a
    dir = input("Direccion: ")
    sensor = input("Sensor numero: ")# ejem... sen1_a
    num_sen = int(input("Numero: "))
    print("...")


# for n in sensor:
#     if n.isdigit():
#         num_sen = n




    if ( dir == 'a'):
        if (num_sen == 1 ):
            print("Guardando sen1 Direccion A")
            # Insertando tiempos a sen1
            ron_a[0] += 1
            hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
            c.execute('''INSERT INTO a ("num_a","sen1_a","sen2_a","sen3_a") VALUES ( ? , ? ,NULL,NULL)''', (ron_a[0], hora_now) )


        else:
            print("Guardando sen", num_sen)
            print("Direccion A")
            # para que las rondas se guarden correctamente
            num_sen -= 1
            ron_a[num_sen] += 1

            hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
            c.execute('''UPDATE a SET {} = ? where num_a = ? '''.format( sensor), (hora_now, ron_a[num_sen] ) )



    else:
        if (num_sen == 3 ):
            print("Guardando sen3 Direccion B ")
            # Insertando tiempos a sen3
            ron_b[2] += 1
            hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
            c.execute('''INSERT INTO b ("num_b","sen3_b","sen2_b","sen1_b") VALUES ( ? , ? ,NULL,NULL)''', (ron_b[2], hora_now) )
        else:
            print("Guardando sen", num_sen)
            print("Direccion B")

            # para que las rondas se guarden correctamente
            num_sen -= 1

            ron_b[num_sen] += 1
            hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
            c.execute('''UPDATE b SET {} = ? where num_b = ? '''.format(sensor), (hora_now, ron_b[num_sen] ) )


    # Guardando los registros
    conexion.commit()

    res = input("Quieres continuar: ")

print('Las vueltas terminan asi A', ron_a)
print('Las vueltas terminan asi B', ron_b)
# cerrando conexiones
conexion.close()

# # insertando datos para sensor 2 y 3 a #######
# ron_a[1] += 1
# c.execute('''UPDATE "dir_a" SET "sen2_a" = '12:05:06' where num_a = ?''', (ron_a[1], ))
# ron_a[2] += 1
# c.execute('''UPDATE "dir_a" SET "sen3_a" = '12:10:06' where num_a = ?''', (ron_a[2], ))


# ########### aqui terminia una vuelta ##############
# ############## segunda vuelta ####################
# # varibles que llegaran desde el http request ESTA INSTRUCCION ES SOLO PARA SEN1
# ron_a[0] += 1
# hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
# #insertando segunda ronda tiempo sensor1
# c.execute('''INSERT INTO dir_a ("num_a","sen1_a","sen2_a","sen3_a") VALUES ( ? , ? ,NULL,NULL)''', (ron_a[0], hora_now) )

# ## sen 2
# ron_a[1] += 1
# hora_1 = (time.strftime('%H:%M:%S',time.localtime())  )
# c.execute('''UPDATE "dir_a" SET "sen2_a" = ? where num_a = ?''', (hora_1 ,ron_a[1] ) )
# ### sen 3
# ron_a[2] += 1
# hora_2 = (time.strftime('%H:%M:%S',time.localtime())  )
# c.execute('''UPDATE "dir_a" SET "sen3_a" = ? where num_a = ?''', (hora_2 ,ron_a[2] ) )



# ########### tercer vuelta queda incompleta ################
# # varibles que llegaran desde el http request ESTA INSTRUCCION ES SOLO PARA SEN1
# ron_a[0] += 1
# hora_now = (time.strftime('%H:%M:%S',time.localtime())  )
# #insertando segunda ronda tiempo sensor1
# c.execute('''INSERT INTO dir_a ("num_a","sen1_a","sen2_a","sen3_a") VALUES ( ? , ? ,NULL,NULL)''', (ron_a[0], hora_now) )

# print('asi quedo rondas', ron_a)



# ###########################   imprimiendo                  ###########################
# #### fetchall devuelve un tuple dentro de otro tuple!!!!!###
# c.execute("SELECT sen1_a FROM dir_a")
# bd = c.fetchall()
# print('asi quedo BD 1', bd)
# print('Sen1 tiene ', len(bd))

# ### para contar las entradas de las otras columnas se debe hacer un conteo uno por uno
# c.execute("SELECT sen2_a FROM dir_a")
# bd = c.fetchall()
# print()
# print('asi quedo BD 2 ', bd)
# cuenta = 0
# for i in range (len(bd)):
#     if ( str(bd[i][0]) != 'None'):
#         cuenta += 1
# print('Sen2 tiene ', cuenta)
# # guardando la vuelta en ron_a
# ron_a[1] = cuenta
# ###### Imp sen3 #######
# print()
# c.execute("SELECT sen3_a FROM dir_a")
# bd = c.fetchall()
# cuenta = 0
# for i in range (len(bd)):
#     if ( str(bd[i][0]) != 'None'):
#         cuenta += 1
# # guardando la vuelta en ron_a
# ron_a[2] = cuenta
# print('asi quedo BD 3', bd)
# print('Sen3 tiene ', cuenta)

# # impriendo la lista de vueltas
# print('las rodas quedaron asi',ron_a)


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




# Guardando los registros

