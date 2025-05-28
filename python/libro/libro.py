#lissett fuentes
#26-05-2025

class libro:

    def __init__(self, titulo, autor, paginas, genero, copias_disponible):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
        self.copias_disponible = copias_disponible

    def artributos (self):
        print(self.titulo, ":", sep="")
        print("*autor:", self.autor)
        print("*paginas:", self.paginas)
        print("*genero:", self.genero)
        print("*copias disponibles", self.copias_disponible)

mi_libro = libro("principito","antonie de saint-exupéry", 154, "cuento", 10 )
mi_libro.titulo = "principito"
mi_libro.autor = "antonie de saint-exupéry"

print(mi_libro)
print("el titulo del libro es:", mi_libro.titulo)
print("el autor del libro es:", mi_libro.autor)

