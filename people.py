
from abc import ABC
from datetime import datetime
from enums import *
from reservation import Reservation

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



# class Receptionist(Employee):
#     def __init__(self, id, account, name, email, phone):
#         super().__init__(id, account, name, email, phone)

#     def create_reservation(self):
#         # Logic to create a reservation
#         pass

#     def search_customer(self, name):
#         # Logic to search for a customer
#         pass


# class Manager(Employee):
#     def __init__(self, id, account, name, email, phone):
#         super().__init__(id, account, name, email, phone)

#     def add_employee(self):
#         # Logic to add a new employee
#         pass


# class Chef(Employee):
#     def __init__(self, id, account, name, email, phone):
#         super().__init__(id, account, name, email, phone)

#     def take_order(self):
#         # Logic for the chef to take an order
#         pass

class Receptionist(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)

    def create_reservation(self, customer, people_count, notes, branch, table_chart, capacity, start_time):
        # Logic to create a reservation
        available_tables = branch.search_available_tables(capacity, start_time)
        
        if available_tables:
            reservation = Reservation.create_reservation(people_count, notes, customer)
            selected_table = available_tables[0]  # Assume the first available table is selected
            reservation.add_table(selected_table)
            table_chart.update_table_status(selected_table.get_number(), ReservationStatus.RESERVED)
            branch.add_reservation(reservation)
            return reservation
        else:
            return None

    def search_customer(self, customers, name):
        # Logic to search for a customer
        matching_customers = [customer for customer in customers if name.lower() in customer.get_name().lower()]
        return matching_customers

    def view_table_chart(self, table_chart):
        table_chart.print_table_chart()

class Manager(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)

    def add_employee(self, employee_list, new_employee):
        # Logic to add a new employee
        employee_list.append(new_employee)
        return employee_list

class Chef(Employee):
    def __init__(self, id, account, name, email, phone):
        super().__init__(id, account, name, email, phone)

    def take_order(self, order):
          if order.get_status() == OrderStatus.RECEIVED:
            # Process the order
            # Update the order status to indicate preparation
            order.update_status(OrderStatus.PREPARING)
            print("Chef {self.get_employee_id()} is preparing the order.")
          else:
            print("Chef can only take received orders.")
        
