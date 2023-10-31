# from datetime import datetime


# class MealItem:
#     def __init__(self, id, quantity, menu_item):
#         self.__meal_item_id = id
#         self.__quantity = quantity
#         self.__menu_item = menu_item

#     def update_quantity(self, quantity):
#         self.__quantity = quantity


# class Meal:
#     def __init__(self, id, seat):
#         self.__meal_id = id
#         self.__seat = seat
#         self.__menu_items = []

#     def add_meal_item(self, meal_item):
#      self.__menu_items.append(meal_item)


# class Check():
#     def __init__(self):
#         None


# class Order:
#     def __init__(self, id, status, table, waiter, chef):
#         self.__order_id = id
#         self.__OrderStatus = status
#         self.__creation_time = datetime.now()

#         self.__meals = []
#         self.__table = table
#         self.__waiter = waiter
#         self.__chef = chef
#         self.__check = Check()

#     def add_meal(self, meal):
#         self.__meals.append(meal)

#     def remove_meal(self, meal):
#         self.__meals.remove(meal)

#     def get_status(self):
#         return self.__OrderStatus

#     def set_status(self, status):
#         self.__OrderStatus = status

from datetime import datetime

class MealItem:
    def __init__(self, id, quantity, menu_item):
        self.__meal_item_id = id
        self.__quantity = quantity
        self.__menu_item = menu_item

    def update_quantity(self, quantity):
        self.__quantity = quantity

class Meal:
    def __init__(self, id, seat):
        self.__meal_id = id
        self.__seat = seat
        self.__menu_items = []

    def add_meal_item(self, meal_item):
        self.__menu_items.append(meal_item)

    def remove_meal_item(self, meal_item):
        self.__menu_items.remove(meal_item)

class Check:
    def __init__(self):
        self.__total_amount = 0

    def calculate_total(self, meals):
        for meal in meals:
            for item in meal._Meal__menu_items:
                self.__total_amount += item._MealItem__menu_item.price * item._MealItem__quantity
        return self.__total_amount

class Order:
    def __init__(self, id, status, table, waiter, chef):
        self.__order_id = id
        self.__OrderStatus = status
        self.__creation_time = datetime.now()

        self.__meals = []
        self.__table = table
        self.__waiter = waiter
        self.__chef = chef
        self.__check = Check()

    def add_meal(self, meal):
        self.__meals.append(meal)

    def remove_meal(self, meal):
        self.__meals.remove(meal)

    def get_status(self):
        return self.__OrderStatus

    def set_status(self, status):
        self.__OrderStatus = status

    def calculate_total(self):
        return self.__check.calculate_total(self.__meals)

# Example usage
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

menu_item1 = MenuItem("Burger", 10.99)
menu_item2 = MenuItem("Fries", 4.99)

meal_item1 = MealItem(1, 2, menu_item1)
meal_item2 = MealItem(2, 1, menu_item2)

meal = Meal(1, 1)
meal.add_meal_item(meal_item1)
meal.add_meal_item(meal_item2)

order = Order(1, "Pending", 1, "John", "Chef Mike")
order.add_meal(meal)

total_amount = order.calculate_total()
print(f"Total Amount: ${total_amount}")
