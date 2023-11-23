# import streamlit as st
# from menu import Menu, MenuSection, MenuItem
# import uuid

# # Function to manage menus
# def menu_management_ui():
#     # Initialize the menus session state if it doesn't exist
#     if "menus" not in st.session_state:
#         st.session_state.menus = []

#     # Initialize the session state for menu sections and items
#     if "current_menu" not in st.session_state:
#         st.session_state.current_menu = None

#     if "current_section" not in st.session_state:
#         st.session_state.current_section = None

#     st.title("Menu Management")

#     # Function to create a menu
#     def create_menu():
#         st.subheader("Create Menu")
#         menu_title = st.text_input("Menu Title")
#         menu_description = st.text_input("Menu Description")
#         menu_id = str(uuid.uuid4())  # Generate a unique ID for the menu

#         if st.button("Create Menu"):
#             existing_menu = next((menu for menu in st.session_state.menus if menu.get_menu_id() == menu_id), None)

#             if existing_menu:
#                 st.warning(f"Menu with ID {menu_id} already exists!")
#                 return None
#             else:
#                 new_menu = Menu(menu_id, menu_title, menu_description)
#                 st.session_state.menus.append(new_menu)
#                 st.session_state.current_menu = new_menu  # Set the current menu
#                 st.success(f"Menu created! ID: {new_menu.get_menu_id()}, Title: {new_menu.get_title()}")
#                 return new_menu

#     # Function to create a menu section
#     def create_menu_section(menu):
#         st.subheader("Create Menu Section")
#         section_title = st.text_input("Section Title")
#         section_description = st.text_input("Section Description")
#         section_id = str(uuid.uuid4())  # Generate a unique ID for the section

#         if st.button("Create Menu Section"):
#             new_section = MenuSection(section_id, section_title, section_description)
#             menu.add_menu_section(new_section)
#             st.session_state.current_section = new_section  # Set the current section
#             st.success(f"Menu Section created! ID: {new_section.get_menu_section_id()}, Title: {new_section.get_title()}")
#             return new_section

#     # Function to create a menu item
#     def create_menu_item(section):
#         st.subheader("Create Menu Item")
#         item_title = st.text_input("Item Title")
#         item_description = st.text_input("Item Description")
#         item_price = st.number_input("Item Price", min_value=0.0, step=0.01)
#         item_id = str(uuid.uuid4())  # Generate a unique ID for the item

#         if st.button("Create Menu Item"):
#             new_item = MenuItem(item_id, item_title, item_description, item_price)
#             section.add_menu_item(new_item)
#             st.success(f"Menu Item created! ID: {new_item.get_menu_item_id()}, Title: {new_item.get_title()}")
#             return new_item

#     # Create a new menu
#     new_menu = create_menu()

#     # Display the details of the new menu
#     if new_menu:
#         st.write(f"New Menu: ID: {new_menu.get_menu_id()}, Title: {new_menu.get_title()}")

#         # Create a new menu section
#         new_section = create_menu_section(new_menu)

#         # Display details of the new menu section
#         if new_section:
#             st.write(f"New Menu Section: ID: {new_section.get_menu_section_id()}, Title: {new_section.get_title()}")

#             # Create a new menu item
#             new_item = create_menu_item(new_section)

#             # Display details of the new menu item
#             if new_item:
#                 st.write(f"New Menu Item: ID: {new_item.get_menu_item_id()}, Title: {new_item.get_title()}, Price: {new_item.get_price()}")

#     # Display details of all menus
#     st.subheader("All Menus")
#     for menu in st.session_state.menus:
#         st.write(f"ID: {menu.get_menu_id()}, Title: {menu.get_title()}")
#         for section in menu.get_menu_sections():
#             st.write(f"  Section ID: {section.get_menu_section_id()}, Title: {section.get_title()}")
#             for item in section.get_menu_items():
#                 st.write(f"    Item ID: {item.get_menu_item_id()}, Title: {item.get_title()}, Price: {item.get_price()}")

# # Call the function
# menu_management_ui()
import streamlit as st
from menu import Menu, MenuSection, MenuItem
import uuid

def menu_management_ui():
    # Initialize session state
    if "menus" not in st.session_state:
        st.session_state.menus = []
    if "current_form" not in st.session_state:
        st.session_state.current_form = None
    if "current_menu" not in st.session_state:
        st.session_state.current_menu = None
    if "current_section" not in st.session_state:
        st.session_state.current_section = None

    st.title("Menu Management")

    # Function to create a menu
    def create_menu():
        st.subheader("Create Menu")
        with st.form(key=f"create_menu_form"):
            menu_title = st.text_input("Menu Title")
            menu_description = st.text_input("Menu Description")
            menu_id = str(uuid.uuid4())  # Generate a unique ID for the menu

            if st.form_submit_button("Create Menu"):
                new_menu = Menu(menu_id, menu_title, menu_description)
                st.session_state.menus.append(new_menu)
                st.session_state.current_form = f"create_menu_section_{new_menu.get_menu_id()}"
                st.success(f"Menu created! ID: {new_menu.get_menu_id()}, Title: {new_menu.get_title()}")
                st.session_state.current_menu = new_menu

    # Function to create a menu section
    def create_menu_section():
        st.subheader("Create Menu Section")
        with st.form(key=f"create_menu_section_form_{st.session_state.current_menu.get_menu_id()}"):
            section_title = st.text_input("Section Title")
            section_description = st.text_input("Section Description")
            section_id = str(uuid.uuid4())  # Generate a unique ID for the section

            if st.form_submit_button("Create Menu Section"):
                new_section = MenuSection(section_id, section_title, section_description)
                st.session_state.current_menu.add_menu_section(new_section)
                st.session_state.current_section = new_section
                st.success(f"Menu Section created! ID: {new_section.get_menu_section_id()}, Title: {new_section.get_title()}")
                st.session_state.current_form = f"create_menu_item_{new_section.get_menu_section_id()}"

    # Function to create a menu item
    def create_menu_item():
        st.subheader("Create Menu Item")
        with st.form(key=f"create_menu_item_form_{st.session_state.current_section.get_menu_section_id()}"):
            item_title = st.text_input("Item Title")
            item_description = st.text_input("Item Description")
            item_price = st.number_input("Item Price", min_value=0.0, step=0.01)
            item_id = str(uuid.uuid4())  # Generate a unique ID for the item

            if st.form_submit_button("Create Menu Item"):
                new_item = MenuItem(item_id, item_title, item_description, item_price)
                st.session_state.current_section.add_menu_item(new_item)
                st.success(f"Menu Item created! ID: {new_item.get_menu_item_id()}, Title: {new_item.get_title()}")
                st.session_state.current_form = None

    # Display the appropriate form based on the current state
    if st.session_state.current_menu and st.session_state.current_form == f"create_menu_section_{st.session_state.current_menu.get_menu_id()}":
        create_menu_section()
    elif st.session_state.current_section and st.session_state.current_form == f"create_menu_item_{st.session_state.current_section.get_menu_section_id()}":
        create_menu_item()
    else:
        create_menu()

    # Display details of all menus
    st.subheader("All Menus")
    for menu in st.session_state.menus:
        st.subheader(f"Menu Title: {menu.get_title()}")
        st.write(f"-------------------------------------")
        for section in menu.get_menu_sections():
            st.write(f"Section Title: {section.get_title()}")
            for item in section.get_menu_items():
                st.write(f"Item Title: {item.get_title()}, Item Price: {item.get_price()}")
                st.write(f"-------------------------------------------------------")

# Call the function
menu_management_ui()
