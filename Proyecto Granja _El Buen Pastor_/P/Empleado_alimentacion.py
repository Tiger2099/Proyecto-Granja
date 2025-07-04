from P.Empleado import Empleado
from A.Animal import Animal
from R.Alimento import Alimento

class EmpleadoAlimentacion(Empleado):
    def __init__(self, id_empleado: str, nombre: str, tipo_alimento: str):
        super().__init__(id_empleado, nombre, "Alimentación")
        self._tipo_alimento = tipo_alimento

    def realizar_tarea(self):
        print(f"{self.nombre} distribuye {self.tipo_alimento}")

    def alimentar_animal(self, animal: Animal, alimento: Alimento):
        animal.alimentar(alimento)
        print(f"{animal.id_animal} alimentado con {alimento.tipo}")

    @property
    def tipo_alimento(self) -> str:
        return self._tipo_alimento