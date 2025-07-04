from datetime import date

class Alimento:
    def __init__(self, tipo: str, cantidad: float, fecha_caducidad: date):
        self._tipo = tipo
        self._cantidad = cantidad
        self._fecha_caducidad = fecha_caducidad

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def cantidad(self) -> float:
        return self._cantidad

    @property
    def fecha_caducidad(self) -> date:
        return self._fecha_caducidad