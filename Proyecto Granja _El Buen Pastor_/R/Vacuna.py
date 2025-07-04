from datetime import date

class Vacuna:
    def __init__(self, nombre: str, dosis: float, fecha_aplicacion: date):
        self._nombre = nombre
        self._dosis = dosis
        self._fecha_aplicacion = fecha_aplicacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def dosis(self) -> float:
        return self._dosis

    @property
    def fecha_aplicacion(self) -> date:
        return self._fecha_aplicacion