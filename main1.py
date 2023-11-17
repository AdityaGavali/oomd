import streamlit as st
from datetime import datetime
from reservation import Reservation, Table, TableSeat
from infrastructure import Branch, Kitchen, Restaurant, TableChart
from people import Receptionist, Manager, Chef
from enums import ReservationStatus
from bill_generation_with_ui import *
from menu import Menu, MenuItem, MenuSection

# Hardcoded admin credentials (for simplicity, replace with a secure authentication mechanism)
admin_username = "admin"
admin_password = "admin123"
session_state = st.session_state
if 'bill' not in session_state:
    session_state.bill = Bill()

# Initialize the restaurant
restaurant = Restaurant("My Restaurant")
kitchen = Kitchen("Main Kitchen")
branch = Branch("Main Branch", "City Center", kitchen)
table_chart = TableChart(1)

# Create employees
receptionist = Receptionist(1, "receptionist_account", "Receptionist Name", "receptionist@email.com", "123456789")
manager = Manager(2, "manager_account", "Manager Name", "manager@email.com", "987654321")
chef = Chef(3, "chef_account", "Chef Name", "chef@email.com", "456789012")

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

# Create Streamlit UI
st.title("Deccan Delights Restaurant")

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
    st.session_state.nav_option = st.sidebar.selectbox("Select a page", ["Home", "Create Reservation", "View Table Chart", "Generate Bill", "Logout"])

    # Display different pages based on the selected option
    if st.session_state.nav_option == "Home":
        st.header("Welcome to the Restaurant Management System")
        # Display general information about the restaurant

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
                customer_name, people_count, notes, branch, table_chart, people_count, datetime.combine(reservation_date, reservation_time)
            )
            if reservation:
                st.success(f"Reservation created successfully! Reservation ID: {reservation.get_reservation_id()}")
            else:
                st.error("No available tables for the specified time and capacity.")

    elif st.session_state.nav_option == "View Table Chart":
        st.header("View Table Chart")
        receptionist.view_table_chart(table_chart)

        # Display the menu
        st.header("Menu")
        for section in menu.get_menu_sections():
            st.subheader(section.get_title())
            for item in section.get_menu_items():
                st.write(f"{item.get_title()}: {item.get_price()}")

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

        if st.button("Generate Bill"):
          if payment_method == "Cash":
            cash_bill = CashBill()
            st.success(cash_bill.make_payment(bill_amount))

          elif payment_method == "Credit Card":
            card_number = st.text_input("Credit Card Number")
            expiry_date = st.text_input("Expiry Date (MM/YYYY)")
            credit_card_bill = CreditCardBill(card_number, expiry_date)
            st.success(credit_card_bill.make_payment(bill_amount))

          elif payment_method == "Online":
            email = st.text_input("Customer Email")
            online_bill = OnlineBill(email)
            st.success(online_bill.make_payment(bill_amount))

          else:
            st.error("Invalid payment method selected.")
   
    elif st.session_state.nav_option == "Logout":
        st.session_state.user = None
