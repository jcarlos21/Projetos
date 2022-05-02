from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk


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
    genderFemale = Radiobutton(frameRegister, text='Female', value="Female", variable=escolha, bg="white")
    genderFemale.place(x=480, y=155)

        # Como obter o valor do Radion para gravar no banco: https://www.youtube.com/watch?v=SkMATionZTQ

    Label(frameRegister, text="Zip Code", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=555, y=150)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=640, y=155, width=100)

    Label(frameRegister, text="Address", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=315, y=190)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=410, y=195, width=200)

    Label(frameRegister, text="Nº", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=615, y=190)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=650, y=195, width=90)

    Label(frameRegister, text="City", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=315, y=230)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=410, y=235, width=110)

    Label(frameRegister, text="State", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=525, y=230)

    stateChosen = StringVar()
    stateChoose = ttk.Combobox(frameRegister, textvariable=stateChosen, width=21)
    stateChoose['values'] = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás' 
        'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba','Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro','Rio Grande do Norte',
        'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo','Sergipe', 'Tocantins']
    stateChoose.grid(column=0, row=0, padx=590, pady=235)
    stateChoose.current(0)

    Label(frameRegister, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=315, y=270)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray").place(x=410, y=275, width=120)
    
    Label(frameRegister, text="Occup.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=535, y=270)

    ocuppMRadio = IntVar()
    ocuppSRadio = IntVar()
    managerRadio = Checkbutton(frameRegister, text='Manager', variable=ocuppMRadio, onvalue=1, offvalue=0, bg="white")
    managerRadio.select()
    managerRadio.place(x=610, y=275)
    sellerRadio = Checkbutton(frameRegister, text='Seller', variable=ocuppSRadio, onvalue=1, offvalue=0, bg="white")
    sellerRadio.deselect()
    sellerRadio.place(x=685, y=275)

        # Veja em: https://www.youtube.com/watch?v=l6q2upwMOtQ

    Label(frameRegister, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=315, y=310)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray", show="*").place(x=410, y=315, width=110)

    Label(frameRegister, text="Re-Enter", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=525, y=310)
    Entry(frameRegister, font=("times new roman", 12), bg="lightgray", show="*").place(x=620, y=315, width=120)

