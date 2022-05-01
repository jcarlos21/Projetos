from abc import abstractmethod
# @abstractmethod

class Person:
    def __init__(self, name, gender, dateBirthday, address, zipCode, city, state, country):
        self.name = name
        self.gender = gender
        # self.dateBirthday = dateBirthday
        self.address = address
        self.zipCode = zipCode
        self.city = city
        self.state = state
        # self.country = country
    
    def insertDatabase(self):
        # code implementation to insert on database
        pass

class Employee (Person):
    def __init__(self, dateAdmission, enrollmentNumber):
        self.dateAdmission = dateAdmission
        self.enrollmentNumber = enrollmentNumber

    def insertDatabase(self):
        # code implementation + method insertDatabase of the class Person to insert on database
        pass

class Manager (Employee):
    def __init__(self, departament):
        # self.numberCRA = numberCRA
        self.departament = departament
    
    def insertDatabase(self):
        # code implementation + method insertDatabase of the class Person and Employee to insert on database
        pass

class Seller (Employee):
    def __init__(self, departament):
        self.departament = departament
    
    def insertDatabase(self):
        # code implementation + method insertDatabase of the class Person and Employee to insert on database
        pass
