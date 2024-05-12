class Enemigo:
    ## CONSTRUCTOR
    def __init__(self,nombre,):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
    ## Función que añade un digipymon a la lista del enemigo
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1
    
    