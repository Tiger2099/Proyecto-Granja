from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):
    def __init__(self, id_animal: str, edad: int, peso: float):
        self.__id_animal = id_animal
        self.__edad = edad
        self.__peso = peso
        self.__vacunas: List["Vacuna"] = []

    @abstractmethod
    def alimentar(self, alimento: 'Alimento'):
        pass

    @abstractmethod
    def vacunar(self, vacuna: 'Vacuna'):
        pass

    def registrar_peso(self, nuevo_peso: float):
        if nuevo_peso <= 0:
            raise ValueError("El peso debe ser un valor positivo")
        self.__peso = nuevo_peso

    @property
    def id_animal(self) -> str:
        return self.__id_animal

    @property
    def edad(self) -> int:
        return self.__edad

    @property
    def peso(self) -> float:
        return self.__peso

    @property
    def vacunas(self) -> List["Vacuna"]:
        return self.__vacunas.copy()