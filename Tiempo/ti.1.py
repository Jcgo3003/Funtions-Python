import time
from datetime import datetime, timedelta
import datetime as dt

FMT = '%H:%M:%S'

#### Tiempo promedio que vendra empaquetado en segundos ####
d = int(round(349.75)) # debe ser redondeado
print("Promedio redondeado", d)

# Conversion a tiempo en h,m,s en datetime formato
t1 = dt.timedelta(seconds = d)
print("Tiempo 2", t1)

# Tiempo NOW en datetime formato
t2 = dt.datetime.now()
print("Hora local es ", t2)

# Suma de esos tiempo para crear TIEMPO ESPERADO
tfinal = t1 + t2
print("Suma",tfinal)


# Conversion de TIEMPO ESPERADO a formato STR de nuevo
strg = tfinal.strftime('%H:%M:%S')
print(strg)

### Para evaluar el tiempo que realmente paso ####
tiempo_esperado = strg
tiempo_now = datetime.now().strftime("%H:%M:%S")
print("Tiempo ahora final", tiempo_now)

# Evalaucion de tiempos 
tdel = datetime.strptime(tiempo_now, FMT) - datetime.strptime(tiempo_esperado, FMT)
t_float = tdel.total_seconds()
print(t_float)






# conclusion
# para transformar de los segundos a int
# t = int(round(349.75))
# >>>> 350
# para transformar de segundos a formato tiempo
# d = timedelta(seconds= t)
# >>>> 0:05:50
#  FORMATO STR        hora_now = (time.strftime('%H:%M:%S',time.localtime()))
