#lissett fuentes
#26-05-2025

pistas = ("puerta roja",221, "londres", 3.14, "watson", 7, "moriarty")

#pregunta 1 

indice = pistas.index("puerta roja")
print(indice)

#pregunta 2
print(pistas[-1])

#pregunta 4
print("londres" in pistas)

#pregunta 5

pista1, pista2, pista3, *_= pistas
print({pista1}, {pista2}, {pista3})

#pregunta 6 

nuevas_pistas = pistas + ("union española", "colo-colo")
print(nuevas_pistas)

#pregunta 7

print(pistas.index("watson"))

#pregunta 8 

print(pistas.count(7))