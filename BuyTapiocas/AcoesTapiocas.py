from BancoDados import RepositorioGeral


class Tapiocas:

    def __init__(self, idtapioca=0, nometapioca=''):
        # Atributos das tapiocas
        self.idtapioca = idtapioca
        self.nometapioca = nometapioca

    def inserirtapioca(self):
        """ Inserindo uma tapioca no banco de dados. """
        tapioca = RepositorioGeral()

        try:

            if len(self.nometapioca) == 0:
                return "Tapioca não cadastrada!"
            else:
                cursor = tapioca.con.cursor()
                # Fazendo a inserção dos dados na tabela
                cursor.execute("insert into tapiocas (nometapioca) values ('" + self.nometapioca + "')")
                tapioca.con.commit()
                cursor.close()

                return "Tapioca cadastrada!"
        except:
            return "Tapioca não cadastrada!"

    def alteratapioca(self):

        """ Alterando os dados de uma tapioca já cadastrada. """

        tapioca = RepositorioGeral()

        try:

            cursor2 = tapioca.con.cursor()
            cursor2.execute("update tapiocas set nometapioca = ? where idtapioca = ?", (self.nometapioca, self.idtapioca))
            tapioca.con.commit()
            cursor2.close()

            return "Alteração feita com sucesso!"

        except:
            return "Alteração não realizada!"

    def removetapioca(self):
        """ Exclusão das informações de uma tapioca. """
        tapioca = RepositorioGeral()

        try:

            cursor3 = tapioca.con.cursor()
            cursor3.execute(f"delete from tapiocas where idtapioca = {self.idtapioca}")
            tapioca.con.commit()
            cursor3.close()

            return 'Tapioca removida!'
        except:
            return 'Tapioca não removida!'

    def consultatapioca(self, idtapioca):
        """ Consulta de tapiocas. """
        tapioca = RepositorioGeral()

        try:

            cursor = tapioca.con.cursor()
            cursor.execute(f"select *from tapiocas where idtapioca = {idtapioca}")
            for linha in cursor:
                self.idtapioca = linha[0]
                self.nometapioca = linha[1]

            cursor.close()

            return "Tapioca localizada!"
        except:
            return "Tapioca não localizada!"
