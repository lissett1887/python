#lissett fuentes
#30-04-2025

respuesta = input ("estas cansado? (si/no):").strip().lower()

cansado = respuesta =='si'

if not cansado:
    print('puedes seguir trabajando')
else:
    print('descansa un poco')