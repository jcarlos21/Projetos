from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog


class RegisterUser(Tk):
    def __int__(self):
        self.geometry("700x500")
        self.resizable(False, False)
        Tk.title(self, "Histórico de Vendas 1.0")

    def Label(self):
        self.backGround = PhotoImage(file="../images/background4.png")
        self.backGroundLabel = Label(self, image=self.backGround)
        self.backGroundLabel.place(x=2, y=2)

        self.canvas = Canvas(self, width=400, height=350, highlightcolor="blue")
        self.canvas.place(x=150, y=60)  # 700 = 150 + 400 + 150


if __name__ == "__main__":
    reg = RegisterUser()
    reg.Label()
    reg.mainloop()
