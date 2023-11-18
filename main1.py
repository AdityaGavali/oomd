import streamlit as st
from datetime import datetime
from reservation import Reservation, Table, TableSeat
from infrastructure import Branch, Kitchen, Restaurant, TableChart
from people import Receptionist, Manager, Chef
from enums import *
from bill_generation_with_ui import *
from menu import Menu, MenuItem, MenuSection
from employee_creation import *

admin_credentials = st.secrets["admin_credentials"]
admin_username = admin_credentials["username"]
admin_password = admin_credentials["password"]

session_state = st.session_state
if 'bill' not in session_state:
    session_state.bill = Bill()
if "reservation" not in st.session_state:
    st.session_state.reservation = None
# Initialize the restaurant
restaurant = Restaurant("My Restaurant")
kitchen = Kitchen("Main Kitchen")
branch = Branch("Main Branch", "City Center", kitchen)
table_chart = TableChart(1)

# Create employees
receptionist = Receptionist(1, "receptionist_account", "Ashish_Receptionist", "receptionist@email.com", "123456789")
manager = Manager(2, "manager_account", "Vansh_Manager", "manager@email.com", "987654321")
chef = Chef(3, "chef_account", "Hemant_Chef", "chef@email.com", "456789012")

# Create a sample menu
menu = Menu(1, "Main Menu", "Delicious dishes for every taste")
section1 = MenuSection(1, "Starters", "Appetizing beginnings")
section1.add_menu_item(MenuItem(1, "Garlic Bread", "Toasty and flavorful", 5.99))
section1.add_menu_item(MenuItem(2, "Caprese Salad", "Fresh tomatoes and mozzarella", 7.99))
menu.add_menu_section(section1)

section2 = MenuSection(2, "Main Course", "Heartwarming mains")
section2.add_menu_item(MenuItem(3, "Spaghetti Bolognese", "Classic Italian pasta dish", 12.99))
section2.add_menu_item(MenuItem(4, "Grilled Salmon", "Healthy and delicious", 16.99))
menu.add_menu_section(section2)

# Add the menu to the branch
branch.add_menu(menu)
#  id, max_capacity, location_identifier, status=TableStatus.FREE
table1 = Table(1,5,'window',TableStatus.FREE)
table2 = Table(2,5,'corner',TableStatus.FREE)
branch.add_table(table1)
branch.add_table(table2)
table_chart.add_table(table1)
table_chart.add_table(table2)
# Create Streamlit UI
st.title("Deccan Delights Restaurant")
def generate_receipt_data(bill, amount_paid, payment_method, payment_result):
           receipt = f"Receipt Details\n\n"
           receipt += "Items Purchased:\n"
           for item in bill.items:
                receipt += f"- {item['name']}: {item['price']}\n"
           receipt += f"\nTotal Amount Paid: {amount_paid}\n"
           receipt += f"Payment Method: {payment_method}\n"
           receipt += f"Payment Result: {payment_result}\n"

           return receipt
# Initialize session state for user and navigation
if "user" not in st.session_state:
    st.session_state.user = None

if "nav_option" not in st.session_state:
    st.session_state.nav_option = "Home"

# Page selection
if st.session_state.user is None:
    st.sidebar.header("Admin Login")
    entered_username = st.sidebar.text_input("Enter username:")
    entered_password = st.sidebar.text_input("Enter password:", type="password")
    login_button = st.sidebar.button("Login")

    if login_button:
        if entered_username == admin_username and entered_password == admin_password:
            st.session_state.user = "admin"
else:
    # If the user is logged in, hide the login form
    st.sidebar.empty()

    # Rest of the code

    # Page selection for logged-in user
    st.sidebar.header("Navigation")
    st.session_state.nav_option = st.sidebar.selectbox("Select a page", ["Home","Employee Database", "Create Reservation","Our Special Menus today", "View Table Chart", "Generate Bill", "Logout"])

    # Display different pages based on the selected option
    if st.session_state.nav_option == "Home":
        st.header("Welcome to the Restaurant Management System")

    elif st.session_state.nav_option == "Employee Database":
        st.subheader("All Employees")
        for employee in [receptionist, manager, chef]:
            st.write(f"Name: {employee.get_name()}, Category: {employee.get_category()}")
        st.title("Employee Creation Section")

