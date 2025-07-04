from A.Animal import Animal
from R.Alimento import Alimento
from R.Vacuna import Vacuna

class Gallina(Animal):
    def __init__(self, id_animal: str, edad: int, peso: float):
        super().__init__(id_animal, edad, peso)
        self._huevos = 0

    def alimentar(self, alimento: Alimento):
        if alimento.tipo == "Granos":
            self._huevos += 2
        else:
            self._huevos += 1

    def vacunar(self, vacuna: Vacuna):
        self._vacunas.append(vacuna)

    def recolectar_huevos(self) -> int:
        huevos = self._huevos
        self._huevos = 0
        return huevos

    @property
    def huevos(self) -> int:
        return self._huevos