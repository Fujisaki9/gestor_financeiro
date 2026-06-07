import sqlite3


def criar_tabelas():
    with sqlite3.connect("gestor_financeiro.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS salario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                empresa TEXT NOT NULL,
                cargo TEXT NOT NULL      
            )     
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS renda_extra (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                atividade TEXT NOT NULL,
                custo REAL NOT NULL            
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS freelance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                preco_hora REAL NOT NULL,
                horas_trabalhadas INTEGER NOT NULL,
                mes INTEGER NOT NULL,
                contratante TEXT NOT NULL         
            )        
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS aluguel (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                proprietario TEXT NOT NULL,
                forma_pagamento TEXT NOT NULL,
                endereco_imovel TEXT NOT NULL,
                numero_imovel TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                empresa TEXT NOT NULL,
                forma_pagamento TEXT NOT NULL,
                tipo_conta TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS plano_saude (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                operadora TEXT NOT NULL,
                forma_pagamento TEXT NOT NULL,
                tipo_plano TEXT NOT NULL    
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transporte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                empresa TEXT NOT NULL,
                forma_pagamento TEXT NOT NULL,
                tipo_servico TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alimentacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                local TEXT NOT NULL,
                forma_pagamento TEXT NOT NULL,
                tipo_servico TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lazer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                local TEXT NOT NULL,
                forma_pagamento TEXT NOT NULL,
                tipo_servico TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS farmacia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                local TEXT NOT NULL,
                forma_pagamento TEXT NOT NULL,
                tipo_servico TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS diversos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                mes INTEGER NOT NULL,
                local TEXT NOT NULL,
                forma_pagamento TEXT NOT NULL,
                tipo_servico TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS investimentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor_investido REAL NOT NULL,
                mes INTEGER NOT NULL,
                tipo_investimento TEXT NOT NULL,
                entidade TEXT NOT NULL
            )
        """)