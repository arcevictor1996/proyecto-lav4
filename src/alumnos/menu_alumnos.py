# Importaciones necesarias para el funcionamiento del menú y operaciones CRUD de alumnos
from .crud_alumnos import (
    crear_alumno,  # Función para crear un nuevo alumno
    leer_alumnos,  # Función para leer (mostrar) los alumnos registrados
    actualizar_alumno,  # Función para actualizar la información de un alumno
    eliminar_alumno,  # Función para eliminar un alumno
)

from src.utils.utils import (
    limpiar_pantalla,
    error_rojo,
)  # Funciones auxiliares para limpiar la pantalla y mostrar errores


# Función que muestra el menú de opciones relacionado con alumnos
def mostrar_menu_alumnos():
    print("\033[1;36m" + "=" * 30)  # Imprime una línea decorativa con color cian
    print("    Menú de Alumnos".center(30))  # Muestra el título del menú centrado
    print("=" * 30 + "\033[0m")  # Imprime otra línea decorativa al final del encabezado
    print("\n\033[1;32m-- Opciones --\033[0m")  # Imprime las opciones en color verde
    print("1. Crear Alumno")  # Opción para crear un alumno
    print("2. Leer Alumnos")  # Opción para mostrar los alumnos existentes
    print("3. Actualizar Alumno")  # Opción para actualizar un alumno
    print("4. Eliminar Alumno")  # Opción para eliminar un alumno
    print(
        "5. Volver al Menú Principal"
    )  # Opción para salir del menú de alumnos y volver al menú principal
    print("\033[1;36m" + "-" * 30 + "\033[0m")  # Línea decorativa final


# Función que obtiene y valida la opción seleccionada por el usuario
def obtener_opcion():
    while True:  # Bucle infinito hasta obtener una opción válida
        opcion = input(
            "\033[1;33mSeleccione una opción: \033[0m"
        ).strip()  # Solicita la opción al usuario
        if opcion in [
            "1",
            "2",
            "3",
            "4",
            "5",
        ]:  # Verifica si la opción es válida (entre 1 y 5)
            return opcion  # Retorna la opción válida
        else:
            error_rojo(
                "Opción no válida. Por favor, intente de nuevo."
            )  # Muestra un error si la opción no es válida


# Función principal del menú de alumnos, que maneja el flujo de selección de opciones
def menu_alumnos():
    while True:  # Bucle infinito hasta que el usuario elija salir
        try:
            mostrar_menu_alumnos()  # Muestra el menú de opciones
            opcion = obtener_opcion()  # Obtiene y valida la opción seleccionada

            # Ejecuta las acciones correspondientes según la opción seleccionada
            if opcion == "1":
                print(
                    "\033[1;34mCreando un nuevo Alumno...\033[0m"
                )  # Muestra mensaje informativo
                crear_alumno()  # Llama a la función para crear un nuevo alumno
            elif opcion == "2":
                print(
                    "\033[1;34mMostrando la lista de Alumnos...\033[0m"
                )  # Muestra mensaje informativo
                leer_alumnos()  # Llama a la función para mostrar los alumnos
            elif opcion == "3":
                print(
                    "\033[1;34mActualizando un Alumno...\033[0m"
                )  # Muestra mensaje informativo
                actualizar_alumno()  # Llama a la función para actualizar los datos de un alumno
            elif opcion == "4":
                print(
                    "\033[1;34mEliminando un Alumno...\033[0m"
                )  # Muestra mensaje informativo
                eliminar_alumno()  # Llama a la función para eliminar un alumno
            elif opcion == "5":
                print(
                    "\033[1;32mVolviendo al Menú Principal...\033[0m"
                )  # Muestra mensaje informativo
                break  # Sale del bucle, volviendo al menú principal
        except Exception as e:  # Captura cualquier error inesperado
            error_rojo(
                f"Se produjo un error inesperado: {e}. Por favor, intente nuevamente."  # Muestra el error
            )
    # Limpiar la pantalla al volver al menú principal
    limpiar_pantalla()  # Llama a la función para limpiar la pantalla
