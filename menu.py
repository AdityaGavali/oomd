# class MenuItem:
#     def __init__(self, id, title, description, price):
#         self.__menu_item_id = id
#         self.__title = title
#         self.__description = description
#         self.__price = price

#     def update_price(self, price):
#         self.__price = price


# class MenuSection:
#     def __init__(self, id, title, description):
#         self.__menu_section_id = id
#         self.__title = title
#         self.__description = description
#         self.__menu_items = []

#     def add_menu_item(self, menu_item):
#         self.__menu_items.append(menu_item)


# class Menu:
#     def __init__(self, id, title, description):
#         self.__menu_id = id
#         self.__title = title
#         self.__description = description
#         self.__menu_sections = []

#     def add_menu_section(self, menu_section):
#         self.__menu_sections.append(menu_section)
   
#     def print(self):
#         for i in self.__menu_sections:
#          print(i, end = ' ')

class MenuItem:
    def __init__(self, id, title, description, price):
        self.__menu_item_id = id
        self.__title = title
        self.__description = description
        self.__price = price

    def update_price(self, price):
        self.__price = price

    def __str__(self):
        return f"ID: {self.__menu_item_id}, Title: {self.__title}, Description: {self.__description}, Price: {self.__price}"


class MenuSection:
    def __init__(self, id, title, description):
        self.__menu_section_id = id
        self.__title = title
        self.__description = description
        self.__menu_items = []

    def add_menu_item(self, menu_item):
        self.__menu_items.append(menu_item)

    def __str__(self):
        menu_items_str = "\n".join(str(item) for item in self.__menu_items)
        return f"ID: {self.__menu_section_id}, Title: {self.__title}, Description: {self.__description}\n{menu_items_str}"


class Menu:
    def __init__(self, id, title, description):
        self.__menu_id = id
        self.__title = title
        self.__description = description
        self.__menu_sections = []

    def add_menu_section(self, menu_section):
        self.__menu_sections.append(menu_section)

    def __str__(self):
        menu_sections_str = "\n".join(str(section) for section in self.__menu_sections)
        return f"ID: {self.__menu_id}, Title: {self.__title}, Description: {self.__description}\n{menu_sections_str}"


# Example usage
menu_item1 = MenuItem(1, "Burger", "Classic beef burger", 9.99)
menu_item2 = MenuItem(2, "Pizza", "Margherita pizza", 12.99)

menu_section1 = MenuSection(1, "Main Dishes", "Delicious main dishes")
menu_section1.add_menu_item(menu_item1)
menu_section1.add_menu_item(menu_item2)

menu_item3 = MenuItem(3, "Salad", "Fresh garden salad", 6.99)
menu_item4 = MenuItem(4, "Dessert", "Chocolate brownie", 5.99)

menu_section2 = MenuSection(2, "Sides and Desserts", "Tasty sides and desserts")
menu_section2.add_menu_item(menu_item3)
menu_section2.add_menu_item(menu_item4)

menu = Menu(1, "Main Menu", "Our delightful menu")
menu.add_menu_section(menu_section1)
menu.add_menu_section(menu_section2)

print("Menu Information:")
print(menu)
