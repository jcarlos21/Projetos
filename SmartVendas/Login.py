from tkinter import *
from PIL import Image, ImageTk

from awesometkinter import *
import awesometkinter as atk

class Login:  # O acesso para a área de registro será feito com um link para Register (Aqui deve ser herdada a classe Register)
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window - SmartVendas")
        self.root.configure(background="white")
        self.root.geometry("1100x625")
        self.root.resizable(False, False)

        # ============= Imagem de Fundo ==================================
        self.backGroundImage = PhotoImage(file="images/background8.png")
        self.backGroundImageLabel = Label(self.root, image=self.backGroundImage).place(x=0, y=0)

        # ============= Frames (ou Containers) de Login ==================
        frameLogin = Frame(self.root, bg="white")
        frameLogin.place(x=300, y=72.5, width=700, height=480)

        # ============= Imagem de Cima ===================================
        self.imageOverBackGround = PhotoImage(file="images/logo.png")
        self.imageOverBackGroundLabel = Label(self.root, image=self.imageOverBackGround).place(x=150, y=112.5, width=300, height=400)

        # ============= Textos e Entradas da Tela de Login ==========================
        self.title = Label(frameLogin, text="SIGN IN", font=("times new roman", 25, "bold"), bg="white", fg="#016AFB").place(x=200, y=50)

        self.userNameEmail = Label(frameLogin, text="User Name or E-mail Address", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=200, y=120)
        self.userNameEmailEntry = Entry(frameLogin, font=("times new roman", 15), bg="lightgray").place(x=200, y=150, width=350)

        self.password = Label(frameLogin, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=200, y=200)
        self.passwordEntry = Entry(frameLogin, font=("times new roman", 15), bg="lightgray").place(x=200, y=230, width=350)

        self.registerAccountButton = Button(frameLogin, text="No account? Register here.", font=("times new roman", 10), bg="white", fg="blue", cursor="hand2")
        self.registerAccountButton["borderwidth"] = 0
        self.registerAccountButton["command"] = self.root.quit
        self.registerAccountButton.place(x=200, y=280)

        # self.buttoLoginImage = PhotoImage(file="images/logo.png")
        self.buttonLogin = Button(frameLogin, text="Login", font=("times new roman", 15), bg="blue", fg="white", cursor="hand2", width=12, height=1)
        self.buttonLogin["command"] = self.root.quit
        self.buttonLogin.place(x=200, y=320)

        self.title = Label(self.root, text="Version 1.0", font=("times new roman", 9), fg="black", background="#8AD8EF")
        self.title.place(x=1030, y=600)

        # ============= Barra de menus ===============================================
        self.menubar = Menu(self.root)
        self.file = Menu(self.root, tearoff=False)
        self.file.add_separator()
        self.file.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.file)

        self.file2 = Menu(self.root, tearoff=False)
        self.file2.add_command(label="Version 1.0")
        self.menubar.add_cascade(label="Sobre", menu=self.file2)

        self.root.config(menu=self.menubar)


root = Tk()
obj = Login(root)

if __name__ == "__main__":
    root.mainloop()