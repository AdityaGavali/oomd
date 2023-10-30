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


class TableChart:
    def __init__(self, id):
        self.__table_chart_id = id
        self.__table_chart_image = []
    def add_table_chart(self, table):
        self.__table_chart_image.append(table)
    def print(self):
        for i in self.__table_chart_image:
            print(i, end = ' ')

