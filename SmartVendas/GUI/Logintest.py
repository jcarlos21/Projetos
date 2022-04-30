from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# root = Tk()

def loginForm(root, Toggle):

    frameLogin = Frame(root, bg="white")
    frameLogin.place(x=200, y=60, width=600, height=380)

    # ============= Logo da empresa ===================================
    # imageLogoBusiness = PhotoImage(file="images/logo.png")
    # Label(frameLogo, image=imageLogoBusiness).place(x=0, y=0, width=200, height=300)  # Não funciona a partir daqui

    Label(frameLogin, text="SIGN IN", font=("times new roman", 20, "bold"), bg="white", fg="#016AFB").place(x=150, y=50)

    # Button(frameLogin, text="Registro", font=("times new roman", 20, "bold"), bg="white", fg="blue", borderwidth=0, cursor="hand2", command=Toggle).place(x=150, y=100)

    # ============= Textos, botões e entradas da Tela de Login =======
    Label(frameLogin, text="SIGN IN", font=("times new roman", 20, "bold"), bg="white", fg="#016AFB").place(x=150, y=50)

    Label(frameLogin, text="User Name or E-mail Address", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=150, y=120)
    Entry(frameLogin, font=("times new roman", 15), bg="lightgray").place(x=150, y=150, width=350)

    Label(frameLogin, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=150, y=200)
    Entry(frameLogin, font=("times new roman", 15), bg="lightgray").place(x=150, y=230, width=350)

    registerAccountButton = Button(frameLogin, text="No account? Register here.", font=("times new roman", 10), bg="white", fg="blue", cursor="hand2")
    registerAccountButton["borderwidth"] = 0
    registerAccountButton["command"] = Toggle
    registerAccountButton.place(x=150, y=260)
    # registerAccountButton.bind("<Button-1>", Toggle)  # Alternancia para o RegisterForm

    buttonLogin = Button(frameLogin, text="Login", font=("times new roman", 11), bg="red", fg="white", cursor="hand2", width=12, height=1)
    buttonLogin["command"] = mensagemLogin
    buttonLogin.place(x=150, y=310)

def mensagemLogin():
        teste = True
        if teste:
            messagebox.showinfo("SmartVendas Version 1.0", "Login efetuado com sucesso!")
        else:
            messagebox.showerror("SmartVendas Version 1.0", "Falha de Login! Usuário ou senha incorretos!")


