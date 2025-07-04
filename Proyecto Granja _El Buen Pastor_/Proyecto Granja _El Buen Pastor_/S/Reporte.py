from datetime import date
from typing import Dict

class Reporte:
    def __init__(self, tipo: str, fecha: date, contenido: Dict):
        self._tipo = tipo
        self._fecha = fecha
        self._contenido = contenido

    def generar(self) -> str:
        return f"Reporte {self._tipo} ({self._fecha}): {self._contenido}"

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def fecha(self) -> date:
        return self._fecha

    @property
    def contenido(self) -> Dict:
        return self._contenido