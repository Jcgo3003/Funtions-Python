from datetime import datetime, timedelta

FMT = '%H:%M:%S'

# tiempos en 'str'
s1 = '19:39:45'
s2 = '20:27:13' # for example

tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
t_float = tdelta.total_seconds()
print('tiempo en minutos',tdelta)
print('tiempo en segundos', t_float)