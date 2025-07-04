from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, id_empleado: str, nombre: str, cargo: str):
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._cargo = cargo

    @abstractmethod
    def realizar_tarea(self):
        pass

    def registrar_asistencia(self):
        print(f"{self._nombre} registró su asistencia")

    def reportar_incidencia(self, descripcion: str):
        print(f"Incidencia reportada por {self._nombre}: {descripcion}")

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cargo(self) -> str:
        return self._cargo