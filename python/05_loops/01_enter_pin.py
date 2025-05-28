#lissett fuentes
#27-05-2025

print ('banco del 4°B')

pin = int(input('Ingresa tu PIN:'))

while pin !=1234:
    pin = int(input('PIN incorrecto. Ingresa tu PIN nuevamente'))

if pin ==1234:
    print('!PIN aceptado')
    print('Bienvenido a tu cuenta')