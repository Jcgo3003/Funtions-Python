from datetime import datetime, timedelta

# tiempos en 'str'
s1 = '10:33:26'
s2 = '23:58:00' # for example
s3 = '00:05:00'
FMT = '%H:%M:%S'

# Resta de tiempos
tdelta = datetime.strptime(s3, FMT) - datetime.strptime(s2, FMT)

# En caso de que alla cambio de dia ejem... '00:05:00' - '23:58:00'/ de otra manera imp -1 day, 0:07:00
if tdelta.days < 0:
    # corrigiendo el error
    tdelta = timedelta(days=0, seconds=tdelta.seconds, microseconds = tdelta.microseconds)

print(tdelta)

# Codigo obtenido de:
#
# https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
# response by 'David Z'