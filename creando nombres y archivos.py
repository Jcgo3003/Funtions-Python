from cs50 import SQL
import sqlite3
import time

# Obteniedo dia + '.db '
nombrebd = time.strftime('%d%m%y_%H%M%S',time.localtime()) + ".db"
# Creando BD
conn= sqlite3.connect(nombrebd)
print ("Base de datos creada con el nombre", nombrebd)




# Estudios de la libreria 'time'
# maneras distintas de obtener tiempo y presentarlo revisar la libreria time
# dia2 = time.strftime('%d' '%m' '%y' '%H' '%M' '%S' , time.gmtime())
# dia3 = time.asctime(time.gmtime(1))
# dia4 = time.asctime(time.localtime(2))
