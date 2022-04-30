from People import Person


class Customers (Person):
    def __init__(self, codCustomer):
        self.codCustomer = codCustomer
        pass



cliente1 = Customers(1)
cliente1.name = "José Carlos"
cliente1.dateBirthday = "08/11/1991"

print(f"O nome do cliente é {cliente1.name}!")
