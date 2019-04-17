import time
from datetime import datetime, timedelta
import datetime as dt

prom = 30

# asi se obtendra el tiempo de la bd
tiempo  = '22:28:33'

# Convirtiendo eso en datatime.datatime
t_leida = datetime.strptime( tiempo , '%H:%M:%S')



# sumando promedio en segundos
#Tiempo promedio en segundos
t_pro_s = int(prom)

# Conversion a tiempo en h,m,s en datetime formato
t_pro_f = dt.timedelta(seconds = t_pro_s)

t_final = t_leida + t_pro_f

print('Tiempo final esperado es', t_final)

t_ya =  dt.datetime.now()
print('El otro tiempo', t_ya)




