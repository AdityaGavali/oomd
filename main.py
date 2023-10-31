from enums import *
from infrastructure import Kitchen, Branch, Restaurant, TableChart
from reservation import Table, TableSeat, Reservation
from menu import MenuItem, MenuSection, Menu
from order import MealItem, Meal, Check, Order
from people import Account, Receptionist, Manager, Chef , Person


# kitchen = Kitchen("Main Kitchen")
# branch = Branch("Branch 1", "123 Main St", kitchen)
# restaurant = Restaurant("My Restaurant")
# restaurant.add_branch(branch)

# menu = Menu(1, "Main Menu", "Delicious dishes")
# section1 = MenuSection(1, "Starters", "Appetizers to start your meal")
# section1.add_menu_item(MenuItem(1, "Salad", "Healthy salad with greens", 5.99))
# section1.add_menu_item(MenuItem(2, "Soup", "Soup of the day", 4.99))
# menu.add_menu_section(section1)

# table1 = Table(1, 4, "A1")
# table2 = Table(2, 6, "B1")

    # Creating Orders and Meals
# meal_item1 = MealItem(1, 2, menu.menu_sections[0].menu_items[0])
# meal_item2 = MealItem(2, 1, menu.menu_sections[0].menu_items[1])
# meal1 = Meal(1, table1)
# meal1.add_meal_item(meal_item1)
# meal1.add_meal_item(meal_item2)

    # Creating Reservation and Assigning Table
# customer_account = Account(1, "password123", "123 Customer St")
# reservation = Reservation(1, 4, "Special Occasion", customer_account)
# reservation.add_table(table1)

    # Creating Employees
# receptionist_account = Account(2, "receptionist123", "123 Reception St")
# receptionist = Receptionist(1, receptionist_account, "Receptionist Name", "receptionist@example.com", "123-456-7890")

# manager_account = Account(3, "manager123", "123 Manager St")
# manager = Manager(2, manager_account, "Manager Name", "manager@example.com", "123-456-7890")

# chef_account = Account(4, "chef123", "123 Chef St")
# chef = Chef(3, chef_account, "Chef Name", "chef@example.com", "123-456-7890")

    # Creating Orders and Adding Meals

    # Printing Reservation Details (same as before, no changes here)

    # Printing Order Details (same as before, no changes here)

    # Modifying Menu Item and Printing Menu
# print("\nBefore Menu Item Modification:")
# print("Menu Items in Section 1:")


# print("Hello")

# print("\nAfter Menu Item Modification:")
# print("Menu Items in Section 1:")


import curses

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to our Restaurant Management System !!", curses.A_BOLD)
    stdscr.addstr(2, 0,"0. Our Team")
    stdscr.addstr(3, 0, "1. View Menu")
    stdscr.addstr(4, 0, "2. Place Order")
    stdscr.addstr(5, 0, "3. View Bill")
    stdscr.addstr(6, 0, "4. Exit")
    stdscr.refresh()

    while True:
        choice = stdscr.getch()
        stdscr.clear()
        if choice ==ord('0'):
            stdscr.addstr(0, 0, "Details of all the employee", curses.A_BOLD)
            # name = input("Enter the name: ")
            # email =(input("Enter the email address: "))  # Convert input to integer if age is expected as an integer
            # phone = int(input("Enter you phone number : "))
            # person_object = Receptionist(name, email,phone)
            stdscr.addstr(2,0," Aditya , Vansh , Hemant , Ashish")
            
        elif choice == ord('1'):
            # Code for viewing menu goes here
            stdscr.addstr(0, 0, "View Menu Option Selected", curses.A_BOLD)
        elif choice == ord('2'):
            # Code for placing an order goes here
            stdscr.addstr(0, 0, "Place Order Option Selected", curses.A_BOLD)
        elif choice == ord('3'):
            # Code for viewing orders goes here
            stdscr.addstr(0, 0, "View Bill Option Selected", curses.A_BOLD)
        elif choice == ord('4'):
            break
        else:
            stdscr.addstr(0, 0, "Invalid Choice. Please try again.", curses.A_BOLD)

        stdscr.refresh()

# curses.wrapper(main)




