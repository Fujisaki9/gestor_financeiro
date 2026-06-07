from rich import print as rprint


def validar_mes(valor):
    """
    Valida e retorna um mês inserido pelo usuário.
    :param valor: Mensagem exibida ao solicitar o input.
    :return: Número inteiro entre 1 e 12.
    """
    while True:
        try:
            mes = int(input(valor))
            if 1 <= mes <= 12:
                return mes
            else:
                rprint("[bold red]Mês inválido! Digite um valor entre 1 e 12.[/]")
        except ValueError:
            rprint("[bold red]ERRO: Digite um comando válido![/]")


def validar_float(valor):
    """
    Valida e retorna um valor float inserido pelo usuário.
    :param valor: Mensagem exibida ao solicitar o input.
    :return: Valor float maior que zero.
    """
    while True:
        try:
            valor_float = float(input(valor))
            if valor_float > 0:
                return valor_float
            else:
                rprint("[bold red]Valor inválido! Digite um valor acima de zero.[/]")
        except ValueError:
            rprint("[bold red]ERRO: Digite um comando válido![/]")


def validar_integer(valor):
    """
    Valida e retorna um número inteiro inserido pelo usuário.
    :param valor: Mensagem exibida ao solicitar o input.
    :return: Valor inteiro maior que zero.
    """
    while True:
        try:
            integer = int(input(valor))
            if integer > 0:
                return integer
            else:
                rprint("[bold red]Valor inválido! Digite um valor acima de zero.[/]")
        except ValueError:
            rprint("[bold red]ERRO: Digite um comando válido![/]")
