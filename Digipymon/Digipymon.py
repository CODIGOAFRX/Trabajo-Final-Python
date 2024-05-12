class Digipymon:
## CONSTRUCTOR
    def __init__(self, nombre, vida, ataque, tipo, nivel):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel
## MÉTODO TOSTRING
    def __str__(self):
        return f"Nombre: {self.nombre}, vida: {self.vida}, ataque: {self.ataque}, tipo: {self.tipo}, nivel: {self.nivel}"