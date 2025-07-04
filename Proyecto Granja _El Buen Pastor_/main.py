from datetime import date
from A.Vaca import Vaca
from A.Cerdo import Cerdo
from R.Alimento import Alimento
from R.Vacuna import Vacuna
from I.Corral import Corral
from P.Empleado_sanitario import EmpleadoSanitario
from P.Empleado_limpieza import EmpleadoLimpieza
from P.Empleado_alimentacion import EmpleadoAlimentacion
from P.Administrador import Administrador
from S.Granja import Granja

def main():
    # Crear la granja
    granja = Granja("El Buen Pastor")

    # Crear corrales
    corral_vacas = Corral("C1", 10)
    corral_cerdos = Corral("C2", 5)
    granja.agregar_corral(corral_vacas)
    granja.agregar_corral(corral_cerdos)

    # Crear animales
    vaca1 = Vaca("V001", 3, 450)
    cerdo1 = Cerdo("C001", 1, 120)
    granja.agregar_animal(vaca1, "C1")
    granja.agregar_animal(cerdo1, "C2")

    # Crear empleados
    sanitario = EmpleadoSanitario("E001", "Juan Pérez", "Bovinos")
    limpiador = EmpleadoLimpieza("E002", "María Gómez", "Corrales")
    alimentador = EmpleadoAlimentacion("E003", "Pedro Ramírez", "Forraje")
    admin = Administrador("E004", "Carlos López")
    
    granja.agregar_empleado(sanitario)
    granja.agregar_empleado(limpiador)
    granja.agregar_empleado(alimentador)
    granja.agregar_empleado(admin)

    # Crear recursos
    vacuna1 = Vacuna("Antibacterial", 5.0, date(2023, 10, 15))
    alimento_vaca = Alimento("Forraje", 100.0, date(2023, 12, 31))
    alimento_cerdo = Alimento("Engorde", 50.0, date(2023, 12, 31))

    # Operaciones
    sanitario.aplicar_vacuna(vaca1, vacuna1)
    limpiador.limpiar_corral(corral_vacas)
    alimentador.alimentar_animal(vaca1, alimento_vaca)

    # Administrador genera reporte
    reporte_corrales = admin.supervisar_corrales(granja.corrales)
    reporte = admin.generar_reporte("Supervisión Corrales", reporte_corrales)
    print(reporte.generar())

    # Polimorfismo
    for empleado in granja.empleados:
        empleado.realizar_tarea()
        empleado.registrar_asistencia()

if __name__ == "__main__":
    main()