from utils.services import conectar


def inserir_salario(salario):
    """
    Insere um novo registro de salário no banco de dados.
    :param salario: Objeto do tipo Salario.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO salario (valor, mes, empresa, cargo)
            VALUES (?, ?, ?, ?)
        """,(salario.valor, salario.mes, salario.origem, salario.cargo))
        conexao.commit()


def inserir_renda_extra(renda):
    """
    Insere um novo registro de renda extra no banco de dados.
    :param renda: Objeto do tipo RendaExtra.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO renda_extra (valor, mes, atividade, custo)
            VALUES (?, ?, ?, ?)
        """,(renda.valor, renda.mes, renda.origem, renda.custo))
        conexao.commit()


def inserir_freelance(freelance):
    """
    Insere um novo registro de freelance no banco de dados.
    :param freelance: Objeto do tipo Freelance.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO freelance (valor, preco_hora, horas_trabalhadas, mes, contratante)
            VALUES (?, ?, ?, ?, ?)
        """,(freelance.valor, freelance.valor_hora, freelance.horas_trabalhadas, freelance.mes,
                       freelance.origem))
        conexao.commit()