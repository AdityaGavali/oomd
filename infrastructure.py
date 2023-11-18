import streamlit as st
from enums import *
class Kitchen:
    def __init__(self, name):
        self.__name = name
        self.__chefs = []

    def assign_chef(self, chef):
        self.__chefs.append(chef)

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

class TableChart:
    def __init__(self, id):
        self.__table_chart_id = id
        self.__table_chart_image = []
    # def update_table_status(self, table_number, new_status):
    #     if table_number in self.__tables:
    #         self.__tables[table_number].update_status(new_status)
    def update_table_status(self, table_number, new_status):
        for table in self.__table_chart_image:
            if table.get_number() == table_number:
                table.update_status(new_status)
                break

    def add_table(self, table):
        self.__table_chart_image.append(table)

    def print_table_chart(self):
        st.write("Table Chart:")
        for table in self.__table_chart_image:
            st.write(f'Table Number: {table.get_number()}, Capacity: {table.get_capacity()}, Status : {table.show_status()}, Location : {table.show_location()}')


    # def view_table_chart(self, table_chart):
    #     st.write("Table Chart:")
    #     for table in table_chart.get_table_chart_image():
    #         st.write(f'Table Number: {table.get_number()}, Capacity: {table.get_capacity()}, Location: {table.get_location_identifier()}')

