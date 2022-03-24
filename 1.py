class Libro:
    def __init__(self, titulo, genero, num_paginas, autor):
        self.titulo = titulo
        self.genero = genero
        self.num_paginas = num_paginas
        self.autor = autor
    
    #Funciones para devolver las variables
    def getTitulo(self):
        return self.titulo
    def getGenero(self):
        return self.genero
    def getNumPaginas(self):
        return self.num_paginas
    def getAutor(self):
        return self.autor

    #Para poner valores a las variables, aunque en este caso no hace falta
    def setTituo(self, titulo):
        self.titulo = titulo
    #El resto con todas igual
