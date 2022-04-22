import platform
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk
from DataBase import *


class RegisterUser(Tk):
    def __int__(self):
        pass

    def RegisterMain(self):

        self.geometry("700x500")
        self.resizable(False, False)
        Tk.title(self, "Histórico de Vendas 1.0")

        # Labels:______________________________________________________________________________________________________

        self.backGround = PhotoImage(file="images/background4.png")
        self.backGroundLabel = Label(self, image=self.backGround)
        self.backGroundLabel.pack()

        self.canvas = Canvas(self, width=550, height=400)
        self.canvas.place(x=75, y=25)

        self.title = Label(text="Registration", font="Arial 18")
        self.title.place(x=85, y=35)

        self.title = Label(text="Full Name (*)", font="Arial 10")
        self.title.place(x=150, y=85)

        self.title = Label(text="E-mail (*)", font="Arial 10")
        self.title.place(x=150, y=115)

        self.title = Label(text="Nickname", font="Arial 10")
        self.title.place(x=150, y=145)

        self.title = Label(text="Password", font="Arial 10")
        self.title.place(x=150, y=175)

        self.title = Label(text="Address", font="Arial 10")
        self.title.place(x=150, y=205)

        self.title = Label(text="City", font="Arial 10")
        self.title.place(x=150, y=235)

        self.title = Label(text="Zip", font="Arial 10")
        self.title.place(x=150, y=265)

        self.title = Label(text="State", font="Arial 10")
        self.title.place(x=150, y=295)

        self.title = Label(text="Country", font="Arial 10")
        self.title.place(x=150, y=325)

        self.title = Label(self, text="Version 1.0", font="Arial 7", fg="white", background="#000000")
        self.title.place(x=645, y=485)

        # Buttons:_____________________________________________________________________________________________________

        self.buttonExit = Button(text="Exit", font="Arial 9", height=1, bg="white", command=self.quit, border=0)
        self.buttonExit["width"] = 8
        self.buttonExit["height"] = 1
        self.buttonExit.place(x=555, y=395)

        # Botão para voltar para a página de Login:
        # https://www.delftstack.com/howto/python-tkinter/how-to-switch-frames-in-tkinter/

        # Entries:_____________________________________________________________________________________________________

        self.entryName = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryName.place(x=250, y=87)

        self.entryEmail = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryEmail.place(x=250, y=117)

        self.entryNick = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)  # Somou 30 a y
        self.entryNick.place(x=250, y=147)

        self.entryPass = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryPass.place(x=250, y=177)

        self.entryAddress = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryAddress.place(x=250, y=207)

        self.entryCity = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryCity.place(x=250, y=237)


class Login(RegisterUser):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(False, False)
        Tk.title(self, "Histórico de Vendas 1.0")

    def openfile(self):
        self.openfile = filedialog.askopenfilename()

    def BarSuperior(self):
        """
        Font: https://pythonguides.com/python-tkinter-menu-bar/
        """
        self.menubar = Menu()
        self.file = Menu(tearoff=False)
        # self.file.add_command(label="New")
        # self.file.add_command(label="Open", command=self.openfile)
        # self.file.add_command(label="Register", command=self.RegisterMain)
        # self.file.add_command(label="Save")
        # self.file.add_command(label="Save as")
        self.file.add_separator()
        self.file.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.file)

        self.config(menu=self.menubar)  # Dever vir no final de todos os menus

    def Label(self):  # O Label trata dos textos na janela
        self.backGroundImage = PhotoImage(file="images/background5.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        self.canvas = Canvas(self, width=400, height=350, highlightcolor="blue")
        self.canvas.place(x=150, y=60)  # 700 = 150 + 400 + 150

        self.title = Label(self, text="Sign In", font="Arial 30")
        self.title.place(x=290, y=80)

        self.title = Label(self, text="Username:", font="8")
        # self.title["font"] = ("Verdana", 8) outra forma de inserir a fonte
        self.title.place(x=200, y=170)

        self.title = Label(self, text="Password:", font="8")
        self.title.place(x=200, y=220)

        self.title = Label(self, text="Ainda não é registrado?", font="Arial 9")
        self.title.place(x=280, y=350)

        self.dados = platform.platform()  # Coleta informações do sistema e gera uma string
        self.title = Label(self, text="Version 1.0", font="Arial 7", fg="white", background="#000000")
        self.title.place(x=645, y=485)
        # self.wm_attributes('-transparentcolor', '#ab23ff')

    def Entry(self):
        self.userName = Text(self, borderwidth=0, highlightthickness=0, width=25, height=1)
        self.userName.place(x=290, y=173)

        self.Password = Entry(self, borderwidth=0, show="*", highlightthickness=0)
        self.Password.place(x=290, y=223, width=202, height=18)

    def Buttons(self):
        # self.loginButtonImage = PhotoImage(file="login_1.png")
        # self.loginButton = Button(self, image=self.loginButtonImage, command=self.LoginTest, border=0)

        self.loginButton = Button(self, text="Enter", font="Arial 9", bg="lightgray", border=0)
        # self.loginButton["font"] = ("Arial", "9")
        self.loginButton["width"] = 8
        self.loginButton["height"] = 1
        self.loginButton["command"] = self.LoginTest
        self.loginButton.place(x=430, y=255)

        self.registerButton = Button(self, text="Register", height=1, bg="white", command=self.ScreenRegister, border=0)
        self.registerButton["font"] = ("Arial", "9")
        self.registerButton["width"] = 8
        self.registerButton.place(x=320, y=380)

    def LoginTest(self):

        print("Deve ser gerado um comando aqui.")
        # Crie uma outra classe para registro

    def ScreenRegister(self):
        return self.RegisterMain()


if __name__ == "__main__":
    # while True:
        Login = Login()
        Login.Label()
        Login.Entry()
        Login.Buttons()
        Login.BarSuperior()
        # Aqui deve existir uma função que retorna verdadeiro se o login deu certo, dai vc para a execução (break)
        Login.mainloop()

    # Use um while para executar o código acima. Se o login retornar verdadeiro vc para a execução do while.

# imagem = Image.open("background1.jpg")
# filename = ImageTk.PhotoImage(imagem)
