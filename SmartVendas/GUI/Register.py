from email.mime import image
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# from ScreenValidation import screenMain

# root = screenMain()

def registerForm(root, Toggle):

        frameRegister = Frame(root, bg="white")
        frameRegister.place(x=50, y=40, width=750, height=400) # Essa tela branca cobre os comandos de Login (não foi possível destruir em Logintest o que depende de root)

        # Button(root, text="Login", font=("times new roman", 20, "bold"), bg="white", fg="blue", borderwidth=0, cursor="hand2", command=Toggle).place(x=150, y=100)

        # imageLogin = PhotoImage(file="images/mascote.png")
        # Label(root, image=imageLogin).place(x=0, y=40, width=100, height=400)  # Não funciona a partir daqui

        Button(frameRegister, text="Login", font=("times new roman", 20, "bold"), bg="white", fg="red", borderwidth=0, cursor="hand2", command=Toggle).place(x=500, y=100)
        
        photo = PhotoImage(file="images/mascote.png")

        label = Label(frameRegister, image=photo).place(x=0, y=40, width=300, height=400)  # Não funciona a partir daqui
        label.image = photo # DEU CERTO!!!!!!!!!!!!!!!!!!!!!!!!  (Mantém a referência)
        # label.pack(x=0, y=40, width=100, height=400)

        


# if __name__ == "__main__":
    # RegisterForm()