"""
Banco de dados para cadastro de clientes e cadastro de tapiocas e acompanhamentos

- cursor: é um interador que permite navegar e manipular os registros do bd.
- execute: lê e executa comandos SQL puro diretamente no bd.

"""

import sqlite3


class RepositorioGeral:
    """ Classe banco de dados de clientes e tapiocas
        Utilizada para o acesso ao banco de dados de clientes e tapiocas

        arq: BancoDados.py
    """

    def __init__(self):
        # Criando conexão objeto que representa um banco de dados
        self.con = sqlite3.connect('dadosgerais.db')
        # Criando relação
        self.createtable1()
        self.createtable2()

    def createtable1(self):
        # Criando um cursor para acessar os métodos do banco de dados
        cur = self.con.cursor()

        # Fazendo a relação
        cur.execute("""create table if not exists clientes (
                    idcliente integer primary key autoincrement,
                    nome text,
                    email text,
                    CEP text,
                    cidade text,
                    bairro text,
                    estado text,
                    numero text,
                    rua text)""")
        # Gravando informações no banco de dados
        self.con.commit()
        # Fechando cursor
        cur.close()

    def createtable2(self):
        cur = self.con.cursor()

        cur.execute(""" create table if not exists tapiocas (
                    idtapioca integer primary key autoincrement,
                    nometapioca text)""")
        self.con.commit()
        cur.close()
