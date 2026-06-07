from rich import print as rprint

from shared.enums import TipoAlimentacao, TipoFarmacia, TipoLazer
from utils.console import limpar_console
from utils.services import escolher_forma_pagamento
from utils.validators import validar_float, validar_integer, validar_mes
from variable_expense.models import Alimentacao, Lazer, Farmacia, Diversos
from variable_expense.repository import (inserir_registro_alimentacao, inserir_registro_lazer, inserir_registro_farmacia,
                                       inserir_registro_diverso)
from variable_expense.ui import (mostrar_menu_gastos_variaveis, mostrar_tipos_alimentacao, mostrar_tipos_lazer,
                               mostrar_tipos_farmacia)


def escolher_tipo_gasto_variavel():
    """
    Exibe o menu de tipos de gastos variáveis e permite ao usuário escolher um tipo.
    :return: None.
    """
    while True:
        limpar_console()
        mostrar_menu_gastos_variaveis()
        indice = validar_integer("Escolha uma opção: ")
        match indice:
            case 1:
                registrar_gasto_alimentacao()
            case 2:
                registrar_gasto_lazer()
            case 3:
                registrar_gasto_farmacia()
            case 4:
                registrar_gasto_diverso()
            case 5:
                limpar_console()
                break
            case _:
                rprint("[bold red]Insira um comando válido![/]")


def registrar_gasto_alimentacao():
    """
    Registra um gasto com alimentação no banco de dados.
    :return: None.
    """
    limpar_console()
    valor = validar_float("Valor gasto: R$ ")
    mes = validar_mes("Mês: ")
    origem = input("Local ou estabelecimento: ").strip().title()
    forma_pagamento = escolher_forma_pagamento()
    tipo_alimentacao = escolher_tipo_alimentacao()
    novo_registro = Alimentacao(valor, mes, origem, forma_pagamento, tipo_alimentacao)
    inserir_registro_alimentacao(novo_registro)


def registrar_gasto_lazer():
    """
    Registra um gasto com lazer no banco de dados.
    :return: None.
    """
    limpar_console()
    valor = validar_float("Valor gasto: R$ ")
    mes = validar_mes("Mês: ")
    origem = input("Local ou estabelecimento: ").strip().title()
    forma_pagamento = escolher_forma_pagamento()
    tipo_lazer = escolher_tipo_lazer()
    novo_registro = Lazer(valor, mes, origem, forma_pagamento, tipo_lazer)
    inserir_registro_lazer(novo_registro)


def registrar_gasto_farmacia():
    """
    Registra um gasto com farmácia no banco de dados.
    :return: None.
    """
    limpar_console()
    valor = validar_float("Valor gasto: R$ ")
    mes = validar_mes("Mês: ")
    origem = input("Nome da farmácia: ").strip().title()
    forma_pagamento = escolher_forma_pagamento()
    tipo_farmacia = escolher_tipo_farmacia()
    novo_registro = Farmacia(valor, mes, origem, forma_pagamento, tipo_farmacia)
    inserir_registro_farmacia(novo_registro)


def registrar_gasto_diverso():
    """
    Registra um gasto diverso no banco de dados.
    :return: None.
    """
    limpar_console()
    valor = validar_float("Valor gasto: R$ ")
    mes = validar_mes("Mês: ")
    origem = input("Local ou estabelecimento: ").strip().title()
    forma_pagamento = escolher_forma_pagamento()
    descricao_servico = input("Descrição do gasto: ").strip().title()
    novo_registro = Diversos(valor, mes, origem, forma_pagamento, descricao_servico)
    inserir_registro_diverso(novo_registro)


def escolher_tipo_alimentacao():
    """
    Exibe o menu de tipos de alimentação e permite ao usuário escolher um tipo.
    :return: O tipo de alimentação escolhido.
    """
    mostrar_tipos_alimentacao()
    while True:
        opcao = validar_integer("Escolha o tipo de alimentação: ")
        match opcao:
            case 1:
                return TipoAlimentacao.SUPERMERCADO.value
            case 2:
                return TipoAlimentacao.RESTAURANTE.value
            case 3:
                return TipoAlimentacao.DELIVERY.value
            case 4:
                return TipoAlimentacao.OUTROS.value
            case _:
                rprint("[bold red]Insira um comando válido![/]")


def escolher_tipo_lazer():
    """
    Exibe o menu de tipos de lazer e permite ao usuário escolher um tipo.
    :return: O tipo de lazer escolhido.
    """
    mostrar_tipos_lazer()
    while True:
        opcao = validar_integer("Escolha o tipo de lazer: ")
        match opcao:
            case 1:
                return TipoLazer.SHOPPING.value
            case 2:
                return TipoLazer.VIAGEM.value
            case 3:
                return TipoLazer.ACADEMIA.value
            case 4:
                return TipoLazer.OUTROS.value
            case _:
                rprint("[bold red]Insira um comando válido![/]")


def escolher_tipo_farmacia():
    """
    Exibe o menu de tipos de farmácia e permite ao usuário escolher um tipo.
    :return: O tipo de farmácia escolhido.
    """
    mostrar_tipos_farmacia()
    while True:
        opcao = validar_integer("Escolha o tipo de produto: ")
        match opcao:
            case 1:
                return TipoFarmacia.MEDICAMENTO.value
            case 2:
                return TipoFarmacia.COSMETICO.value
            case 3:
                return TipoFarmacia.SUPLEMENTO.value
            case 4:
                return TipoFarmacia.OUTROS.value
            case _:
                rprint("[bold red]Insira um comando válido![/]")