# Create buttons for each class
        if st.button("Create Manager"):
         create_manager()

        if st.button("Create Receptionist"):
         create_receptionist()

        if st.button("Create Chef"):
         create_chef()

    elif st.session_state.nav_option == " Special Menus ":
        st.header("Menu")
        for section in menu.get_menu_sections():
            st.subheader(section.get_title())
            for item in section.get_menu_items():
                st.write(f"{item.get_title()}: {item.get_price()}")

    elif st.session_state.nav_option == "Create Reservation":
        st.header("Create Reservation")

        # Form to create a reservation
        customer_name = st.text_input("Customer Name")
        people_count = st.number_input("Number of People", min_value=1, step=1)
        notes = st.text_area("Notes")
        reservation_date = st.date_input("Reservation Date", value=datetime.now())
        reservation_time = st.time_input("Reservation Time", value=datetime.now().time())

        if st.button("Create Reservation"):
            # Logic to create a reservation
            reservation = receptionist.create_reservation(
                customer_name, people_count, notes, branch, table_chart, people_count,datetime.combine(reservation_date, reservation_time)
            )
            if reservation:
                st.success(f"Reservation created successfully! Reservation ID: {reservation.get_reservation_id()}")
                st.session_state.reservation = reservation
            else:
                st.error("No available tables for the specified time and capacity.")


    elif st.session_state.nav_option == "View Table Chart":
        st.header("View Table Chart")
        st.write(f"{receptionist.view_table_chart(table_chart)}")

   

    elif st.session_state.nav_option == "Generate Bill":
        st.header("Generate Bill")
        bill = session_state.bill

        # Add items to the bill
        item_name = st.text_input("Item Name")
        item_price = st.number_input("Item Price", min_value=0.0, step=0.01)

        if st.button("Add Item"):
          bill.add_item(item_name, item_price)
          st.success(f"Item '{item_name}' added to the bill.")
        if st.button("Clear"):
          bill.items.clear()
    # Display the current bill
        st.subheader("Current Bill")
        for item in bill.items:
          st.write(f"{item['name']}: {item['price']}")

        bill_amount = bill.calculate_total()
        st.write(f"Total Bill Amount: {bill_amount}")

    # Continue with payment logic based on the selected payment method
        payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Online"])
        email = st.text_input("Customer Email")
        card_number = st.text_input("Credit Card Number", type="password")
        expiry_date = st.text_input("Expiry Date (MM/YYYY)", type="password")
        payment_result = None
        if st.button("Generate Bill"):
          if payment_method == "Cash":
            cash_bill = CashBill()
            payment_result = cash_bill.make_payment(bill_amount)

          elif payment_method == "Credit Card":
            credit_card_bill = CreditCardBill(card_number, expiry_date)
            payment_result = credit_card_bill.make_payment(bill_amount)

          elif payment_method == "Online":   
            online_bill = OnlineBill(email)
            payment_result = online_bill.make_payment(bill_amount)
          else:
            st.error("Invalid payment method selected.")
          if payment_result and "failed" not in payment_result.lower():
        # Display receipt information
            st.subheader("Receipt Details")
            st.write("Items Purchased:")
            for item in bill.items:
              st.write(f"- {item['name']}: {item['price']}")
            st.write(f"Total Amount Paid: {bill_amount}")
            st.write(f"Payment Method: {payment_method}")
            st.write(f"Payment Result: {payment_result}") 
            receipt_data = generate_receipt_data(bill, bill_amount, payment_method, payment_result)
            st.download_button(
            label="Download Receipt",
            data=receipt_data.encode(),
            file_name="receipt.txt",
            mime="text/plain",
        )

          else:
           st.error(f"Payment failed. {payment_result}")
      
   
    elif st.session_state.nav_option == "Logout":
        st.session_state.user = None
