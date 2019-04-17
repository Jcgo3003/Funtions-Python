import time
from datetime import datetime, timedelta
import datetime as dt

# Variavles
FMT = '%H:%M:%S'

# Para guardar el tiempo promedio
t_pro_f = 0
# segundos
t_pro_s = 0

# Modulo 1 TIEMPO ESPERADO por primera vez
print("Modulo 1 ")
#### Tiempo promedio en segundos ####
t_pro_s = int(round(349.75)) # debe ser redondeado
print("Promedio redondeado", t_pro_s)

# Conversion a tiempo en h,m,s en datetime formato
t_pro_f = dt.timedelta(seconds = t_pro_s)
print("Tiempo pro en H M S formato", t_pro_f)

# Introduccion de tiempo NOW en datetime
t_now = dt.datetime.now()
print("Hora local es ", t_now)

# Suma de esos tiempos para crear TIEMPO ESPERADO
t_esp = t_pro_f + t_now
print("Tiempo esperado 1 ",t_esp)


# Modulo 2 creacion de TIEMPO ESPERADO segunda vez
print("Modulo 2 ")
# TIEMPO ESPERADO   del primer tiempo

# Hora Now
t_now = dt.datetime.now()
print("Hora local 2 es ", t_now)


# Evaluando el tiempo contra el TIEMPO ESPERADO 1
# Conversion de TIEMPO ESPERADO a formato STR de nuevo para que pueda ser evaluado
t_esp_str = t_esp.strftime('%H:%M:%S')
t_now_str = t_now.strftime('%H:%M:%S')
# Resta
tdel = datetime.strptime(t_now_str, FMT) - datetime.strptime(t_esp_str, FMT)
t_float = tdel.total_seconds()
print("Valor de evaluacion ", tdel)
print("Valor de evaluacion ", t_float)
####### Evaluando el tiempo esperado con los ifs

# Suma de esos tiempos para crear TIEMPO ESPERADO 2
t_esp = t_pro_f + t_now
print("Tiempo esperado 2 ",t_esp)




# Necesito que tiempo ahora este en datetime

# tiempo_now = datetime.now().strftime("%H:%M:%S")
# print("Tiempo ahora 2", tiempo_now)

# Creando el proximo TIEMPO ESPERADO

# conclusion
# para transformar de los segundos a int
# t = int(round(349.75))
# >>>> 350
# para transformar de segundos a formato tiempo
# d = timedelta(seconds= t)
# >>>> 0:05:50
#  FORMATO STR        hora_now = (time.strftime('%H:%M:%S',time.localtime()))
