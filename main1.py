import streamlit as st
from datetime import datetime
from reservation import Reservation, Table, TableSeat
from infrastructure import Branch, Kitchen, Restaurant, TableChart
from people import *
from enums import *
from menu_management import *
from bill_generation_with_ui import *
from menu import Menu, MenuItem, MenuSection
from employee_creation import *

admin_credentials = st.secrets["admin_credentials"]
admin_username = admin_credentials["username"]
admin_password = admin_credentials["password"]

session_state = st.session_state
if "tables" not in st.session_state:
    st.session_state.tables = []
if "reservations" not in st.session_state:
    st.session_state.reservations = []
if "managers" not in st.session_state:
    st.session_state.managers = []
if "receptionists" not in st.session_state:
    st.session_state.receptionists = []
if "chefs" not in st.session_state:
    st.session_state.chefs = []
if 'bill' not in session_state:
    session_state.bill = Bill()
if "reservation" not in st.session_state:
    st.session_state.reservation = None
# Initialize the restaurant
restaurant = Restaurant("My Restaurant")
kitchen = Kitchen("Main Kitchen")
branch = Branch("Main Branch", "City Center", kitchen)
table_chart = TableChart(1)

menu = Menu(1, "Main Menu", "Delicious dishes for every taste")
section1 = MenuSection(1, "Starters", "Appetizing beginnings")
section1.add_menu_item(MenuItem(1, "Garlic Bread", "Toasty and flavorful", 5.99))
section1.add_menu_item(MenuItem(2, "Caprese Salad", "Fresh tomatoes and mozzarella", 7.99))
menu.add_menu_section(section1)

section2 = MenuSection(2, "Main Course", "Heartwarming mains")
section2.add_menu_item(MenuItem(3, "Spaghetti Bolognese", "Classic Italian pasta dish", 12.99))
section2.add_menu_item(MenuItem(4, "Grilled Salmon", "Healthy and delicious", 16.99))
menu.add_menu_section(section2)

branch.add_menu(menu)
#  id, max_capacity, location_identifier, status=TableStatus.FREE
table1 = Table(1,5,'window',TableStatus.FREE)
table2 = Table(2,5,'corner',TableStatus.OCCUPIED)
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
if "user" not in st.session_state:
    st.session_state.user = None
if "nav_option" not in st.session_state:
    st.session_state.nav_option = "Home"
if st.session_state.user is None:
    st.sidebar.header("Admin Login")
    entered_username = st.sidebar.text_input("Enter username:")
    entered_password = st.sidebar.text_input("Enter password:", type="password")
    login_button = st.sidebar.button("Login")

    if login_button:
        if entered_username == admin_username and entered_password == admin_password:
            st.session_state.user = "admin"
else:
 
    st.sidebar.empty()

    st.sidebar.header("Navigation")
    st.session_state.nav_option = st.sidebar.selectbox("Select a page", ["Home","Employee Database","Special Menus", "View Table Chart", "Generate Bill", "Logout"])

    # Display different pages based on the selected option
    if st.session_state.nav_option == "Home":
        st.header("Welcome to the Restaurant Management System")

    elif st.session_state.nav_option == "Employee Database":
        st.title("Employee Management Section")
        st.subheader("All Employees")

    # Display details of all employees
        for manager in st.session_state.managers:
          st.write(f"Name: {manager.get_name()}, Category: {manager.get_category()}")
        for receptionist in st.session_state.receptionists:
         st.write(f"Name: {receptionist.get_name()}, Category: {receptionist.get_category()}")
        for chef in st.session_state.chefs:
         st.write(f"Name: {chef.get_name()}, Category: {chef.get_category()}")

    # Employee management buttons
        employee_type = st.radio("Select Employee Type", ["Manager", "Receptionist", "Chef"])
        if employee_type == "Manager":
          create_manager()
          if st.button("View Managers"):
            for manager in st.session_state.managers:
                st.write(f"Name: {manager.get_name()}, Category: {manager.get_category()}, Admin: {manager.is_admin()}")
        elif employee_type == "Receptionist":
          create_receptionist()
          if st.button("View Receptionists"):
            for receptionist in st.session_state.receptionists:
                st.write(f"Name: {receptionist.get_name()}, Category: {receptionist.get_category()}")
        elif employee_type == "Chef":
          create_chef()
          if st.button("View Chefs"):
            for chef in st.session_state.chefs:
                st.write(f"Name: {chef.get_name()}, Category: {chef.get_category()}")
     
    elif st.session_state.nav_option == "Special Menus":
        menu_management_ui()

    elif st.session_state.nav_option == "View Table Chart":
        st.title("Reservation And Table Management")
        reservation_option = st.selectbox("Select Reservation Action", ["Create Reservation", "View Reservations"])

        if reservation_option == "Create Reservation":
         st.subheader("Create Reservation")
         with st.form(key="create_reservation_form"):
          customer_name = st.text_input("Customer Name")
          people_count = st.number_input("Number of People", min_value=1, step=1)
          notes = st.text_area("Reservation Notes")
          reservation_id = st.text_input("Reservation ID")

          if st.form_submit_button("Create Reservation"):
            reservation = Reservation(reservation_id, people_count, notes, customer_name)
            st.session_state.reservations.append(reservation)
            st.success(f"Reservation created! ID: {reservation.get_reservation_id()}, Customer: {customer_name}")

        elif reservation_option == "View Reservations":
          st.subheader("View Reservations")
          for reservation in st.session_state.reservations:
            st.write(f"Reservation ID: {reservation.get_reservation_id()}")
     
        st.title("Table data")
        table_option = st.selectbox("Select Action", ["Create Table", "View tables"])

        if table_option == "Create Table":
         with st.form(key="create_table_form"):
          table_id = st.text_input("Table id")
          table_capacity = st.number_input("Capacity", min_value=1, step=1)
          table_location = st.text_area("Location")
          table_status = st.text_input("Status (FREE OR RESERVED)")
          if st.form_submit_button("Add table"):
            table = Table(table_id, table_capacity, table_location, table_status)
            st.session_state.tables.append(table)
            st.success(f"Table added! ID: {table.get_number()}, Location: {table.show_location()}, Status: {table.show_status()}")
        elif table_option == "View tables":
          st.subheader("Tables")
          for table in st.session_state.tables:
            st.write(f"Table Id: {table.get_number()}, Location: {table.show_location()}, Status: {table.show_status()}")

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
