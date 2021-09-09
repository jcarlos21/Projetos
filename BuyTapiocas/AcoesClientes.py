from BancoDados import RepositorioGeral


class Clientes:
    """ Classe destinada a fazer a inserção dos clientes no banco de dados. """

    def __init__(self, idcliente=0, nome='', email='', cep='', cidade='', bairro='', estado='', numero='', rua=''):
        # Atributos do cliente
        self.idcliente = idcliente
        self.nome = nome
        self.email = email
        self.cep = cep
        self.cidade = cidade
        self.bairro = bairro
        self.estado = estado
        self.numero = numero
        self.rua = rua

    def inserircliente(self):

        """ Inserindo um cliente no banco de dados. """

        # Criando uma instância da classe RepositorioClientes
        cliente = RepositorioGeral()

        try:

            # Criando cursor para acesso ao banco de dados
            cursor = cliente.con.cursor()

            if len(self.nome) == 0 or len(self.email) == 0 or len(self.cep) == 0 or len(self.cidade) == 0 or len(self.bairro) == 0 or len(self.estado) == 0 or len(self.numero) == 0 or len(self.rua) == 0:
                return "Cliente não cadastrado!"
            else:
                # Inserindo cliente
                cursor.execute("insert into clientes (nome, email, CEP, cidade, bairro, estado, numero, "
                               "rua) values (?, ?, ?, ?, ?, ?, ?, ?)", (self.nome, self.email, self.cep, self.cidade,
                                                                        self.bairro, self.estado, self.numero,
                                                                        self.rua))

                # Salvando no banco
                cliente.con.commit()

                # Encerrando o cursor
                cursor.close()

                return "Cliente cadastrado!"

        except:
            return "Cliente não cadastrado!"

    def alteracliente(self):

        """ Alterando os dados de um cliente já cadastrado. """

        cliente = RepositorioGeral()

        try:

            cursor2 = cliente.con.cursor()

            # Alteração dos dados
            cursor2.execute("update clientes set nome = ?, email = ?, CEP = ?, cidade = ?,"
                            "bairro = ?, estado = ?,  numero = ?, rua = ? where idcliente = ? ",
                            (self.nome, self.email, self.cep, self.cidade,
                             self.bairro, self.estado, self.numero, self.rua, self.idcliente))

            cliente.con.commit()  # Salvando as alterações no banco
            cursor2.close()

            return "Alteração feita com sucesso!"

        except:
            return "Alteração não realizada!"

    def removecliente(self):
        """ Exclusão das informações de um cliente. """
        cliente = RepositorioGeral()

        try:

            # Cursor para acesso ao banco de dados
            cursor3 = cliente.con.cursor()

            # Realizando a exclusão
            cursor3.execute(f"delete from clientes where idcliente = {self.idcliente}")

            cliente.con.commit()  # Salvando alterações no banco
            cursor3.close()

            return 'Cliente removido!'
        except:
            return 'Cliente não removido!'

    def consultacliente(self, idcliente):
        """ Consulta de clientes. """
        cliente = RepositorioGeral()
        try:

            # Cursor para acesso ao banco
            cursor4 = cliente.con.cursor()

            # Fazendo consulta
            cursor4.execute(f"select *from clientes where idcliente = {idcliente}")

            # Se o código digitado for encontrado os componentes abaixo recebem os valores armazenados no banco
            for linha in cursor4:
                self.idcliente = linha[0]
                self.nome = linha[1]
                self.email = linha[2]
                self.cep = linha[3]
                self.cidade = linha[4]
                self.bairro = linha[5]
                self.estado = linha[6]
                self.numero = linha[7]
                self.rua = linha[8]

            # Encerrando o cursor
            cursor4.close()

            return "Cliente localizado!"
        except:
            return "Cliente não localizado!"
