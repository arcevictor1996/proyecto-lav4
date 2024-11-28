from .crud_alumnos import (
    crear_alumno,
    leer_alumnos,
    actualizar_alumno,
    eliminar_alumno,
)

from src.utils.utils import limpiar_pantalla


def mostrar_menu_alumnos():
    print("\033[1;36m" + "=" * 30)
    print("    Menú de Alumnos".center(30))
    print("=" * 30 + "\033[0m")
    print("\n\033[1;32m-- Opciones --\033[0m")
    print("1. Crear Alumno")
    print("2. Leer Alumnos")
    print("3. Actualizar Alumno")
    print("4. Eliminar Alumno")
    print("5. Volver al Menú Principal")
    print("\033[1;36m" + "-" * 30 + "\033[0m")


def obtener_opcion():
    while True:
        opcion = input("\033[1;33mSeleccione una opción: \033[0m").strip()
        if opcion in ["1", "2", "3", "4", "5"]:
            return opcion
        else:
            print("\033[1;31mOpción no válida. Por favor, intente de nuevo.\033[0m")


def menu_alumnos():
    while True:
        mostrar_menu_alumnos()
        opcion = obtener_opcion()

        if opcion == "1":
            print("\033[1;34mCreando un nuevo Alumno...\033[0m")
            crear_alumno()
        elif opcion == "2":
            print("\033[1;34mMostrando la lista de Alumnos...\033[0m")
            leer_alumnos()
        elif opcion == "3":
            print("\033[1;34mActualizando un Alumno...\033[0m")
            actualizar_alumno()
        elif opcion == "4":
            print("\033[1;34mEliminando un Alumno...\033[0m")
            eliminar_alumno()
        elif opcion == "5":
            print("\033[1;32mVolviendo al Menú Principal...\033[0m")
            break
    # Limpiar la pantalla al volver al menú principal
    limpiar_pantalla()
