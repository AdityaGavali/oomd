from enums import *

class MenuItem:
    def __init__(self, id, title, description, price):
        self.__menu_item_id = id
        self.__title = title
        self.__description = description
        self.__price = price
    def get_menu_item_id(self):
        return self.get_menu_item_id
    def update_price(self, price):
        self.__price = price
        
    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price
    def __str__(self):
        return f"ID: {self.__menu_item_id}, Title: {self.__title}, Description: {self.__description}, Price: {self.__price}"


class MenuSection:
    def __init__(self, id, title, description):
        self.__menu_section_id = id
        self.__title = title
        self.__description = description
        self.__menu_items = []
    def get_menu_section_id(self):
        return self.get_menu_section_id
    def add_menu_item(self, menu_item):
        self.__menu_items.append(menu_item)

    def get_menu_items(self):
        return self.__menu_items

    def get_title(self):
        return self.__title    

    def __str__(self):
        menu_items_str = "\n".join(str(item) for item in self.__menu_items)
        return f"ID: {self.__menu_section_id}, Title: {self.__title}, Description: {self.__description}\n{menu_items_str}"


class Menu:
    def __init__(self, id, title, description):
        self.__menu_id = id
        self.__title = title
        self.__description = description
        self.__menu_sections = []
    def get_menu_id(self):
        return self.__menu_id
    def add_menu_section(self, menu_section):
        self.__menu_sections.append(menu_section)
    def get_title(self):
        return self.__title
    def get_menu_sections(self):
        return self.__menu_sections
    def __str__(self):
        menu_sections_str = "\n".join(str(section) for section in self.__menu_sections)
        return f"ID: {self.__menu_id}, Title: {self.__title}, Description: {self.__description}\n{menu_sections_str}"

