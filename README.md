# 💰 Gestor Financeiro

Um sistema de gestão financeira pessoal desenvolvido em console como projeto de aprendizado de Programação Orientada a 
Objetos (POO) em Python com banco de dados SQLite.

## 🛠️ Tecnologias e Bibliotecas utilizadas

* Linguagem: Python 3
* Bibliotecas: `rich` (formatação visual), `sqlite3` (banco de dados), `enum` (categorias fixas), `abc` (classes abstratas)
* Ambiente: PyCharm

## ⚙️ Funcionalidades

* Receitas — Registro de salário, renda extra e freelance.
* Gastos Fixos — Registro de aluguel, contas, plano de saúde e transporte.
* Gastos Variáveis — Registro de alimentação, lazer, farmácia e diversos.
* Investimentos — Registro de investimentos mensais.
* Relatório por categoria — Visualização detalhada de cada categoria de gasto ou receita.
* Relatório mensal — Consolidado com total de ganhos, gastos, investimentos e saldo do mês.

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado.
2. Clone o repositório: `git clone https://github.com/Fujisaki9/gestor_financeiro.git`
3. Instale as dependências: `pip install rich`
4. Execute o programa: `main.py`

-> ⚠️ PyCharm: Habilite **Emulate terminal in output** em `Run > Edit Configurations > Emulate terminal in output console` 
para visualizar a interface colorida corretamente. **Obrigatório.**

## 📚 Aprendizados

* Aplicação de POO: classes abstratas, herança, encapsulamento e composição.
* Integração com banco de dados SQLite — criação de tabelas, inserção e consulta de dados.
* Organização do código em múltiplos packages seguindo separação de responsabilidades.
* Uso de Enum para controle de valores fixos.
* Validação de inputs do usuário.

Desenvolvido por Celso Henrique Pereira Benassi.