import streamlit as st
from datetime import datetime
from reservation import Reservation, Table, TableSeat
from infrastructure import Branch, Kitchen, Restaurant, TableChart
from people import Receptionist, Manager, Chef
from enums import ReservationStatus
from bill_genration import Cash, CreditCard, Online
from menu import Menu, MenuItem, MenuSection

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
st.title("Surya Restaurant")

# Navigation
page = st.sidebar.selectbox("Select a page", ["Home", "Create Reservation", "View Table Chart", "Generate Bill"])

if page == "Home":
    st.header("Welcome to the Restaurant !!")
    # Display general information about the restaurant

elif page == "Create Reservation":
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

elif page == "View Table Chart":
    st.header("View Table Chart")
    receptionist.view_table_chart(table_chart)

    # Display the menu
    st.header("Menu")
    for section in menu.get_menu_sections():
        st.subheader(section.get_title())
        for item in section.get_menu_items():
            st.write(f"{item.get_title()}: {item.get_price()}")

elif page == "Generate Bill":
    st.header("Generate Bill")

    # Form to generate a bill
    bill_amount = st.number_input("Bill Amount", min_value=0.0, step=0.01)
    payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Online"])

    if st.button("Generate Bill"):
        if payment_method == "Cash":
            cash_payment = Cash(bill_amount)
            st.success(cash_payment.make_payment(bill_amount))
        elif payment_method == "Credit Card":
            card_number = st.text_input("Credit Card Number")
            expiry_date = st.text_input("Expiry Date (MM/YYYY)")
            credit_card_payment = CreditCard(bill_amount, card_number, expiry_date)
            st.success(credit_card_payment.make_payment(bill_amount))
        elif payment_method == "Online":
            email = st.text_input("Customer Email")
            online_payment = Online(bill_amount, email)
            st.success(online_payment.make_payment(bill_amount))
        else:
            st.error("Invalid payment method selected.")
