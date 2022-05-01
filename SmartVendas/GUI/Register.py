from email.mime import image
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# from ScreenValidation import screenMain


def registerForm(root, Toggle):

    frameRegister = Frame(root, bg="white")
    frameRegister.place(x=100, y=40, width=700, height=400) # Essa tela branca cobre os comandos de Login (não foi possível destruir em Logintest o que depende de root)

    Button(frameRegister, text="Login", font=("times new roman", 20, "bold"), bg="white", fg="red", borderwidth=0, cursor="hand2", command=Toggle).place(x=500, y=100)
        
    photo = PhotoImage(file="images/mascote.png")
    label = Label(frameRegister, width=300, height=400, image=photo)
    label.place(x=0, y=0)
    label.image = photo # DEU CERTO!!!!!!!!!!!!!!!!!!!!!!!!  (Mantém a referência)
        

# if __name__ == "__main__":
    # RegisterForm()