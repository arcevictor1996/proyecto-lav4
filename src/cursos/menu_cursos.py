# Importación de funciones necesarias desde otros módulos
from src.utils.utils import (
    limpiar_pantalla,
    error_rojo,
)  # Importa las funciones de utilidades para limpiar pantalla y mostrar errores en rojo.
from .crud_cursos import (
    crear_curso,  # Función para crear un nuevo curso.
    leer_cursos,  # Función para leer la lista de cursos.
    actualizar_curso,  # Función para actualizar un curso existente.
    eliminar_curso,  # Función para eliminar un curso existente.
)


# Función para mostrar el menú de cursos
def mostrar_menu_cursos():
    """
    Muestra el menú de opciones disponibles para gestionar los cursos.
    Cada opción se representa con un número que el usuario puede seleccionar.
    """
    print("\033[1;36m" + "=" * 30)  # Imprime una línea de separación con color cian.
    print("    Menú de Cursos".center(30))  # Imprime el título del menú centrado.
    print(
        "=" * 30 + "\033[0m"
    )  # Imprime otra línea de separación con color cian y resetea el color al final.
    print(
        "\n\033[1;32m-- Opciones --\033[0m"
    )  # Imprime un título para las opciones, en color verde.
    print("1. Crear Curso")  # Opción para crear un nuevo curso.
    print("2. Leer Cursos")  # Opción para ver la lista de cursos.
    print("3. Actualizar Curso")  # Opción para actualizar un curso.
    print("4. Eliminar Curso")  # Opción para eliminar un curso.
    print("5. Volver al Menú Principal")  # Opción para volver al menú principal.
    print(
        "\033[1;36m" + "-" * 30 + "\033[0m"
    )  # Línea de separación al final, en color cian.


# Función para obtener la opción del usuario
def obtener_opcion():
    """
    Solicita al usuario que ingrese una opción válida entre 1 y 5.
    Si el usuario ingresa una opción no válida, se muestra un mensaje de error y se vuelve a pedir la opción.
    """
    while (
        True
    ):  # Inicia un bucle infinito que solo se detendrá cuando se ingrese una opción válida.
        opcion = input(
            "\033[1;33mSeleccione una opción: \033[0m"
        ).strip()  # Solicita la opción al usuario y elimina espacios extra.
        if opcion in [
            "1",
            "2",
            "3",
            "4",
            "5",
        ]:  # Verifica si la opción ingresada es válida (de 1 a 5).
            return opcion  # Retorna la opción válida seleccionada.
        else:
            error_rojo(
                "Opción no válida. Por favor, intente de nuevo."
            )  # Si la opción no es válida, muestra un mensaje de error.


# Función principal que maneja el menú de cursos
def menu_cursos():
    """
    Muestra el menú de cursos y permite al usuario seleccionar una opción para gestionar los cursos.
    Según la opción elegida, se llama a las funciones correspondientes.
    El proceso se repite hasta que el usuario elija salir.
    """
    while (
        True
    ):  # Bucle infinito para mantener el menú activo hasta que el usuario elija salir.
        try:
            mostrar_menu_cursos()  # Muestra el menú de opciones.
            opcion = obtener_opcion()  # Obtiene la opción seleccionada por el usuario.

            if (
                opcion == "1"
            ):  # Si la opción es "1", se llama a la función para crear un curso.
                print(
                    "\033[1;34mCreando un nuevo Curso...\033[0m"
                )  # Mensaje informativo en color azul.
                crear_curso()  # Llama a la función para crear un nuevo curso.
            elif (
                opcion == "2"
            ):  # Si la opción es "2", se llama a la función para mostrar los cursos existentes.
                print(
                    "\033[1;34mMostrando la lista de Cursos...\033[0m"
                )  # Mensaje informativo en color azul.
                leer_cursos()  # Llama a la función para mostrar los cursos registrados.
            elif (
                opcion == "3"
            ):  # Si la opción es "3", se llama a la función para actualizar un curso.
                print(
                    "\033[1;34mActualizando un Curso...\033[0m"
                )  # Mensaje informativo en color azul.
                actualizar_curso()  # Llama a la función para actualizar un curso.
            elif (
                opcion == "4"
            ):  # Si la opción es "4", se llama a la función para eliminar un curso.
                print(
                    "\033[1;34mEliminando un Curso...\033[0m"
                )  # Mensaje informativo en color azul.
                eliminar_curso()  # Llama a la función para eliminar un curso.
            elif (
                opcion == "5"
            ):  # Si la opción es "5", se muestra un mensaje y se sale del bucle (vuelve al menú principal).
                print(
                    "\033[1;32mVolviendo al Menú Principal...\033[0m"
                )  # Mensaje informativo en color verde.
                break  # Sale del bucle, retornando al menú principal.
        except Exception as e:  # Si ocurre un error inesperado durante la ejecución
            error_rojo(
                f"Ocurrió un error inesperado: {e}. Verifique su conexión o los datos ingresados."
            )  # Muestra un mensaje de error detallado.

    # Limpiar la pantalla al volver al menú principal
    limpiar_pantalla()  # Llama a la función para limpiar la pantalla antes de mostrar el menú principal.
