from P.Empleado import Empleado
from I.Corral import Corral

class EmpleadoLimpieza(Empleado):
    def __init__(self, id_empleado: str, nombre: str, area_asignada: str):
        super().__init__(id_empleado, nombre, "Limpieza")
        self._area_asignada = area_asignada

    def realizar_tarea(self):
        print(f"{self.nombre} limpia el área {self.area_asignada}")

    def limpiar_corral(self, corral: Corral):
        corral.limpiar()
        print(f"Corral {corral._id_corral} limpiado")

    @property
    def area_asignada(self) -> str:
        return self._area_asignada