import streamlit as st
from people import Manager, Receptionist, Chef

# Initialize session state
if "managers" not in st.session_state:
    st.session_state.managers = []
if "receptionists" not in st.session_state:
    st.session_state.receptionists = []
if "chefs" not in st.session_state:
    st.session_state.chefs = []

def create_manager():
    st.subheader("Create Manager")
    with st.form(key="create_manager_form"):
        manager_name = st.text_input("Manager Name")
        manager_email = st.text_input("Manager Email")
        manager_phone = st.text_input("Manager Phone")
        manager_id = st.text_input("Manager ID")
        manager_account = st.text_input("Manager Account")
        manager_is_admin = st.checkbox("Is Admin")

        if st.form_submit_button("Create Manager"):
            manager1 = Manager(manager_id, manager_account, manager_name, manager_email, manager_phone, manager_is_admin)
            st.session_state.managers.append(manager1)
            
            st.success(f"Manager created! ID: {manager1.get_employee_id()}, Name: {manager1.get_name()}")

def create_receptionist():
    st.subheader("Create Receptionist")
    with st.form(key="create_receptionist_form"):
        receptionist_name = st.text_input("Receptionist Name")
        receptionist_email = st.text_input("Receptionist Email")
        receptionist_phone = st.text_input("Receptionist Phone")
        receptionist_id = st.text_input("Receptionist ID")
        receptionist_account = st.text_input("Receptionist Account")

        if st.form_submit_button("Create Receptionist"):
            receptionist = Receptionist(receptionist_id, receptionist_account, receptionist_name, receptionist_email, receptionist_phone)
            st.session_state.receptionists.append(receptionist)
            st.success(f"Receptionist created! ID: {receptionist.get_employee_id()}, Name: {receptionist.get_name()}")

def create_chef():
    st.subheader("Create Chef")
    with st.form(key="create_chef_form"):
        chef_name = st.text_input("Chef Name")
        chef_email = st.text_input("Chef Email")
        chef_phone = st.text_input("Chef Phone")
        chef_id = st.text_input("Chef ID")
        chef_account = st.text_input("Chef Account")

        if st.form_submit_button("Create Chef"):
            chef = Chef(chef_id, chef_account, chef_name, chef_email, chef_phone)
            st.session_state.chefs.append(chef)
            st.success(f"Chef created! ID: {chef.get_employee_id()}, Name: {chef.get_name()}")

