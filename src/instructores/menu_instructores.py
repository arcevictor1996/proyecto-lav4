from .crud_instructores import (
    crear_instructor,
    leer_instructores,
    actualizar_instructor,
    eliminar_instructor,
)
from src.utils.utils import limpiar_pantalla, error_rojo


def mostrar_menu_instructores():
    print("\033[1;36m" + "=" * 30)
    print("    Menú de Instructores".center(30))
    print("=" * 30 + "\033[0m")
    print("\n\033[1;32m-- Opciones --\033[0m")
    print("1. Crear Instructor")
    print("2. Leer Instructores")
    print("3. Actualizar Instructor")
    print("4. Eliminar Instructor")
    print("5. Volver al Menú Principal")
    print("\033[1;36m" + "-" * 30 + "\033[0m")


def obtener_opcion():
    while True:
        opcion = input("\033[1;33mSeleccione una opción: \033[0m").strip()
        if opcion in ["1", "2", "3", "4", "5"]:
            return opcion
        else:
            error_rojo("Opción no válida. Por favor, intente de nuevo.")


def menu_instructores():
    while True:
        try:
            mostrar_menu_instructores()
            opcion = obtener_opcion()

            if opcion == "1":
                print("\033[1;34mCreando un nuevo Instructor...\033[0m")
                crear_instructor()
            elif opcion == "2":
                print("\033[1;34mMostrando la lista de Instructores...\033[0m")
                leer_instructores()
            elif opcion == "3":
                print("\033[1;34mActualizando un Instructor...\033[0m")
                actualizar_instructor()
            elif opcion == "4":
                print("\033[1;34mEliminando un Instructor...\033[0m")
                eliminar_instructor()
            elif opcion == "5":
                print("\033[1;32mVolviendo al Menú Principal...\033[0m")
                break
        except Exception as e:
            error_rojo(
                f"Ocurrió un error inesperado: {e}. Verifique su conexión o los datos ingresados."
            )
    # Limpiar la pantalla al volver al menú principal
    limpiar_pantalla()
