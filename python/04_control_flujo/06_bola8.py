#lissett fuentes
#28-04-2025

import random

pregunta = input("pregunta:")

num_ale = random.randint(1, 9)
if num_ale == 1:
    respuesta = 'si, definitivamente'
elif num_ale == 2:
    respuesta ='no, definitivamente'
elif num_ale == 3:
    respuesta ='preguntame mas tarde'
elif num_ale == 4:
    respuesta ='no cuentes con ello'
elif num_ale == 5:
    respuesta = 'si, en mi opinion, si'
elif num_ale == 6:
    respuesta = 'si, pero no lo hagas'
elif num_ale == 7:
    respuesta = 'no estoy seguro, pegúntame mas tarde'
elif num_ale == 8:
    respuesta = 'si, pero no lo creo'
else:
    respuesta = 'no, no cuentes con ello'

    print(f"respuesta = {respuesta}")