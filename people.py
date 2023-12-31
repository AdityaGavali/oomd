
from abc import ABC
from datetime import datetime
from enums import *
from reservation import Reservation
from  infrastructure import *
import uuid

class Account:
    def __init__(self, id, password, address, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__address = address
        self.__status = status

    def reset_password(self, new_password):
        self.__password = new_password

class Person(ABC):  # Ensure that Person inherits from ABC
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone

class Employee(Person, ABC):  # Inherit from Person and ABC
    def __init__(self, id, account, name, email, phone):
        super().__init__(name, email, phone)  # Call the __init__ method of the Person class
        self.__employee_id = id
        self.__date_joined = datetime.now()
        self.__account = account
    def get_employee_id(self):  # Added the getter method for employee_id
        return self.__employee_id
class Manager(Employee):
    def __init__(self, id, account, name, email, phone, is_admin=False):
        super().__init__(id, account, name, email, phone)
        self.__is_admin = is_admin
    def get_name(self):
        return self._Person__name
    def get_category(self):
        return "Manager"
    def is_admin(self):
        return self.__is_admin

    def add_employee(self, employee_list, new_employee):
        # Logic to add a new employee
        if self.is_admin():
            employee_list.append(new_employee)
            return employee_list
        else:
            print("Only admin can add new employees.")
            return employee_list
        

def generate_reservation_id():
  return str(uuid.uuid4())


class Receptionist(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)
    def get_name(self):
        return self._Person__name
    def get_category(self):
        return "Receptionist"
    def create_reservation(self, customer, people_count, notes, branch, table_chart, capacity, start_time):
        # Logic to create a reservation
        available_tables = branch.search_available_tables(capacity, start_time)

        if available_tables:
            reservation_id = generate_reservation_id()
            reservation = Reservation(reservation_id,people_count, notes, customer)
            selected_table = available_tables[0]
            reservation.add_table(selected_table)
            table_chart.update_table_status(selected_table.get_number(), TableStatus.RESERVED)
            branch.add_reservation(reservation)
            return reservation
        else:
            return None

    def view_table_chart(self, table_chart):
        table_chart.print_table_chart()        

class Chef(Employee):
    chef_count = 0
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)
        Chef.chef_count += 1
    def get_name(self):
        return self._Person__name
    def get_category(self):
        return "Chef"
    def take_order(self, order):
          if order.get_status() == OrderStatus.RECEIVED:
            # Process the order
            # Update the order status to indicate preparation
            order.update_status(OrderStatus.PREPARING)
            print("Chef {self.get_employee_id()} is preparing the order.")
          else:
            print("Chef can only take received orders.")
        
