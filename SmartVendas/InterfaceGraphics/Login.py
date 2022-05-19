from tkinter import *
from tkinter import messagebox
# from PIL import Image, ImageTk


def loginForm(root, Toggle):

    frameLogin = Frame(root, bg="white")
    frameLogin.place(x=200, y=60, width=600, height=380)

    # ============= Logo da empresa ===================================
    photo = PhotoImage(file="images/logo.png")
    label = Label(root, width=200, height=300, image=photo)
    label.place(x=100, y=100)
    label.image = photo

    photo2 = PhotoImage(file="images/cadeado.png")
    label2 = Label(frameLogin, width=90, height=90, image=photo2)
    label2.place(x=500, y=280)
    label2.image = photo2

    # ============= Textos, botões e entradas da Tela de Login =======
    Label(frameLogin, text="Sign In", font=("times new roman", 20, "bold"), bg="white", fg="#016AFB").place(x=150, y=50)

    Label(frameLogin, text="User Name or E-mail Address", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=150, y=120)
    Entry(frameLogin, font=("times new roman", 12), bg="lightgray").place(x=150, y=150, width=350)

    Label(frameLogin, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=150, y=200)
    Entry(frameLogin, font=("times new roman", 12), bg="lightgray", show="*").place(x=150, y=230, width=350)

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
