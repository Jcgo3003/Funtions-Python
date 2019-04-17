import time
from datetime import datetime, timedelta
import datetime as dt

d = int(round(349.75))
print("Redondeo", d)


# d = timedelta(microseconds=1)
# print(d)
# d = timedelta(minutes=1.5)
# (d.days, d.seconds, d.microseconds)
# print(d)


t3 = timedelta(seconds = d)
print("Tiempo 3", t3)

t2 = (time.strftime('%H:%M:%S',time.localtime()))
# t2 = timedelta(seconds = 200)
print("Hora local es ", t2)

# t1 = t2 + t3
# print("T final", t1)


nextTime = dt.datetime.now() + dt.timedelta(minutes = 15)
print(nextTime)

# conclusion
# para transformar de los segundos a int
# t = int(round(349.75))
# >>>> 350
# para transformar de segundos a formato tiempo
# d = timedelta(seconds= t)
# >>>> 0:05:50