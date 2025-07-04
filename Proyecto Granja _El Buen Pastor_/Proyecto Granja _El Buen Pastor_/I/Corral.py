from typing import List, Optional
from A.Animal import Animal

class Corral:
    def __init__(self, id_corral: str, capacidad: int):
        self._id_corral = id_corral
        self._capacidad = capacidad
        self._estado = "Limpio"
        self._animales: List[Animal] = []

    def asignar_animal(self, animal: Animal):
        if len(self._animales) >= self._capacidad:
            raise ValueError("Corral a capacidad máxima")
        self._animales.append(animal)

    def retirar_animal(self, animal_id: str) -> Optional[Animal]:
        for i, animal in enumerate(self._animales):
            if animal.id_animal == animal_id:
                return self._animales.pop(i)
        return None

    def limpiar(self):
        self._estado = "Limpio"

    def verificar_estado(self) -> str:
        return self._estado

    @property
    def animales(self) -> List[Animal]:
        return self._animales.copy()

    @property
    def capacidad(self) -> int:
        return self._capacidad

    @property
    def estado(self) -> str:
        return self._estado