# class Kitchen:
#     def __init__(self, name):
#         self.__name = name
#         self.__chefs = []

#     def assign_chef(self, chef):
#         self.__chefs.append(chef)


# class Branch:
#     def __init__(self, name, location, kitchen):
#         self.__name = name
#         self.__location = location
#         self.__kitchen = kitchen

   


# class Restaurant:
#     def __init__(self, name):
#         self.__name = name
#         self.__branches = []

#     def add_branch(self, branch):
#         self.__branches.append(branch)


# class TableChart:
#     def __init__(self, id):
#         self.__table_chart_id = id
#         self.__table_chart_image = []
#     def add_table_chart(self, table):
#         self.__table_chart_image.append(table)
#     def print(self):
#         for i in self.__table_chart_image:
#             print(i, end = ' ')

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


class Restaurant:
    def __init__(self, name):
        self.__name = name
        self.__branches = []

    def add_branch(self, branch):
        self.__branches.append(branch)


class Table:
    def __init__(self, number, capacity):
        self.__number = number
        self.__capacity = capacity

    def get_number(self):
        return self.__number

    def get_capacity(self):
        return self.__capacity


class TableChart:
    def __init__(self, id):
        self.__table_chart_id = id
        self.__table_chart_image = []

    def add_table(self, table):
        self.__table_chart_image.append(table)

    def print_table_chart(self):
        for table in self.__table_chart_image:
            print(f'Table Number: {table.get_number()}, Capacity: {table.get_capacity()}')


# Example usage
kitchen1 = Kitchen("Main Kitchen")
chef1 = "Chef John"
kitchen1.assign_chef(chef1)

branch1 = Branch("Branch 1", "123 Main St", kitchen1)

restaurant = Restaurant("My Restaurant")
restaurant.add_branch(branch1)

table1 = Table(1, 4)
table2 = Table(2, 6)

table_chart = TableChart(1)
table_chart.add_table(table1)
table_chart.add_table(table2)

print("Restaurant Name:", restaurant._Restaurant__name)
print("Branch Name:", restaurant._Restaurant__branches[0]._Branch__name)
print("Kitchen Name:", restaurant._Restaurant__branches[0]._Branch__kitchen._Kitchen__name)

print("Table Chart for Branch 1:")
table_chart.print_table_chart()
