from tkinter import *
from tkinter import messagebox
# from PIL import Image, ImageTk
# from Pessoas.People import Person
# from awesometkinter import *
# import awesometkinter as atk

class Login:  # O acesso para a área de registro será feito com um link para Register (Aqui deve ser herdada a classe Register)
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window - SmartVendas")
        self.root.configure(background="white")
        self.root.geometry("900x500")
        self.root.iconbitmap("images/venda1.ico")
        self.root.resizable(False, False)

        # ============= Imagem de Fundo ==================================
        self.backGroundImage = PhotoImage(file="images/background9.png")
        self.backGroundImageLabel = Label(self.root, image=self.backGroundImage).place(x=0, y=0)

        # ============= Frames (ou Containers) de Login ==================
        frameLogin = Frame(self.root, bg="white")
        frameLogin.place(x=200, y=60, width=600, height=380)

        # ============= Imagem de Cima ===================================
        self.imageOverBackGround = PhotoImage(file="images/logo.png")
        self.imageOverBackGroundLabel = Label(self.root, image=self.imageOverBackGround).place(x=100, y=100, width=200, height=300)

        # ============= Textos, botões e entradas da Tela de Login =======
        self.title = Label(frameLogin, text="SIGN IN", font=("times new roman", 20, "bold"), bg="white", fg="#016AFB").place(x=150, y=50)

        self.userNameEmail = Label(frameLogin, text="User Name or E-mail Address", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=150, y=120)
        self.userNameEmailEntry = Entry(frameLogin, font=("times new roman", 15), bg="lightgray").place(x=150, y=150, width=350)

        self.password = Label(frameLogin, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=150, y=200)
        self.passwordEntry = Entry(frameLogin, font=("times new roman", 15), bg="lightgray").place(x=150, y=230, width=350)

        self.registerAccountButton = Button(frameLogin, text="No account? Register here.", font=("times new roman", 10), bg="white", fg="blue", cursor="hand2")
        self.registerAccountButton["borderwidth"] = 0
        self.registerAccountButton["command"] = self.root.quit
        self.registerAccountButton.place(x=150, y=260)

        # self.buttoLoginImage = PhotoImage(file="images/logo.png")
        self.buttonLogin = Button(frameLogin, text="Login", font=("times new roman", 11), bg="red", fg="white", cursor="hand2", width=12, height=1)
        self.buttonLogin["command"] = self.mensagemLogin
        self.buttonLogin.place(x=150, y=310)

        self.title = Label(self.root, text="Version 1.0", font=("times new roman", 9), fg="black", background="#A9D7FB")
        self.title.place(x=835, y=475)

        # ============= Barra de menus ===================================
        self.menubar = Menu(self.root)
        self.file = Menu(self.root, tearoff=False)
        self.file.add_separator()
        self.file.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.file)

        self.file2 = Menu(self.root, tearoff=False)
        self.file2.add_command(label="Version 1.0")
        self.menubar.add_cascade(label="Sobre", menu=self.file2)

        self.root.config(menu=self.menubar)
    
    def verificaLogin(self, userName, passaword):
        # Verify the veracity of the informations of username and password with the database.
        # Verifica as informações no banco de dados por meio de um selec. Se o banco não encontrar a informação, será retornado um erro.
        if userName == "carlosowen75" and passaword == "1234":
            self.mensagemLogin(True)
        else:
            self.mensagemLogin(False)

        # pass

    def screenRegistration(self):
        # It should allow entry on the registration screen.
        # Permite a entrada no tela de registro
        self.Register
    
    # ============= Mensagens de confirmação de Login ================

    def mensagemLogin(self):
        self.teste = True
        if self.teste:
            messagebox.showinfo("SmartVendas Version 1.0", "Login efetuado com sucesso!")
        else:
            messagebox.showerror("SmartVendas Version 1.0", "Falha de Login! Usuário ou senha incorretos!")

root = Tk()
obj = Login(root)

if __name__ == "__main__":
    root.mainloop()