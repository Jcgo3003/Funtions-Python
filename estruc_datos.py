# Ejemplo de estructuras de datos

# tuplas - Inmutables
t=(25, "Mayo", 1810)
print('Tuplas')
print("t = ", t)
# t no soporta que se le asignen nuevos valores
# t[1] = bla
print("t1 = ", t[0])

# Listas si se pueden modificar
l =[78455, 89211, 66540, 45750]
print("Listas")
print('L = ', l)
print('l1 = ', l[0])
l[0] = 1
print("L despues de asignacion ", l)

# haciendo un experimento con listas y for
# donde turno [0], turno [1], etc... representa cada sensor
turnos  = [0, 0, 0, 0]

for i in range (1, 10):
    turnos[0] = i
    print(turnos)
    turnos[1] = i
    print(turnos)
    turnos[2] = i
    print(turnos)
    turnos[3] = i
    print(turnos)

## Ahora necesito agregar algo que de el warning de por ejemplo el numero t[0] es menor que t[1]
# es decir sensor 2 se activo y este va un numero arriva que el sensor anterior  es decir algo extrano paso
# como para manda llamar un erro o algo asi
# seria exactamente de esta manera
#   if  sen2 == True
##       #agregar a su lista de turnos  +1
        # comparar ese numero con sen1 s
        #if sen1 < menor que sen2
            # mostrar que hay un problema, no guardar ese numero
        # guardar tiempo en la bd







