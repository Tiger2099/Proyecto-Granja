class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f"Animal: {self.especie}, Edad: {self.edad} años"
