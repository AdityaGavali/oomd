from enums import *
class Kitchen:
    def __init__(self, name):
        self.__name = name
        self.__chefs = []

    def assign_chef(self, chef):
        self.__chefs.append(chef)


# class Branch:
#     def __init__(self, name, location, kitchen):
#         self.__name = name
#         self.__location = location
#         self.__kitchen = kitchen

class Branch:
    def __init__(self, name, location, kitchen):
        self.__name = name
        self.__location = location
        self.__kitchen = kitchen
        self.__tables = []  # Add a list to store tables
    def add_menu(self, menu):
        self.__menu = menu
    def add_table(self, table):
        self.__tables.append(table)

    def search_available_tables(self, capacity, start_time):
        # Return all tables with the given capacity and availability
        available_tables = []
        for table in self.__tables:
            if table.is_table_free() and table.get_capacity() >= capacity:
                available_tables.append(table)
        return available_tables

    def add_reservation(self, reservation):
        # Add logic to update table status when a reservation is made
        for table in reservation.get_tables():
            table.add_reservation(reservation)

class Restaurant:
    def __init__(self, name):
        self.__name = name
        self.__branches = []

    def add_branch(self, branch):
        self.__branches.append(branch)


class Table:
    def __init__(self, number, capacity, location_identifier):
        self.__number = number
        self.__capacity = capacity
        self.__location_identifier = location_identifier
        
    def is_table_free(self):
        return self.__status == TableStatus.FREE    

    def get_number(self):
        return self.__number
    def add_reservation(self, reservation):
        self.__status = TableStatus.RESERVED
        self.__seats.extend(reservation.get_table_seats())

    def get_capacity(self):
        return self.__capacity

    def get_location_identifier(self):
        return self.__location_identifier

# infrastructure.py
class TableChart:
    def __init__(self, id):
        self.__table_chart_id = id
        self.__table_chart_image = []

    def add_table(self, table):
        self.__table_chart_image.append(table)

    def print_table_chart(self):
        for table in self.__table_chart_image:
            print(f'Table Number: {table.get_number()}, Capacity: {table.get_capacity()}, Location: {table.get_location_identifier()}')



