from P.Empleado import Empleado
from A.Animal import Animal
from R.Vacuna import Vacuna
from typing import Dict

class EmpleadoSanitario(Empleado):
    def __init__(self, id_empleado: str, nombre: str, especialidad: str):
        super().__init__(id_empleado, nombre, "Sanitario")
        self._especialidad = especialidad

    def realizar_tarea(self):
        print(f"{self.nombre} realiza chequeos sanitarios")

    def aplicar_vacuna(self, animal: Animal, vacuna: Vacuna):
        animal.vacunar(vacuna)
        print(f"Vacuna {vacuna.nombre} aplicada a {animal.id_animal}")

    def realizar_chequeo(self, animal: Animal) -> Dict:
        return {
            "animal": animal.id_animal,
            "peso": animal.peso,
            "vacunas": [v.nombre for v in animal.vacunas]
        }

    @property
    def especialidad(self) -> str:
        return self._especialidad