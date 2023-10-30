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


class Check():
    def __init__(self):
        None


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

