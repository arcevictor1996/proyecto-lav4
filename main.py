from src.utils.utils import limpiar_pantalla
from src.alumnos.menu_alumnos import menu_alumnos
from src.instructores.menu_instructores import menu_instructores
from src.cursos.menu_cursos import menu_cursos


def mostrar_titulo():
    print("\033[1;36m" + "=" * 30)
    print("     Sistema de Gestión".center(30))
    print("=" * 30 + "\033[0m")


def menu_principal():
    while True:
        mostrar_titulo()
        print("\n\033[1;32m-- Menú Principal --\033[0m")
        print("1. Gestionar Alumnos")
        print("2. Gestionar Instructores")
        print("3. Gestionar Cursos")
        print("4. Salir")
        print("\033[1;36m" + "-" * 30 + "\033[0m")
        opcion = input("\033[1;33mSeleccione una opción: \033[0m").strip()

        if opcion == "1":
            print("\033[1;34mRedirigiendo a la gestión de Alumnos...\033[0m")
            menu_alumnos()
            limpiar_pantalla()  # Limpia la pantalla después de salir del menú de alumnos
        elif opcion == "2":
            print("\033[1;34mRedirigiendo a la gestión de Instructores...\033[0m")
            menu_instructores()
            limpiar_pantalla()  # Limpia la pantalla después de salir del menú de instructores
        elif opcion == "3":
            print("\033[1;34mRedirigiendo a la gestión de Cursos...\033[0m")
            menu_cursos()
            limpiar_pantalla()  # Limpia la pantalla después de salir del menú de cursos
        elif opcion == "4":
            confirmar = (
                input("\033[1;31m¿Está seguro de que desea salir? (s/n): \033[0m")
                .strip()
                .lower()
            )
            if confirmar == "s":
                print("\033[1;31mSaliendo del sistema...\033[0m")
                break
            else:
                print("\033[1;32mRegresando al menú principal...\033[0m")
        else:
            print("\033[1;31mOpción no válida. Por favor, intente de nuevo.\033[0m")


if __name__ == "__main__":
    menu_principal()
