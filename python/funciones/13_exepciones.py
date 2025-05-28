#lissett fuentes
#28-04-2025

#ejercicio 1 conversión segura a nu´mero

#objetivo: pedir un numero al usuario y evitar errores si escribe letras.

def pedir_numero ():
    try: 
        numero = int(input("escribe un numero entero:"))
        print ("!gracias¡ tu numero es:" numero)
    exept ValueError:
        print("eso no es un numero valido. intenta otra vez.")

pedir_numero()