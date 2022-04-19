import mysql.connector


class Banco:
    def __init__(self):  # Creating a connection with the database
        self.mydatabase = mysql.connector.connect(
            host="localhost",
            user="root",
            password="32648978",
            database="myfirstDB"
        )
        self.mycursor = self.mydatabase.cursor()

    def createDB(self):  # It's must one of the first things.
        try:
            self.mydatabase = mysql.connector.connect(
                host="localhost",
                user="root",
                password="32648978"
            )
            self.mycursor = self.mydatabase.cursor()  # It's need to create a new cursor again because here there is a
            # new method!!!
            self.mycursor.execute("CREATE DATABASE myfirstDB")  # Database was already created!!!
            print('Banco de dados criado com sucesso!')
        except mysql.connector.errors.DatabaseError:
            return 'Banco de dados já existe!'

    def showsDB(self):  # Show databases if them was already created.
        self.mycursor = self.mydatabase.cursor()
        self.mycursor.execute("SHOW DATABASES")
        for x in self.mycursor:
            print(x)

    def createTablesUsers(self):
        pass

    def createTableFuncionario(self):
        pass

    def createTableStatus(self):
        pass


if __name__ == "__main__":
    Banco().showsDB()
