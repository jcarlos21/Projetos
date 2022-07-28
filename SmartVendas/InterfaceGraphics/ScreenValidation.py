from tkinter import *
from tkinter import messagebox
from Login import loginForm
from Register import registerForm


class ScreenMain:
    def __init__(self, root):
        # global frameLogin, frameLogo, frameImageRegister.
        self.root = root
        self.root.title("Login Window - SmartVendas")
        self.root.configure(background="blue")
        self.root.geometry("900x500")
        self.root.iconbitmap("images/venda1.ico")
        self.root.resizable(False, False)

        # ============= Imagem de Fundo ==================================
        self.backGroundImage = PhotoImage(file="images/background8.png")
        Label(root, image=self.backGroundImage).place(x=0, y=0)

        # Label(root, text="Version 1.0", font=("times new roman", 9), fg="white", bg="#8CD8EF").place(x=835, y=460) # version

        # ==================== Chamada de Métodos ========================    
        loginForm(root, self.ToggleToRegister)
        # registerForm(root, ToggleToLogin)

        # ============= Barra de menus ===================================
        self.menubar = Menu(root)
        self.file = Menu(root, tearoff=False)
        self.file.add_command(label="Register", command=self.ToggleToRegister)
        self.file.add_separator()
        self.file.add_command(label="Exit", command=self.exitLogin)
        self.menubar.add_cascade(label="File", menu=self.file)

        self.file2 = Menu(root, tearoff=False)
        self.file2.add_command(label="Version 1.0")
        self.menubar.add_cascade(label="About", menu=self.file2)

        self.root.config(menu=self.menubar)

    # ==================== Funções Específicas ========================
        
    def exitLogin(self):
        self.result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if self.result == 'yes':
            self.root.destroy()
            exit()

    def ToggleToRegister(self, event=None):  # Faz a mudança para a tela de Registro
        registerForm(self.root, self.ToggleToLogin)

    def ToggleToLogin(event=None):   # A aplicação reinicia a tela principal após clicar em 'Login'.
        ScreenMain(root)
        root.mainloop()


root = Tk()
obj = ScreenMain(root)

if __name__ == "__main__":
    root.mainloop()