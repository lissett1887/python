#lissett fuentes
#28-04-2025

#mostar un elemento de una lista por su posicio´n, manejando si la posicio´n no existe

def mostrar_elemento():
    frutas = ["manzana", "banana", "naranja", "palta"]
    try:
        indice = int(input("elige una posición (0 a 3):"))
        print("fruta elegida:", frutas[indice] )
    exept IndexError:
        print("esta posicion no existe en la lista")
    exept ValueError:
    print("debes ingresar numero")

mostrar_elemento()