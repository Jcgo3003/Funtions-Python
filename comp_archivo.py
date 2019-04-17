import time
import os.path

nombrebd = time.strftime('%d%m%y_%H%M%S',time.localtime()) + ".db"
#dir = "sqlite:///" + nombrebd
print(nombrebd)

if (os.path.isfile(nombrebd) ):
    print("base existe")
else:
    print("base no existe")