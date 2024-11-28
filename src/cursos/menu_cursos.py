from src.utils.utils import limpiar_pantalla
from .crud_cursos import (
    crear_curso,
    leer_cursos,
    actualizar_curso,
    eliminar_curso,
)


def mostrar_menu_cursos():
    print("\033[1;36m" + "=" * 30)
    print("    Menú de Cursos".center(30))
    print("=" * 30 + "\033[0m")
    print("\n\033[1;32m-- Opciones --\033[0m")
    print("1. Crear Curso")
    print("2. Leer Cursos")
    print("3. Actualizar Curso")
    print("4. Eliminar Curso")
    print("5. Volver al Menú Principal")
    print("\033[1;36m" + "-" * 30 + "\033[0m")


def obtener_opcion():
    while True:
        opcion = input("\033[1;33mSeleccione una opción: \033[0m").strip()
        if opcion in ["1", "2", "3", "4", "5"]:
            return opcion
        else:
            print("\033[1;31mOpción no válida. Por favor, intente de nuevo.\033[0m")


def menu_cursos():
    while True:
        mostrar_menu_cursos()
        opcion = obtener_opcion()

        if opcion == "1":
            print("\033[1;34mCreando un nuevo Curso...\033[0m")
            crear_curso()
        elif opcion == "2":
            print("\033[1;34mMostrando la lista de Cursos...\033[0m")
            leer_cursos()
        elif opcion == "3":
            print("\033[1;34mActualizando un Curso...\033[0m")
            actualizar_curso()
        elif opcion == "4":
            print("\033[1;34mEliminando un Curso...\033[0m")
            eliminar_curso()
        elif opcion == "5":
            print("\033[1;32mVolviendo al Menú Principal...\033[0m")
            break

    # Limpiar la pantalla al volver al menú principal
    limpiar_pantalla()
