# mucho cuidado con las librerias 'datetime' e import 'datetime' ocacionan muchos problemas al usarse juntas
import datetime
from datetime import datetime, date
import time


t = datetime.datetime.now() - datetime.timedelta(hours=2, minutes=10)

datetime.datetime(2012, 12, 26, 17, 18, 52, 167840)
print(t)


# Parsing times into timeobjects
hora = '12:20:10'
my_hora = datetime.time(*[int(i) for i in hora.split(":")])

# restando horas
hora_final = my_hora - datetime.timedelta(12,20,10)

# imprimiendo datos
print("momento", momento)
print("my_date", my_date)
print("hora", hora)
print("My_hora", my_hora)

print("hora final", hora_final )

t = datetime.time(1, 2, 10)
dt = datetime.datetime.combine(datetime.date.today(), t)
print(dt)
datetime.datetime(2012, 12, 26, 1, 2)
dt -= datetime.timedelta(hours=5)
dt.time()
datetime.time(20, 2)
print(dt)

# Parsing the time
# hora = '00:10:10' # 12:10
# t2 = datetime.time(*[int(i) for i in hora.split(":")])

# t1 = datetime.time(23, 55, 0) #11:55 pm

# # operacion de resta
# delta = (t2.hour - t1.hour)*60 + t2.minute - t1.minute + (t2.second - t1.second)/60.0
# delta = 24*60 - delta

# d1 = (t2.hour - t1.hour)*60
# d2 = t2.minute - t1.minute
# d3 = (t2.second - t1.second)/60.0

# print (d1)
# print (d2)
# print (d3)
# print( delta)

# t = datetime.now()
# print(t)

# t1 = datetime.time(3, 2, 1)
# td = t1 - datetime.timedelta(hours=2, minutes=10)
# t2 = datetime.time(3, 2, 1)


# t = datetime.datetime.now() - datetime.timedelta(hours=2, minutes=10)
# print( t)

# import datetime
# import time

# t1 = datetime.time(00, 10, )
# print ('\tt1:', t1 )
# t2 = datetime.time(23, 55, )
# print ('\tt2:', t2 )
# print ('\tt1 > t2:', t1 > t2 )


# Parsing the time
hora = '00:10:10' # 12:10
t2 = datetime.time(*[int(i) for i in hora.split(":")])
hora = '00:20:10' # 12:10
t1 = datetime.time(*[int(i) for i in hora.split(":")])

datetime.combine(date.today(), t1) - datetime.combine(date.today(), t2)