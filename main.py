from src.utils.utils import limpiar_pantalla, error_rojo
from src.alumnos.menu_alumnos import menu_alumnos
from src.instructores.menu_instructores import menu_instructores
from src.cursos.menu_cursos import menu_cursos


# Función para mostrar el título estilizado del sistema
def mostrar_titulo():
    print("\033[1;36m" + "=" * 30)  # Línea superior en color cian
    print("     Sistema de Gestión".center(30))  # Título centrado
    print("=" * 30 + "\033[0m")  # Línea inferior en color cian


# Función que muestra el menú principal y gestiona las opciones del usuario
def menu_principal():
    while True:  # Bucle infinito hasta que el usuario decida salir
        mostrar_titulo()  # Llama a la función mostrar_titulo para imprimir el encabezado
        print(
            "\n\033[1;32m-- Menú Principal --\033[0m"
        )  # Imprime el título del menú en verde
        print("1. Gestionar Alumnos")  # Opción para gestionar alumnos
        print("2. Gestionar Instructores")  # Opción para gestionar instructores
        print("3. Gestionar Cursos")  # Opción para gestionar cursos
        print("4. Salir")  # Opción para salir del sistema
        print("\033[1;36m" + "-" * 30 + "\033[0m")  # Línea divisoria en color cian
        opcion = input(
            "\033[1;33mSeleccione una opción: \033[0m"
        ).strip()  # Captura la opción del usuario

        # Redirige según la opción seleccionada
        if opcion == "1":
            print(
                "\033[1;34mRedirigiendo a la gestión de Alumnos...\033[0m"
            )  # Mensaje en azul
            menu_alumnos()  # Llama al menú de alumnos
            limpiar_pantalla()  # Limpia la pantalla después de salir del menú de alumnos
        elif opcion == "2":
            print(
                "\033[1;34mRedirigiendo a la gestión de Instructores...\033[0m"
            )  # Mensaje en azul
            menu_instructores()  # Llama al menú de instructores
            limpiar_pantalla()  # Limpia la pantalla después de salir del menú de instructores
        elif opcion == "3":
            print(
                "\033[1;34mRedirigiendo a la gestión de Cursos...\033[0m"
            )  # Mensaje en azul
            menu_cursos()  # Llama al menú de cursos
            limpiar_pantalla()  # Limpia la pantalla después de salir del menú de cursos
        elif opcion == "4":
            # Confirma si el usuario realmente desea salir
            confirmar = (
                input("\033[1;31m¿Está seguro de que desea salir? (s/n): \033[0m")
                .strip()  # Elimina espacios antes y después de la entrada
                .lower()  # Convierte la entrada a minúsculas
            )
            if confirmar == "s":  # Si la respuesta es 's', sale del sistema
                print("\033[1;31mSaliendo del sistema...\033[0m")  # Mensaje en rojo
                break  # Termina el bucle y sale
            elif confirmar == "n": # Si la respuesta no es 's', regresa al menú principal
                print(
                    "\033[1;32mRegresando al menú principal...\033[0m"
                )  # Mensaje en verde
            else:
                error_rojo("Ingrese s o n")    
        else:
            # Si la opción no es válida, muestra un mensaje de error
            print(
                "\033[1;31mOpción no válida. Por favor, intente de nuevo.\033[0m"
            )  # Mensaje en rojo


# Inicia la ejecución del programa llamando al menú principal
if __name__ == "__main__":
    menu_principal()  # Llama a la función menu_principal para comenzar la ejecución
