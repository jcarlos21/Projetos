import platform
from tkinter import *
from tkinter import filedialog


class RegisterUser(Tk):
    def __int__(self):
        pass

    def RegisterMain(self):

        self.geometry("700x500")
        self.resizable(False, False)
        Tk.title(self, "Histórico de Vendas 1.0")

        # Labels:______________________________________________________________________________________________________

        self.backGround = PhotoImage(file="images/background4.png")
        self.backGroundLabel = Label(self, image=self.backGround)
        self.backGroundLabel.pack()

        self.canvas = Canvas(self, width=550, height=400)
        self.canvas.place(x=75, y=25)

        self.title = Label(text="Registration", font="Arial 18")
        self.title.place(x=85, y=35)

        self.title = Label(text="Full Name (*)", font="Arial 10")
        self.title.place(x=150, y=85)

        self.title = Label(text="E-mail (*)", font="Arial 10")
        self.title.place(x=150, y=115)

        self.title = Label(text="Nickname", font="Arial 10")
        self.title.place(x=150, y=145)

        self.title = Label(text="Password", font="Arial 10")
        self.title.place(x=150, y=175)

        self.title = Label(text="Address", font="Arial 10")
        self.title.place(x=150, y=205)

        self.title = Label(text="City", font="Arial 10")
        self.title.place(x=150, y=235)

        self.title = Label(text="Zip", font="Arial 10")
        self.title.place(x=150, y=265)

        self.title = Label(text="State", font="Arial 10")
        self.title.place(x=150, y=295)

        self.title = Label(text="Country", font="Arial 10")
        self.title.place(x=150, y=325)

        self.title = Label(self, text="Version 1.0", font="Arial 7", fg="white", background="#1B4C5A")
        self.title.place(x=645, y=485)

        # Buttons:_____________________________________________________________________________________________________

        self.buttonExit = Button(text="Exit", font="Arial 9", height=1, bg="white", command=self.quit, border=0)
        self.buttonExit["width"] = 8
        self.buttonExit["height"] = 1
        self.buttonExit.place(x=555, y=395)

        # Botão para voltar para a página de Login:
        # https://www.delftstack.com/howto/python-tkinter/how-to-switch-frames-in-tkinter/

        # Entries:_____________________________________________________________________________________________________

        self.entryName = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryName.place(x=250, y=87)

        self.entryEmail = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryEmail.place(x=250, y=117)

        self.entryNick = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)  # Somou 30 a y
        self.entryNick.place(x=250, y=147)

        self.entryPass = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryPass.place(x=250, y=177)

        self.entryAddress = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryAddress.place(x=250, y=207)

        self.entryCity = Text(self, borderwidth=0, highlightthickness=0, width=35, height=1)
        self.entryCity.place(x=250, y=237)


if __name__ == "__main__":
    Register = RegisterUser()
    Register.RegisterMain()
