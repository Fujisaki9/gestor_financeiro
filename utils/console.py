import os


def limpar_console():
    """
    Limpa o console, independentemente do sistema operacional.
    :return: None.
    """
    if os.name == 'nt':
        comando = 'cls'
    else:
        comando = 'clear'
    os.system(comando)
