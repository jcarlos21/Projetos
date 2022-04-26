from abc import abstractmethod
# @abstractmethod

class Person:
    def __init__(self, name, gender, dateBirthday, address, zipCode, city, state, country):
        self.name = name
        self.gender = gender
        self.dateBirthday = dateBirthday
        self.address = address
        self.zipCode = zipCode
        self.city = city
        self.state = state
        self.country = country
        
    def insertDatabase(self):
        # code implementation to insert on database
        pass

class Employee (Person):
    def __init__(self, dateAdmission, enrollment):
        self.dateAdmission = dateAdmission
        self.enrollment = enrollment

    def insertDatabase(self):
        # code implementation + method insertDatabase of the class Person to insert on database
        pass

class Management (Employee):
    def __init__(self, numberCRA):
        self.numberCRA = numberCRA
    
    def insertDatabase(self):
        # code implementation + method insertDatabase of the class Person and Employee to insert on database
        pass

class Seller (Employee):
    def __init__(self, departament):
        self.departament = departament
    
    def insertDatabase(self):
        # code implementation + method insertDatabase of the class Person and Employee to insert on database
        pass