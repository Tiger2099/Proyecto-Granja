from A.Animal import Animal
from R.Alimento import Alimento
from R.Vacuna import Vacuna

class Cerdo(Animal):
    def __init__(self, id_animal: str, edad: int, peso: float):
        super().__init__(id_animal, edad, peso)
        self._grasa_corporal = 10.0

    def alimentar(self, alimento: Alimento):
        self._grasa_corporal += 0.1 if alimento.tipo == "Engorde" else 0.05

    def vacunar(self, vacuna: Vacuna):
        self._vacunas.append(vacuna)

    def control_peso(self):
        if self._grasa_corporal > 25.0:
            print(f"Alerta: Cerdo {self.id_animal} con exceso de grasa ({self._grasa_corporal}%)")

    @property
    def grasa_corporal(self) -> float:
        return self._grasa_corporal