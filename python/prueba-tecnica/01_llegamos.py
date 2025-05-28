#lissett fuentes
#30-04-2025

respuesta = input("¿ya llegamos?")

while respuesta.lower() != "si":
    if respuesta.lower() == "falta una hora mas":
        print("¿Ya llegamos? Falta una hora mas.")
    elif respuesta.lower() == "casi llegamos":
        print("¿Ya llegamos? Casi llegamos.")
    elif respuesta.lower() == "no me hagas detener el auto":
        print("¿Ya llegamos? No me hagas detener el auto.")
    else:
        print("¿Ya llegamos?")
    respuesta = input("¿ya llegamos?")