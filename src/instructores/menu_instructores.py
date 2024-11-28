# Se importan las funciones necesarias para manejar las operaciones CRUD de instructores
from .crud_instructores import (
    crear_instructor,  # Función para crear un nuevo instructor en la base de datos
    leer_instructores,  # Función para mostrar los instructores existentes
    actualizar_instructor,  # Función para actualizar la información de un instructor
    eliminar_instructor,  # Función para eliminar un instructor de la base de datos
)

# Se importan funciones adicionales para la utilidad de la interfaz de usuario
from src.utils.utils import (
    limpiar_pantalla,
    error_rojo,
)  # Funciones para limpiar la pantalla y mostrar mensajes de error


# Función para mostrar el menú de opciones relacionadas con los instructores
def mostrar_menu_instructores():
    # Imprime un encabezado en color cian con un borde de 30 caracteres
    print("\033[1;36m" + "=" * 30)  # Borde superior en color cian
    # Centra el texto "Menú de Instructores" dentro de 30 caracteres
    print("    Menú de Instructores".center(30))  # Título centrado
    print("=" * 30 + "\033[0m")  # Borde inferior en color cian
    # Imprime las opciones del menú en color verde
    print("\n\033[1;32m-- Opciones --\033[0m")  # Título de opciones en color verde
    # Las opciones numéricas que el usuario puede seleccionar
    print("1. Crear Instructor")  # Opción 1: Crear instructor
    print("2. Leer Instructores")  # Opción 2: Mostrar la lista de instructores
    print(
        "3. Actualizar Instructor"
    )  # Opción 3: Actualizar la información de un instructor
    print("4. Eliminar Instructor")  # Opción 4: Eliminar un instructor
    print("5. Volver al Menú Principal")  # Opción 5: Volver al menú principal
    print("\033[1;36m" + "-" * 30 + "\033[0m")  # Línea divisoria en color cian


# Función que obtiene la opción seleccionada por el usuario
def obtener_opcion():
    # Bucle infinito que asegura que el usuario elija una opción válida
    while True:
        # Solicita al usuario que ingrese una opción
        opcion = input(
            "\033[1;33mSeleccione una opción: \033[0m"
        ).strip()  # Muestra el prompt en color amarillo
        # Si la opción ingresada está en el rango de opciones válidas, se retorna la opción
        if opcion in ["1", "2", "3", "4", "5"]:
            return opcion  # Devuelve la opción seleccionada
        else:
            # Si la opción no es válida, muestra un mensaje de error en color rojo
            error_rojo(
                "Opción no válida. Por favor, intente de nuevo."
            )  # Llama a la función de error_rojo


# Función principal que controla el flujo de ejecución del menú de instructores
def menu_instructores():
    # Bucle infinito que muestra el menú hasta que el usuario decida salir
    while True:
        try:
            # Muestra el menú de instructores
            mostrar_menu_instructores()  # Llama a la función para mostrar el menú

            # Obtiene la opción seleccionada por el usuario
            opcion = (
                obtener_opcion()
            )  # Llama a la función que obtiene la opción seleccionada

            # Si la opción es 1 (crear instructor)
            if opcion == "1":
                print(
                    "\033[1;34mCreando un nuevo Instructor...\033[0m"
                )  # Muestra un mensaje informativo en color azul
                crear_instructor()  # Llama a la función para crear un instructor
            # Si la opción es 2 (mostrar instructores)
            elif opcion == "2":
                print(
                    "\033[1;34mMostrando la lista de Instructores...\033[0m"
                )  # Muestra un mensaje informativo en color azul
                leer_instructores()  # Llama a la función para leer y mostrar los instructores existentes
            # Si la opción es 3 (actualizar instructor)
            elif opcion == "3":
                print(
                    "\033[1;34mActualizando un Instructor...\033[0m"
                )  # Muestra un mensaje informativo en color azul
                actualizar_instructor()  # Llama a la función para actualizar los datos de un instructor
            # Si la opción es 4 (eliminar instructor)
            elif opcion == "4":
                print(
                    "\033[1;34mEliminando un Instructor...\033[0m"
                )  # Muestra un mensaje informativo en color azul
                eliminar_instructor()  # Llama a la función para eliminar un instructor
            # Si la opción es 5 (volver al menú principal)
            elif opcion == "5":
                print(
                    "\033[1;32mVolviendo al Menú Principal...\033[0m"
                )  # Muestra un mensaje en color verde
                break  # Sale del bucle y termina la ejecución del menú de instructores
        except Exception as e:
            # Si ocurre un error inesperado, muestra el mensaje de error en rojo
            error_rojo(
                f"Ocurrió un error inesperado: {e}. Verifique su conexión o los datos ingresados."  # Mensaje detallado del error
            )
    # Al salir del bucle (cuando el usuario decide volver al menú principal), se limpia la pantalla
    limpiar_pantalla()  # Llama a la función que limpia la pantalla de la terminal
