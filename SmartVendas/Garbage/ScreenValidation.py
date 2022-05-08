from tkinter import *
from tkinter import messagebox
import os, sys
sys.path.insert(0, os.getcwd())
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

# from ..InterfaceGraphics import Login
# from PIL import Image, ImageTk
# from ..InterfaceGraphics import Register

import InterfaceGraphics.Login as Login
import InterfaceGraphics.Register as Register

root = Tk()


def screenMain():

    # global frameLogin, frameLogo, frameImageRegister (Linha não necessária)

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
    Login.loginForm(root, ToggleToRegister)
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
    root.mainloop()  # Se você tirar essa linha o programa não funcionará

def exitLogin():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def ToggleToRegister(event=None):  # Faz a mudança para a tela de Registro
    Register.registerForm(root, ToggleToLogin)

def ToggleToLogin(event=None):   # A aplicação reinicia a tela principal após clicar em 'Login'
    screenMain()
    

screenMain()