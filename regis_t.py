import time
from datetime import datetime, timedelta

tiempo_1 = 0
tiempo_2 = 0
tiempo_3 = 0

cuenta = 0

FMT = '%H:%M:%S'

while ( cuenta < 3):
    ya = input ('Para registra el tiempo ahora presiona n')
    tiempo_1 = (time.strftime('%H:%M:%S',time.localtime()))

    cuenta += 1

    ya = input ('Para registra el tiempo ahora presiona n')
    tiempo_2 = (time.strftime('%H:%M:%S',time.localtime()))
    cuenta += 1

    ya = input ('Para registra el tiempo ahora presiona n')
    tiempo_3 = (time.strftime('%H:%M:%S',time.localtime()))
    cuenta += 1

print('Tiempo 1', tiempo_1)
print('Tiempo 2', tiempo_2)
print('Tiempo 3', tiempo_3)

tdel = datetime.strptime(tiempo_2, FMT) - datetime.strptime(tiempo_1, FMT)
print('tdel de tiempo 2 y tiempo 1 es ', tdel)
t_float = tdel.total_seconds()
print('T float es ', t_float)
tdel = datetime.strptime(tiempo_1, FMT) - datetime.strptime(tiempo_2, FMT)
print('tdel de tiempo 1 y tiempo 2 es ', tdel)
t_float = tdel.total_seconds()
print('T float es ',  t_float)

t1 = datetime.timedelta(hours=9.888888888888886)

t_del = 100.00
print('Segundos ',  t_del)
ta = tdel.total_seconds()
print('T float a str ',  ta)


# tarea 1 convertir 10 segundos a str

# suma = datetime.strptime(tiempo_1, FMT) - datetime.strptime('0:00:10', FMT)
suma = datetime.strptime(tiempo_1, FMT) + datetime.strptime(tiempo_2, FMT)
print("Tiempo 1 es ", tiempo_1)
print('Suma de tiempo 1 mas tiempo 2 es ', suma)


# t_float1 = tiempo_1.total_seconds()
# print('Tiempo 1 en segundos', tiempo_1 )
# t_float2 = tiempo_2.total_seconds()
# print('Tiempo 2 en segundos', tiempo_2)


### Este es el tipo de datos que se recibiran
# Tengo que acer que tiempo_1 se pueda tranquilamente sumar un float como ese

# Promedios finales pro_a [349.75, 347.25, 348.0]
# Promedios finales pro_b [377.5, 405.25, 361.25]
# Necesito una funcion que me deje agregarle un float a un str de hora
#   00:02:32 + 349.75  y me entrege una hora
## Estos son los tiempo antes de ser transformados en floats
# Tiempo  0:05:30
# Tiempo  0:05:55
# Tiempo  0:05:30
# Tiempo  0:06:24
# Tiempo  0:04:20
