#lissett fuentes
#28-04-2025

#objetivo: acceder a un valor en un diccionario sin que se rompa el programasi la clave no existe

def buscar_cantante={
    "nombre": "luis miguel"
    "pais" : "puerto rico"
}
try:
    clave = input(¿que quieres saber? (nombre o pais))
    print("resultado:", canatante[clave])
exept KeyError:
    print("esta clave no existe")


buscar_cantante()