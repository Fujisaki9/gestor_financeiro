import sqlite3

from rich import print as rprint

from shared.enums import TipoPagamento
from utils.ui import mostrar_menu_pagamento
from utils.validators import validar_integer


def escolher_forma_pagamento():
    """
    Exibe o menu de opções para o usuário escolher a forma de pagamento.
    :return: Forma de pagamento selecionada.
    """
    mostrar_menu_pagamento()
    while True:
        opcao = validar_integer("Escolha uma forma de pagamento: ")
        if opcao in (1, 2, 3, 4, 5):
            if opcao == 1:
                return TipoPagamento.DINHEIRO.value
            if opcao == 2:
                return TipoPagamento.PIX.value
            if opcao == 3:
                return TipoPagamento.BOLETO.value
            if opcao == 4:
                return TipoPagamento.CARTAO.value
            if opcao == 5:
                return TipoPagamento.OUTROS.value
        else:
            rprint("[bold red]Insira um comando válido![/]")


def conectar():
    """
    Abre e retorna uma conexão com o banco de dados.
    :return: Objeto de conexão SQLite.
    """
    return sqlite3.connect("gestor_financeiro.db")