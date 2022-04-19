import platform
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk
from DataBase import *


# root = Tk()
# root.title("Python: Simple Inventory System")


class Login(Tk):
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
        self.file.add_command(label="New")
        self.file.add_command(label="Open", command=self.openfile)
        self.file.add_command(label="Register", command=self.LoginTest)
        self.file.add_command(label="Save")
        self.file.add_command(label="Save as")
        self.file.add_separator()
        self.file.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.file, font="Arial 15")

        self.config(menu=self.menubar)  # Dever vir no final de todos os menus

    def Label(self):  # O Label trata dos textos na janela
        self.backGroundImage = PhotoImage(file="background5.png")
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

        self.registerButton = Button(self, text="Register", height=1, bg="white", command=self.LoginTest, border=0)
        self.registerButton["font"] = ("Arial", "9")
        self.registerButton["width"] = 8
        self.registerButton.place(x=320, y=380)

    def LoginTest(self):
        print("Deve ser gerado um comando aqui.")
        # Crie uma outra classe para registro


if __name__ == "__main__":
    Login = Login()
    Login.Label()
    Login.Entry()
    Login.Buttons()
    Login.BarSuperior()
    Login.mainloop()

# imagem = Image.open("background1.jpg")
# filename = ImageTk.PhotoImage(imagem)
