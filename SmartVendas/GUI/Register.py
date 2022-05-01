from email.mime import image
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
# from ScreenValidation import screenMain


def registerForm(root, Toggle):

    # ===================== Fundo branco ============================================================
    frameRegister = Frame(root, bg="white")
    frameRegister.place(x=50, y=40, width=800, height=400) # Essa tela branca cobre os comandos de Login (não foi possível destruir em Logintest o que depende de root)    

    # ============================= Imagem acima do fundo branco ==================================== 
    photo = PhotoImage(file="images/Jump.png")
    label = Label(frameRegister, width=300, height=400, image=photo)
    label.place(x=0, y=0)
    label.image = photo  # (Mantém a referência)

    # ============================ Botão para a tela de Login (acima da imagem) =====================
    toggleLogin = Button(frameRegister, text="Login", font=("times new roman", 17, "bold"), bg="blue", fg="white", borderwidth=3, cursor="hand2", command=Toggle)
    toggleLogin["width"] = 6
    toggleLogin["height"] = 1
    toggleLogin.place(x=100, y=340)

    # ============= Textos, botões e entradas da Tela de Registro ===================================
    Label(frameRegister, text="New User Registration", font=("times new roman", 20, "bold"), bg="white", fg="#016AFB").place(x=315, y=15)

    Label(frameRegister, text="Full Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=315, y=70)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=410, y=75, width=330)

    Label(frameRegister, text="E-mail", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=315, y=110)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=410, y=115, width=330)

    Label(frameRegister, text="Gender", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=315, y=150)

    escolha = StringVar()
    genderMale = Radiobutton(frameRegister, text='Male', value="Male", variable=escolha, bg="white")
    genderMale.place(x=410, y=155)

    genderFemale = Radiobutton(frameRegister, text='Female', value="Male", variable=escolha, bg="white")
    genderFemale.place(x=480, y=155)

    # genderChoose = ttk.Combobox(frameRegister, textvariable=escolha, width=12)
    # genderChoose['values'] = ['Male', 'Female']
    # genderChoose.pack()  # Não precisa disso aqui
    # genderChoose.set('Female')
    # genderChoose.grid(column=0, row=0, padx=410, pady=155)
    # genderChoose.current(0)

    Label(frameRegister, text="Zip Code", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=555, y=150)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=640, y=155, width=100)

    Label(frameRegister, text="Address", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=315, y=190)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=410, y=195, width=200)

    Label(frameRegister, text="Nº", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=615, y=190)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=650, y=195, width=90)

    Label(frameRegister, text="City", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=315, y=230)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=410, y=235, width=110)

    Label(frameRegister, text="State", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=530, y=230)
    # Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=590, y=235, width=150)

    stateChosen = StringVar()
    stateChoose = ttk.Combobox(frameRegister, textvariable=stateChosen, width=21)
    stateChoose['values'] = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás' 
        'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba','Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro','Rio Grande do Norte',
        'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo','Sergipe', 'Tocantins']
    stateChoose.grid(column=0, row=0, padx=590, pady=235)
    stateChoose.current(0)
    




# if __name__ == "__main__":
    # RegisterForm()