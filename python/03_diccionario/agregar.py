#lissett fuentes
#28-04-2025

#agregar o modificar un elemento en una lista

mi_diccionario = {
    "nombre": "lissett",
    "apellido": "fuentes",
    "edad": 17,
    "ciudad": "madrid",
    "Pais": "francia",
    "telefono": 988298769
}
#eliminar un elemento del diccionario
del mi_diccionario["edad"]

#eliminar un elemento del diccionario pop
mi_diccionario.pop("apellido")

#eliminar un elemento de el diccionario popitem
mi_diccionario.popitem()

#imprimir el diccionario atualizado
print(mi_diccionario)