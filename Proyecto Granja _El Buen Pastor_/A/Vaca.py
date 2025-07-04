from A.Animal import Animal
from R.Alimento import Alimento
from R.Vacuna import Vacuna

class Vaca(Animal):
    def __init__(self, id_animal: str, edad: int, peso: float):
        super().__init__(id_animal, edad, peso)
        self._produccion_leche = 0.0

    def alimentar(self, alimento: Alimento):
        if alimento.tipo != "Forraje":
            print(f"Alerta: La vaca {self.id_animal} no debería comer {alimento.tipo}")
        self._produccion_leche += 0.5

    def vacunar(self, vacuna: Vacuna):
        self._vacunas.append(vacuna)

    def ordeñar(self) -> float:
        produccion = self._produccion_leche
        self._produccion_leche = 0.0
        return produccion

    @property
    def produccion_leche(self) -> float:
        return self._produccion_leche