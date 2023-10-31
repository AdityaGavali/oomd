from enums import *
from infrastructure import Kitchen, Branch, Restaurant, TableChart
from reservation import Table, TableSeat, Reservation
from menu import MenuItem, MenuSection, Menu
from order import MealItem, Meal, Check, Order
from people import Account, Receptionist, Manager, Chef


kitchen = Kitchen("Main Kitchen")
branch = Branch("Branch 1", "123 Main St", kitchen)
restaurant = Restaurant("My Restaurant")
restaurant.add_branch(branch)

menu = Menu(1, "Main Menu", "Delicious dishes")
section1 = MenuSection(1, "Starters", "Appetizers to start your meal")
section1.add_menu_item(MenuItem(1, "Salad", "Healthy salad with greens", 5.99))
section1.add_menu_item(MenuItem(2, "Soup", "Soup of the day", 4.99))
menu.add_menu_section(section1)

table1 = Table(1, 4, "A1")
table2 = Table(2, 6, "B1")

    # Creating Orders and Meals
# meal_item1 = MealItem(1, 2, menu.menu_sections[0].menu_items[0])
# meal_item2 = MealItem(2, 1, menu.menu_sections[0].menu_items[1])
# meal1 = Meal(1, table1)
# meal1.add_meal_item(meal_item1)
# meal1.add_meal_item(meal_item2)

    # Creating Reservation and Assigning Table
customer_account = Account(1, "password123", "123 Customer St")
reservation = Reservation(1, 4, "Special Occasion", customer_account)
reservation.add_table(table1)

    # Creating Employees
receptionist_account = Account(2, "receptionist123", "123 Reception St")
receptionist = Receptionist(1, receptionist_account, "Receptionist Name", "receptionist@example.com", "123-456-7890")

manager_account = Account(3, "manager123", "123 Manager St")
manager = Manager(2, manager_account, "Manager Name", "manager@example.com", "123-456-7890")

chef_account = Account(4, "chef123", "123 Chef St")
chef = Chef(3, chef_account, "Chef Name", "chef@example.com", "123-456-7890")

    # Creating Orders and Adding Meals
order = Order(1, OrderStatus.RECEIVED, table1, receptionist, chef)
order.add_meal(meal1)

    # Printing Reservation Details (same as before, no changes here)

    # Printing Order Details (same as before, no changes here)

    # Modifying Menu Item and Printing Menu
print("\nBefore Menu Item Modification:")
print("Menu Items in Section 1:")




print("\nAfter Menu Item Modification:")
print("Menu Items in Section 1:")


