import os


def limpiar_pantalla():
    # Limpia la pantalla dependiendo del sistema operativo
    os.system("cls" if os.name == "nt" else "clear")
