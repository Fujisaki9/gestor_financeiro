from time import sleep

from rich import print as rprint

from database.setup import criar_tabelas
from fixed_expense.services import escolher_tipo_gasto_fixo
from investment.services import registrar_investimento
from report.services import abrir_menu_relatorio
from revenue.services import escolher_tipo_receita
from utils.console import limpar_console
from utils.ui import mostrar_menu_opcoes
from utils.validators import validar_integer
from variable_expense.services import escolher_tipo_gasto_variavel


def main():
    criar_tabelas()

    while True:
        limpar_console()
        mostrar_menu_opcoes()
        opcao = validar_integer("Escolha uma opção: ")
        match opcao:
            case 1:
                escolher_tipo_receita()
            case 2:
                escolher_tipo_gasto_fixo()
            case 3:
                escolher_tipo_gasto_variavel()
            case 4:
                registrar_investimento()
            case 5:
                abrir_menu_relatorio()
            case 6:
                rprint("[bold blue]Saindo do programa...[/]")
                sleep(1)
                rprint("[bold blue]Programa encerrado![/]")
                break
            case _:
                rprint("[bold red]ERRO: Insira um comando válido![/]")
                sleep(1)

if __name__ == "__main__":
    main()