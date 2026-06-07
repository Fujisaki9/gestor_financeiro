from utils.services import conectar

from fixed_expense.models import Aluguel, Conta, PlanoSaude, Transporte
from investment.models import Investimento
from revenue.models import Salario, RendaExtra, Freelance
from variable_expense.models import Alimentacao, Lazer, Farmacia, Diversos


def buscar_salario():
    """
    Busca todos os salários registrados no banco de dados.
    :return: Lista de objetos Salario.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, empresa, cargo FROM salario")
        registros = cursor.fetchall()
        return [Salario(valor, mes, empresa, cargo)
               for valor, mes, empresa, cargo in registros]


def buscar_renda_extra():
    """
    Busca todas as rendas extras registradas no banco de dados.
    :return: Lista de objetos RendaExtra.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, atividade, custo FROM renda_extra")
        registros = cursor.fetchall()
        return [RendaExtra(valor, mes, atividade, custo)
               for valor, mes, atividade, custo in registros]


def buscar_freelance():
    """
    Busca todos os freelancers registrados no banco de dados.
    :return: Lista de objetos Freelance.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT mes, contratante, preco_hora, horas_trabalhadas FROM freelance")
        registros = cursor.fetchall()
        return [Freelance(mes, contratante, preco_hora, horas_trabalhadas)
               for mes, contratante, preco_hora, horas_trabalhadas in registros]


def buscar_aluguel():
    """
    Busca todos os aluguéis registrados no banco de dados.
    :return: Lista de objetos Aluguel.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, proprietario, forma_pagamento, endereco_imovel, numero_imovel FROM aluguel")
        registros = cursor.fetchall()
        return [Aluguel(valor, mes, proprietario, forma_pagamento, endereco_imovel, numero_imovel)
               for valor, mes, proprietario, forma_pagamento, endereco_imovel, numero_imovel in registros]


def buscar_conta():
    """
    Busca todas as contas registradas no banco de dados.
    :return: Lista de objetos Conta.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, empresa, forma_pagamento, tipo_conta FROM conta")
        registros = cursor.fetchall()
        return [Conta(valor, mes, empresa, forma_pagamento, tipo_conta)
               for valor, mes, empresa, forma_pagamento, tipo_conta in registros]


def buscar_plano_saude():
    """
    Busca todos os planos de saúde registrados no banco de dados.
    :return: Lista de objetos PlanoSaude.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, operadora, forma_pagamento, tipo_plano FROM plano_saude")
        registros = cursor.fetchall()
        return [PlanoSaude(valor, mes, operadora, forma_pagamento, tipo_plano)
               for valor, mes, operadora, forma_pagamento, tipo_plano in registros]


def buscar_transporte():
    """
    Busca todos os serviços de transporte registrados no banco de dados.
    :return: Lista de objetos Transporte.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, empresa, forma_pagamento, tipo_servico FROM transporte")
        registros = cursor.fetchall()
        return [Transporte(valor, mes, empresa, forma_pagamento, tipo_servico)
               for valor, mes, empresa, forma_pagamento, tipo_servico in registros]


def buscar_alimentacao():
    """
    Busca todas as despesas com alimentação registradas no banco de dados.
    :return: Lista de objetos Alimentacao.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, local, forma_pagamento, tipo_servico FROM alimentacao")
        registros = cursor.fetchall()
        return [Alimentacao(valor, mes, local, forma_pagamento, tipo_servico)
               for valor, mes, local, forma_pagamento, tipo_servico in registros]


def buscar_lazer():
    """
    Busca todas as despesas com lazer registradas no banco de dados.
    :return: Lista de objetos Lazer.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, local, forma_pagamento, tipo_servico FROM lazer")
        registros = cursor.fetchall()
        return [Lazer(valor, mes, local, forma_pagamento, tipo_servico)
               for valor, mes, local, forma_pagamento, tipo_servico in registros]


def buscar_farmacia():
    """
    Busca todas as despesas com farmácia registradas no banco de dados.
    :return: Lista de objetos Farmacia.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, local, forma_pagamento, tipo_servico FROM farmacia")
        registros = cursor.fetchall()
        return [Farmacia(valor, mes, local, forma_pagamento, tipo_servico)
               for valor, mes, local, forma_pagamento, tipo_servico in registros]


def buscar_diversos():
    """
    Busca todas as despesas diversas registradas no banco de dados.
    :return: Lista de objetos Diversos.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, local, forma_pagamento, tipo_servico FROM diversos")
        registros = cursor.fetchall()
        return [Diversos(valor, mes, local, forma_pagamento, tipo_servico)
               for valor, mes, local, forma_pagamento, tipo_servico in registros]


def buscar_investimentos():
    """
    Busca todos os investimentos registrados no banco de dados.
    :return: Lista de objetos Investimento.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor_investido, mes, tipo_investimento, entidade FROM investimentos")
        registros = cursor.fetchall()
        return [Investimento(valor_investido, mes, tipo_investimento, entidade)
               for valor_investido, mes, tipo_investimento, entidade in registros]


