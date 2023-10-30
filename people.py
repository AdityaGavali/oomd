from abc import ABC
from datetime import datetime
from constants import *



class Account:
    def __init__(self, id, password, address, status=AccountStatus.Active):
        self.__id = id
        self.__password = password
        self.__address = address
        self.__status = status

    def reset_password(self,new_pas):
        self.__password = new_pas


class Person(ABC):
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone


class Employee(ABC):
    def __init__(self, id, account, name, email, phone):
        super().__init__(name, email, phone)
        self.__employee_id = id
        self.__date_joined = datetime.date.today()
        self.__account = account


class Receptionist(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)

    def create_reservation(self):
        None

    def search_customer(self, name):
        None


class Manager(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)

    def add_employee(self):
        None


class Chef(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)

    def take_order(self):
        None

