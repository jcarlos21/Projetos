from tkinter import *
from AcoesClientes import Clientes
from AcoesTapiocas import Tapiocas
from BancoDados import RepositorioGeral
from tkinter import ttk
from PIL import ImageTk, Image


class Principal:
    def __init__(self, master=None):

        # Definindo os containeres (que serão as abas do programa)
        self.abaprincipal = ttk.Notebook(master, width=450, height=390)  # 'abaprincipal' é o container principal
        self.aba1_cliente = Frame(self.abaprincipal)
        self.aba2_tapioca = Frame(self.abaprincipal)
        self.aba3_consultacliente = Frame(self.abaprincipal)
        self.aba4_consultatapioca = Frame(self.abaprincipal)
        self.aba5_sobre = Frame(self.abaprincipal)

        # Mostrando as abas
        self.abaprincipal.add(self.aba1_cliente, text="Clientes")
        self.abaprincipal.add(self.aba2_tapioca, text="Tapiocas")
        self.abaprincipal.add(self.aba3_consultacliente, text="Clientes cadastrados")
        self.abaprincipal.add(self.aba4_consultatapioca, text="Tapiocas disponíveis")
        self.abaprincipal.add(self.aba5_sobre, text="Sobre o Buy Tapiocas")
        self.abaprincipal.pack()  # O gerenciador pack exibe na tela

        """Aba 1 Clientes"""

        # Mensagens na aba1: Clientes

        self.mensagem_aba1 = Label(self.aba1_cliente, text="Entre com os dados do cliente:")  # Definindo frase
        self.mensagem_aba1['font'] = ("Verdana", "9", "bold")
        self.mensagem_aba1.place(x=145, y=20)

        self.mensagem2_aba1 = Label(self.aba1_cliente, text="Faça uma consulta:")
        self.mensagem2_aba1['font'] = ("Verdana", "9", "bold")
        self.mensagem2_aba1.place(x=167, y=275)

        self.mensagem3_aba1 = Label(self.aba1_cliente, text="",  # Status
                                    fg="blue")  # text="" indica que ainda vai receber um texto
        self.mensagem3_aba1['font'] = ("Verdana", "9", "italic")
        self.mensagem3_aba1.place(x=210, y=250)

        # Configurações de rótulos e widgets da aba1: Clientes

        self.rotulonome = Label(self.aba1_cliente, text="Nome:")
        self.rotulonome.place(x=25, y=55)
        self.caixanome = Entry(self.aba1_cliente)
        self.caixanome['width'] = 55
        self.caixanome.place(x=80, y=55)

        self.rotuloemail = Label(self.aba1_cliente, text="E-mail:")  # Criando widget 'E-mail'
        self.rotuloemail.place(x=25, y=95)  # Localizando o texto 'E-mail' no container aba1_cliente
        self.caixaemail = Entry(self.aba1_cliente)  # Criando caixa de texto que vai receber dados
        self.caixaemail['width'] = 55  # Definindo largura do caixa de texto
        self.caixaemail.place(x=80, y=95)  # Localizando caixa de texto no container aba1_cliente

        self.rotulorua = Label(self.aba1_cliente, text="Rua:")
        self.rotulorua.place(x=25, y=135)
        self.caixarua = Entry(self.aba1_cliente)
        self.caixarua['width'] = 40
        self.caixarua.place(x=80, y=135)  # Adicionou 55 em x

        self.rotulonum = Label(self.aba1_cliente, text="Nº:")
        self.rotulonum.place(x=300, y=135)
        self.caixanum = Entry(self.aba1_cliente)
        self.caixanum['width'] = 14
        self.caixanum.place(x=326, y=135)

        self.rotulobairro = Label(self.aba1_cliente, text="Bairro:")
        self.rotulobairro.place(x=25, y=170)
        self.caixabairro = Entry(self.aba1_cliente)
        self.caixabairro['width'] = 23
        self.caixabairro.place(x=80, y=170)

        self.rotulocep = Label(self.aba1_cliente, text="CEP:")
        self.rotulocep.place(x=215, y=170)
        self.caixacep = Entry(self.aba1_cliente)
        self.caixacep['width'] = 27
        self.caixacep.place(x=248, y=170)

        self.rotulocidade = Label(self.aba1_cliente, text="Cidade:")
        self.rotulocidade.place(x=25, y=210)
        self.caixacidade = Entry(self.aba1_cliente)
        self.caixacidade['width'] = 35
        self.caixacidade.place(x=80, y=210)

        self.rotuloestado = Label(self.aba1_cliente, text="UF:")
        self.rotuloestado.place(x=300, y=210)
        self.caixaestado = Entry(self.aba1_cliente)
        self.caixaestado['width'] = 14
        self.caixaestado.place(x=326, y=210)

        self.rotuloidcliente = Label(self.aba1_cliente, text="ID Cliente:")
        self.rotuloidcliente.place(x=25, y=310)
        self.caixaidcliente = Entry(self.aba1_cliente)
        self.caixaidcliente['width'] = 10
        self.caixaidcliente.place(x=100, y=310)

        # Botões da aba1: Clientes

        self.botaogravar = Button(self.aba1_cliente, text="Salvar informações")  # Definindo botão salvar
        self.botaogravar['command'] = self.gravarcliente  # 'self.gravarcliente' trata-se de uma função mais adiante
        self.botaogravar.place(x=25, y=245)

        self.botaobuscar = Button(self.aba1_cliente, text="Buscar")
        self.botaobuscar['command'] = self.buscacliente
        self.botaobuscar.place(x=175, y=306)

        self.botaoatualizar = Button(self.aba1_cliente, text="Atualizar")
        self.botaoatualizar['command'] = self.atualizacliente
        self.botaoatualizar.place(x=236, y=306)

        self.botaoapagar = Button(self.aba1_cliente, text="Apagar")
        self.botaoapagar['command'] = self.apagacliente
        self.botaoapagar.place(x=307, y=306)

        self.botaosair = Button(self.aba1_cliente, text="Sair")
        self.botaosair['command'] = self.abaprincipal.quit  # Sai do programa ao ser pressionado
        self.botaosair.place(x=370, y=306)

        """Aba 2 Tapiocas"""

        # Mensagens na aba2: Tapiocas

        self.mensagem_aba2 = Label(self.aba2_tapioca, text="Entre com o tipo da tapioca:")  # Definindo frase
        self.mensagem_aba2['font'] = ("Verdana", "9", "bold")
        self.mensagem_aba2.place(x=145, y=20)

        self.mensagem2_aba2 = Label(self.aba2_tapioca, text="",
                                    fg="blue")  # text="" indica que ainda vai receber um texto
        self.mensagem2_aba2['font'] = ("Verdana", "9", "italic")
        self.mensagem2_aba2.place(x=210, y=90)

        self.mensagem3_aba2 = Label(self.aba2_tapioca, text="Faça uma consulta:")
        self.mensagem3_aba2['font'] = ("Verdana", "9", "bold")
        self.mensagem3_aba2.place(x=165, y=125)

        # Configurações da aba2: Tapiocas

        self.rotulonometapioca = Label(self.aba2_tapioca, text="Nome da tapioca:")
        self.rotulonometapioca.place(x=25, y=55)
        self.caixanometapioca = Entry(self.aba2_tapioca)
        self.caixanometapioca['width'] = 47
        self.caixanometapioca.place(x=128, y=55)

        self.rotuloidtapioca = Label(self.aba2_tapioca, text="ID Tapioca:")
        self.rotuloidtapioca.place(x=25, y=160)
        self.caixaidtapioca = Entry(self.aba2_tapioca)
        self.caixaidtapioca['width'] = 10
        self.caixaidtapioca.place(x=128, y=160)

        # Botões da aba2: Tapiocas
        self.botaogravartapioca = Button(self.aba2_tapioca, text="Salvar informações")  # Definindo botão salvar
        self.botaogravartapioca['command'] = self.gravartapioca
        self.botaogravartapioca.place(x=25, y=85)

        self.botaobuscartapioca = Button(self.aba2_tapioca, text="Buscar")
        self.botaobuscartapioca['command'] = self.buscatapioca
        self.botaobuscartapioca.place(x=215, y=155)

        self.botaoatualizartapioca = Button(self.aba2_tapioca, text="Atualizar")
        self.botaoatualizartapioca['command'] = self.atualizatapioca
        self.botaoatualizartapioca.place(x=276, y=155)

        self.botaoapagartapioca = Button(self.aba2_tapioca, text="Apagar")
        self.botaoapagartapioca['command'] = self.apagatapioca
        self.botaoapagartapioca.place(x=347, y=155)

        self.botaosairaba2 = Button(self.aba2_tapioca, text="Sair")
        self.botaosairaba2['command'] = self.abaprincipal.quit  # Sai do programa ao ser pressionado
        self.botaosairaba2.place(x=25, y=306)

        """Aba 3 Clientes cadastrados"""

        # Configurações na aba3: Clientes cadastrados

        self.arvore = ttk.Treeview(self.aba3_consultacliente)  # Montando a árvore
        self.arvore.bind("<<TreeviewSelect>>", self.arvore_select)  # Associando uma função a um evento

        bancodedados = RepositorioGeral()
        cursor = bancodedados.con.cursor()

        filhosdaarvore = self.arvore.get_children()

        for filho in filhosdaarvore:
            self.arvore.delete(filho)

        self.arvore['columns'] = ("ID", "Nome", "E-mail", "Cidade")
        self.arvore.column("ID", width=30)
        self.arvore.column("Nome", width=150)
        self.arvore.column("E-mail", width=120)
        self.arvore.column("Cidade", width=100)
        self.arvore.heading("ID", text="ID")
        self.arvore.heading("Nome", text="Nome")
        self.arvore.heading("E-mail", text="E-mail")
        self.arvore.heading("Cidade", text="Cidade")
        self.arvore['show'] = "headings"

        # dadosclientes = "select idcliente,nome, email, cidade from clientes"
        cursor.execute("select idcliente,nome, email, cidade from clientes")

        self.contador = 0  # Será útil para contar o número de clientes no cadastro

        for coluna in cursor:
            self.contador = self.contador + 1
            self.arvore.insert("", END, text="Clientes", values=coluna)
            self.arvore.pack()

        cursor.close()

        # Mensagens na aba3: Clientes cadastrados

        self.mensagem_fidelizados = Label(self.aba3_consultacliente, text="Quantidade de fidelizados:",
                                          font=("Verdana", 9))
        self.mensagem_fidelizados.place(x=25, y=250)
        self.qtde_fidelizados = Label(self.aba3_consultacliente, text="", font=("Verdana", 9))
        self.qtde_fidelizados['text'] = self.contador
        self.qtde_fidelizados.place(x=210, y=250)

        """Aba 4 Tapiocas disponíveis"""

        self.arvore2 = ttk.Treeview(self.aba4_consultatapioca)  # Montando a árvore
        self.arvore2.bind("<<TreeviewSelect>>", self.arvore_select)  # Associando uma função a um evento

        bancodedados = RepositorioGeral()
        cursor = bancodedados.con.cursor()

        filhosdaarvore2 = self.arvore2.get_children()

        for filho2 in filhosdaarvore2:
            self.arvore2.delete(filho2)

        self.arvore2['columns'] = ("ID Tapioca", "Nome da Tapioca")
        self.arvore2.column("ID Tapioca", width=80)
        self.arvore2.column("Nome da Tapioca", width=190)
        self.arvore2.heading("ID Tapioca", text="ID Tapioca")
        self.arvore2.heading("Nome da Tapioca", text="Nome da Tapioca")
        self.arvore2['show'] = "headings"

        cursor.execute("select idtapioca, nometapioca from tapiocas")

        for coluna2 in cursor:
            self.arvore2.insert("", END, text="Tapiocas", values=coluna2)
            self.arvore2.pack()

        cursor.close()

        """Aba 5 Sobre o Buy Tapiocas"""

        self.mensagem_aba5 = Label(self.aba5_sobre, text="Buy Tapiocas")
        self.mensagem_aba5['font'] = ("Verdana", "10", "bold")
        self.mensagem_aba5.place(x=125, y=20)

        self.mensagem2_aba5 = Label(self.aba5_sobre, text="v1.0 (32-bit)")
        self.mensagem2_aba5['font'] = ("Verdana", "9")
        self.mensagem2_aba5.place(x=125, y=40)

        self.mensagem3_aba5 = Label(self.aba5_sobre, text="Copyright 2021 TechLife S.A.")
        self.mensagem3_aba5['font'] = ("Verdana", "9")
        self.mensagem3_aba5.place(x=125, y=60)

        self.mensagem4_aba5 = Label(self.aba5_sobre, text="Desenvolvedores:")
        self.mensagem4_aba5['font'] = ("Verdana", "9")
        self.mensagem4_aba5.place(x=125, y=80)

        self.mensagem4_aba5 = Label(self.aba5_sobre, text="José Carlos dos Santos")
        self.mensagem4_aba5['font'] = ("Verdana", "9", "italic")
        self.mensagem4_aba5.place(x=125, y=100)

        self.imagem_aba5 = Label(self.aba5_sobre, image=filename)
        self.imagem_aba5.place(x=10, y=20, height=105, width=105)

    """ Métodos da classe Principal """

    def arvore_select(self, event):  # Função que será associada ao evento <<TreeviewSelect>>
        pass

    def gravarcliente(self):

        usuario = Clientes()  # Instância da classe Clientes

        usuario.nome = self.caixanome.get()  # Insere na variável o texto digitado na caixanome
        usuario.email = self.caixaemail.get()
        usuario.cep = self.caixacep.get()
        usuario.rua = self.caixarua.get()
        usuario.numero = self.caixanum.get()
        usuario.bairro = self.caixabairro.get()
        usuario.cidade = self.caixacidade.get()
        usuario.estado = self.caixaestado.get()

        # Status da gravação

        self.mensagem3_aba1['text'] = usuario.inserircliente()  # A gravação no banco é feita aqui

        # Excluindo dados digitados nas caixas

        self.caixanome.delete(0, END)
        self.caixaemail.delete(0, END)
        self.caixacep.delete(0, END)
        self.caixarua.delete(0, END)
        self.caixanum.delete(0, END)
        self.caixabairro.delete(0, END)
        self.caixacidade.delete(0, END)
        self.caixaestado.delete(0, END)

        self.atualizadados()

    def buscacliente(self):
        usuario = Clientes()

        idclientecaixa = self.caixaidcliente.get()

        self.mensagem3_aba1['text'] = usuario.consultacliente(idclientecaixa)  # A busca é feita aqui e atribuida nas
        # caixas das linhas abaixo (primeira executa a função, depois preenche as caixas).

        # Limpando caixas e obtendo valor do banco de dados para as caixas

        self.caixaidcliente.delete(0, END)
        self.caixaidcliente.insert(INSERT, usuario.idcliente)

        self.caixanome.delete(0, END)
        self.caixanome.insert(INSERT, usuario.nome)

        self.caixaemail.delete(0, END)
        self.caixaemail.insert(INSERT, usuario.email)

        self.caixacep.delete(0, END)
        self.caixacep.insert(INSERT, usuario.cep)

        self.caixacidade.delete(0, END)
        self.caixacidade.insert(INSERT, usuario.cidade)

        self.caixabairro.delete(0, END)
        self.caixabairro.insert(INSERT, usuario.bairro)

        self.caixaestado.delete(0, END)
        self.caixaestado.insert(INSERT, usuario.estado)

        self.caixanum.delete(0, END)
        self.caixanum.insert(INSERT, usuario.numero)

        self.caixarua.delete(0, END)
        self.caixarua.insert(INSERT, usuario.rua)

    def atualizacliente(self):
        usuario = Clientes()

        usuario.idcliente = self.caixaidcliente.get()
        usuario.nome = self.caixanome.get()
        usuario.email = self.caixaemail.get()
        usuario.cep = self.caixacep.get()
        usuario.rua = self.caixarua.get()
        usuario.numero = self.caixanum.get()
        usuario.bairro = self.caixabairro.get()
        usuario.cidade = self.caixacidade.get()
        usuario.estado = self.caixaestado.get()

        self.mensagem3_aba1['text'] = usuario.alteracliente()  # A alteração no banco é feita aqui

        self.atualizadados()

        # Excluindo dados digitados nas caixas

        self.caixanome.delete(0, END)
        self.caixaemail.delete(0, END)
        self.caixacep.delete(0, END)
        self.caixarua.delete(0, END)
        self.caixanum.delete(0, END)
        self.caixabairro.delete(0, END)
        self.caixacidade.delete(0, END)
        self.caixaestado.delete(0, END)

    def atualizadados(self):

        # Clientes

        self.arvore.bind("<<TreeviewSelect>>", self.arvore_select)  # Associando uma função a um evento

        bancodedados = RepositorioGeral()
        cursor = bancodedados.con.cursor()

        filhosdaarvores = self.arvore.get_children()
        for filho in filhosdaarvores:
            self.arvore.delete(filho)

        self.arvore['columns'] = ("ID", "Nome", "E-mail", "Cidade")
        self.arvore.column("ID", width=30)
        self.arvore.column("Nome", width=150)
        self.arvore.column("E-mail", width=120)
        self.arvore.column("Cidade", width=100)
        self.arvore.heading("ID", text="ID")
        self.arvore.heading("Nome", text="Nome")
        self.arvore.heading("E-mail", text="E-mail")
        self.arvore.heading("Cidade", text="Cidade")
        self.arvore['show'] = "headings"

        dadosclientes = "select idcliente,nome, email, cidade from clientes"
        cursor.execute(dadosclientes)

        self.contador = 0  # Será útil para contar o número de clientes no cadastro

        for coluna in cursor:
            self.contador = self.contador + 1
            self.arvore.insert("", END, text="Clientes", values=coluna)
            self.arvore.pack()

        cursor.close()

        # Tapiocas

        self.arvore2.bind("<<TreeviewSelect>>", self.arvore_select)  # Associando uma função a um evento

        bancodedados = RepositorioGeral()
        cursor2 = bancodedados.con.cursor()

        filhosdaarvore2 = self.arvore2.get_children()

        for filho2 in filhosdaarvore2:
            self.arvore2.delete(filho2)

        self.arvore2['columns'] = ("ID Tapioca", "Nome da Tapioca")
        self.arvore2.column("ID Tapioca", width=80)
        self.arvore2.column("Nome da Tapioca", width=190)
        self.arvore2.heading("ID Tapioca", text="ID Tapioca")
        self.arvore2.heading("Nome da Tapioca", text="Nome da Tapioca")
        self.arvore2['show'] = "headings"

        cursor2.execute("select idtapioca, nometapioca from tapiocas")

        for coluna2 in cursor2:
            self.arvore2.insert("", END, text="Tapiocas", values=coluna2)
            self.arvore2.pack()

        cursor2.close()

        # Mensagens na aba3: Clientes cadastrados

        self.mensagem_fidelizados = Label(self.aba3_consultacliente, text="Quantidade de fidelizados:",
                                          font=("Verdana", 9))
        self.mensagem_fidelizados.place(x=25, y=250)
        self.qtde_fidelizados = Label(self.aba3_consultacliente, text="", font=("Verdana", 9))
        self.qtde_fidelizados['text'] = self.contador
        self.qtde_fidelizados.place(x=210, y=250)

    def apagacliente(self):
        usuario = Clientes()

        usuario.idcliente = self.caixaidcliente.get()

        self.mensagem3_aba1['text'] = usuario.removecliente()  # Remoção feita aqui

        # Excluindo dados digitados nas caixas

        self.caixanome.delete(0, END)
        self.caixaemail.delete(0, END)
        self.caixacep.delete(0, END)
        self.caixarua.delete(0, END)
        self.caixanum.delete(0, END)
        self.caixabairro.delete(0, END)
        self.caixacidade.delete(0, END)
        self.caixaestado.delete(0, END)

        self.atualizadados()

    def gravartapioca(self):

        tapioca = Tapiocas()

        tapioca.nometapioca = self.caixanometapioca.get()

        # Status e ativação do método da classe Tapiocas()
        self.mensagem2_aba2['text'] = tapioca.inserirtapioca()

        # Removendo dados das caixas
        self.caixanometapioca.delete(0, END)

        self.atualizadados()

    def buscatapioca(self):

        tapioca = Tapiocas()

        idtapiocacaixa = self.caixaidtapioca.get()

        self.mensagem2_aba2['text'] = tapioca.consultatapioca(idtapiocacaixa)

        # Limpando e obtendo valores paras as caixas

        self.caixaidtapioca.delete(0, END)
        self.caixaidtapioca.insert(INSERT, tapioca.idtapioca)

        self.caixanometapioca.delete(0, END)
        self.caixanometapioca.insert(INSERT, tapioca.nometapioca)

    def atualizatapioca(self):

        tapioca = Tapiocas()

        tapioca.idtapioca = self.caixaidtapioca.get()
        tapioca.nometapioca = self.caixanometapioca.get()

        self.mensagem2_aba2['text'] = tapioca.alteratapioca()

        self.atualizadados()

        # Removendo dados das caixas

        self.caixanometapioca.delete(0, END)

    def apagatapioca(self):

        tapioca = Tapiocas()

        tapioca.idtapioca = self.caixaidtapioca.get()

        self.mensagem2_aba2['text'] = tapioca.removetapioca()

        # Removendo dados das caixas

        self.caixaidtapioca.delete(0, END)
        self.caixanometapioca.delete(0, END)

        self.atualizadados()


win = Tk()
imagem = Image.open("logo_size.png")
filename = ImageTk.PhotoImage(imagem)
Principal(win)
win.title('Buy Tapiocas')
win.mainloop()  # Event loop: permite a visualização da interface
