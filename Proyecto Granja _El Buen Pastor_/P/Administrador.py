from P.Empleado import Empleado
from S.Reporte import Reporte
from I.Corral import Corral
from typing import List, Dict
from datetime import date

class Administrador(Empleado):
    def __init__(self, id_empleado: str, nombre: str):
        super().__init__(id_empleado, nombre, "Administrador")

    def realizar_tarea(self):
        print(f"{self.nombre} supervisa operaciones")

    def supervisar_corrales(self, corrales: List[Corral]) -> Dict:
        reporte = {}
        for corral in corrales:
            reporte[corral._id_corral] = {
                "animales": len(corral.animales),
                "estado": corral.estado
            }
        return reporte

    def generar_reporte(self, tipo: str, datos: Dict) -> Reporte:
        return Reporte(tipo, date.today(), datos)