def buscar_salario_mes(mes):
    """
    Busca o salário de um mês específico.
    :param mes: Mês para o qual se deseja buscar o salário.
    :return: Lista de objetos Salario ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, empresa, cargo FROM salario WHERE mes = ?", (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Salario(valor, mes, empresa, cargo) for valor, mes, empresa, cargo in registros]


def buscar_renda_extra_mes(mes):
    """
    Busca as rendas extras de um mês específico.
    :param mes: Mês para o qual se deseja buscar as rendas extras.
    :return: Lista de objetos RendaExtra ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, atividade, custo FROM renda_extra WHERE mes = ?", (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [RendaExtra(valor, mes, atividade, custo) for valor, mes, atividade, custo in registros]


def buscar_freelance_mes(mes):
    """
    Busca os freelances de um mês específico.
    :param mes: Mês para o qual se deseja buscar os freelances.
    :return: Lista de objetos Freelance ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT mes, contratante, preco_hora, horas_trabalhadas FROM freelance WHERE mes = ?",
                       (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Freelance(mes, contratante, preco_hora, horas_trabalhadas)
                for mes, contratante, preco_hora, horas_trabalhadas in registros]


def buscar_aluguel_mes(mes):
    """
    Busca os aluguéis de um mês específico.
    :param mes: Mês para o qual se deseja buscar os aluguéis.
    :return: Lista de objetos Aluguel ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, proprietario, forma_pagamento, endereco_imovel, numero_imovel "
                       "FROM aluguel WHERE mes = ?", (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Aluguel(valor, mes, proprietario, forma_pagamento, endereco_imovel, numero_imovel)
                for valor, mes, proprietario, forma_pagamento, endereco_imovel, numero_imovel in registros]


def buscar_conta_mes(mes):
    """
    Busca as contas de um mês específico.
    :param mes: Mês para o qual se deseja buscar as contas.
    :return: Lista de objetos Conta ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, empresa, forma_pagamento, tipo_conta FROM conta WHERE mes = ?",
                       (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Conta(valor, mes, empresa, forma_pagamento, tipo_conta)
                for valor, mes, empresa, forma_pagamento, tipo_conta in registros]


def buscar_plano_saude_mes(mes):
    """
    Busca os planos de saúde de um mês específico.
    :param mes: Mês para o qual se deseja buscar os planos de saúde.
    :return: Lista de objetos PlanoSaude ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, operadora, forma_pagamento, tipo_plano FROM plano_saude WHERE mes = ?",
                       (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [PlanoSaude(valor, mes, operadora, forma_pagamento, tipo_plano)
                for valor, mes, operadora, forma_pagamento, tipo_plano in registros]


def buscar_transporte_mes(mes):
    """
    Busca os serviços de transporte de um mês específico.
    :param mes: Mês para o qual se deseja buscar os serviços de transporte.
    :return: Lista de objetos Transporte ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, empresa, forma_pagamento, tipo_servico FROM transporte WHERE mes = ?",
                       (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Transporte(valor, mes, empresa, forma_pagamento, tipo_servico)
                for valor, mes, empresa, forma_pagamento, tipo_servico in registros]


def buscar_alimentacao_mes(mes):
    """
    Busca as despesas com alimentação de um mês específico.
    :param mes: Mês para o qual se deseja buscar as despesas com alimentação.
    :return: Lista de objetos Alimentacao ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, local, forma_pagamento, tipo_servico FROM alimentacao WHERE mes = ?",
                       (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Alimentacao(valor, mes, local, forma_pagamento, tipo_servico)
                for valor, mes, local, forma_pagamento, tipo_servico in registros]


def buscar_lazer_mes(mes):
    """
    Busca as despesas com lazer de um mês específico.
    :param mes: Mês para o qual se deseja buscar as despesas com lazer.
    :return: Lista de objetos Lazer ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, local, forma_pagamento, tipo_servico FROM lazer WHERE mes = ?",
                       (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Lazer(valor, mes, local, forma_pagamento, tipo_servico)
                for valor, mes, local, forma_pagamento, tipo_servico in registros]


def buscar_farmacia_mes(mes):
    """
    Busca as despesas com farmácia de um mês específico.
    :param mes: Mês para o qual se deseja buscar as despesas com farmácia.
    :return: Lista de objetos Farmacia ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, local, forma_pagamento, tipo_servico FROM farmacia WHERE mes = ?",
                       (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Farmacia(valor, mes, local, forma_pagamento, tipo_servico)
                for valor, mes, local, forma_pagamento, tipo_servico in registros]


def buscar_diversos_mes(mes):
    """
    Busca as despesas diversas de um mês específico.
    :param mes: Mês para o qual se deseja buscar as despesas diversas.
    :return: Lista de objetos Diversos ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor, mes, local, forma_pagamento, tipo_servico FROM diversos WHERE mes = ?",
                       (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Diversos(valor, mes, local, forma_pagamento, tipo_servico)
                for valor, mes, local, forma_pagamento, tipo_servico in registros]


def buscar_investimentos_mes(mes):
    """
    Busca os investimentos de um mês específico.
    :param mes: Mês para o qual se deseja buscar os investimentos.
    :return: Lista de objetos Investimento ou lista vazia se não houver registros.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT valor_investido, mes, tipo_investimento, entidade FROM investimentos WHERE mes = ?",
                       (mes,))
        registros = cursor.fetchall()
        if not registros:
            return list()
        return [Investimento(valor_investido, mes, tipo_investimento, entidade)
                for valor_investido, mes, tipo_investimento, entidade in registros]