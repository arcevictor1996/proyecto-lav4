import os


def limpiar_pantalla():
    # Limpia la pantalla dependiendo del sistema operativo
    os.system("cls" if os.name == "nt" else "clear")


# Código ANSI para texto rojo para mensajes de erores
def error_rojo(mensaje):
    print(f"\033[31m{mensaje}\033[0m")
