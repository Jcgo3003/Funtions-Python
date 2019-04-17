import time
from datetime import datetime, timedelta
import datetime as dt

# Variables
FMT = '%H:%M:%S'

# Para guardar el tiempo promedio
t_pro_f = 0
# segundos
t_pro_s = 0

# Modulo 1 TIEMPO ESPERADO por primera vez
print("Modulo 1 ")

#### Tiempo promedio en segundos ####
t_pro_s = int(round(349.75)) # debe ser redondeado

# Conversion a tiempo en h,m,s en datetime formato
t_pro_f = dt.timedelta(seconds = t_pro_s)

# Introduccion de tiempo NOW en datetime
t_now = dt.datetime.now()

# Suma de esos tiempos para crear TIEMPO ESPERADO
t_esp = t_pro_f + t_now
print("Tiempo esperado 1 ",t_esp)


# Modulo 2 creacion de TIEMPO ESPERADO segunda vez
print()
print("Modulo 2 ")
# Hora Now
t_now = dt.datetime.now()

# Evaluando
# Conversion de TIEMPO ESPERADO a formato STR de nuevo para que pueda ser evaluado
t_esp_str = t_esp.strftime('%H:%M:%S')
t_now_str = t_now.strftime('%H:%M:%S')

# Resta
tdel = datetime.strptime(t_now_str, FMT) - datetime.strptime(t_esp_str, FMT)
t_int = int(round(tdel.total_seconds()))

print("Valor de evaluacion datetime", tdel)
print("Valor de evaluacion float", t_int)
####### Evaluando el tiempo esperado con los ifs

# Suma de esos tiempos para crear TIEMPO ESPERADO 2
t_esp = t_pro_f + t_now
print("Tiempo esperado 2 ",t_esp)

# conclusion
# Los tiempo esperados se guardaran datetime formato
# Tiempo promedio se guarda en datetime y no se modifica
# Se hace una conversion a str para hacer la resta, pero nada mas
# Para evaluar se hace una conversion a float pero lo pasaremos a int