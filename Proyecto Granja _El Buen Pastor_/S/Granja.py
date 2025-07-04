from typing import List, Dict, Optional
from A.Animal import Animal
from I.Corral import Corral
from P.Empleado import Empleado
from R.Alimento import Alimento
from R.Vacuna import Vacuna

class Granja:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._empleados: List[Empleado] = []
        self._corrales: List[Corral] = []
        self._animales: List[Animal] = []
        self._alimentos: List[Alimento] = []
        self._vacunas: List[Vacuna] = []

    def agregar_empleado(self, empleado: Empleado):
        self._empleados.append(empleado)

    def agregar_corral(self, corral: Corral):
        self._corrales.append(corral)

    def agregar_animal(self, animal: Animal, corral_id: Optional[str] = None):
        self._animales.append(animal)
        if corral_id:
            corral = next((c for c in self._corrales if c._id_corral == corral_id), None)
            if corral:
                corral.asignar_animal(animal)
            else:
                raise ValueError("Corral no encontrado")

    def agregar_alimento(self, alimento: Alimento):
        self._alimentos.append(alimento)

    def agregar_vacuna(self, vacuna: Vacuna):
        self._vacunas.append(vacuna)

    def buscar_animal(self, animal_id: str) -> Optional[Animal]:
        return next((a for a in self._animales if a.id_animal == animal_id), None)

    def buscar_corral(self, corral_id: str) -> Optional[Corral]:
        return next((c for c in self._corrales if c._id_corral == corral_id), None)

    def buscar_empleado(self, empleado_id: str) -> Optional[Empleado]:
        return next((e for e in self._empleados if e._id_empleado == empleado_id), None)

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def empleados(self) -> List[Empleado]:
        return self._empleados.copy()

    @property
    def corrales(self) -> List[Corral]:
        return self._corrales.copy()

    @property
    def animales(self) -> List[Animal]:
        return self._animales.copy()