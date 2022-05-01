from tkinter import *
from tkinter import messagebox
from Logintest import loginForm
from PIL import Image, ImageTk
from Register import registerForm


root = Tk()


def screenMain():

    # global frameLogin, frameLogo, frameImageRegister

    root.title("Login Window - SmartVendas")
    root.configure(background="blue")
    root.geometry("900x500")
    root.iconbitmap("images/venda1.ico")
    root.resizable(False, False)

    # ============= Imagem de Fundo ==================================
    backGroundImage = PhotoImage(file="images/background8.png")
    Label(root, image=backGroundImage).place(x=0, y=0)

        # Textos devem vir depois da imagem de fundo (depois do código acima)

    Label(root, text="Version 1.0", font=("times new roman", 9), fg="white", bg="#8CD8EF").place(x=835, y=460)

    # ==================== Chamada de Métodos ========================    
    loginForm(root, ToggleToRegister)
    # registerForm(root, ToggleToLogin)

    # ============= Barra de menus ===================================
    menubar = Menu(root)
    file = Menu(root, tearoff=False)
    file.add_command(label="Register", command=ToggleToRegister)
    file.add_separator()
    file.add_command(label="Exit", command=exitLogin)
    menubar.add_cascade(label="File", menu=file)

    file2 = Menu(root, tearoff=False)
    file2.add_command(label="Version 1.0")
    menubar.add_cascade(label="About", menu=file2)

    root.config(menu=menubar)

    # ==================== Janela Principal ========================
    root.mainloop()

def exitLogin():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def ToggleToRegister(event=None):  # Faz a mudança para a tela de Registro
    registerForm(root, ToggleToLogin)

def ToggleToLogin(event=None):   # A aplicação reinicia a tela principal após clicar em 'Login'
    screenMain()
    

screenMain()
