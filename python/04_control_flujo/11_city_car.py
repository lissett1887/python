#lissett fuentes
#30-04-2025

altura = int(input('ingresa tu altura en cm:'))
creditos = int(input('ingresa tus creditos:'))

alrura_suficiente = altura >= 137
creditos_sufuciente = creditos >= 10

if altura_suficiente and creditos_sufucientes:
    print('puedes conducir un coche de ciudad')
elif altura_suficiente and not creditos_suficientes:
    print('puedes conducir un coche de ciudad, pero no tienes suficiente creditos')
else: 
    print('no puedes conducir un coche en la ciudad')