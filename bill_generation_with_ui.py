
import streamlit as st
from abc import ABC

class Bill(ABC):
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        return self.amount

class Payment(Bill):
    def make_payment(self, amount_paid):
        if amount_paid >= self.amount:
            return "Payment successful!"
        else:
            return "Insufficient funds. Payment failed."

class Cash(Payment):
    def __init__(self, amount):
        super().__init__(amount)
        self.payment_method = "Cash"

    def make_payment(self, amount_paid):
        if amount_paid >= self.amount:
            return f"Paid {self.amount} using {self.payment_method}"
        else:
            return "Insufficient cash. Payment failed."

class CreditCard(Payment):
    def __init__(self, amount, card_number, expiry_date):
        super().__init__(amount)
        self.payment_method = "Credit Card"
        self.card_number = card_number
        self.expiry_date = expiry_date

    def make_payment(self, amount_paid):
        if amount_paid >= self.amount:
            return f"Paid {self.amount} using {self.payment_method} ending with {self.card_number[-4:]}"
        else:
            return "Credit card limit exceeded. Payment failed."

class Online(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.payment_method = "Online"
        self.email = email

    def make_payment(self, amount_paid):
        if amount_paid >= self.amount:
            return f"Paid {self.amount} using {self.payment_method} to {self.email}"
        else:
            return "Insufficient funds in the online account. Payment failed."

def main():
    st.title("Payment Processor")

    payment_type = st.selectbox("Payment Type", ["Cash", "Credit Card", "Online"])
    amount = st.number_input("Bill Amount", min_value=0.0, step=1.0, format="%.2f")

    if payment_type == "Credit Card":
        card_number = st.text_input("Card Number")
        expiry_date = st.text_input("Expiry Date")
        payment = CreditCard(amount, card_number, expiry_date)
    elif payment_type == "Online":
        email = st.text_input("Email")
        payment = Online(amount, email)
    else:
        payment = Cash(amount)

    amount_paid = st.number_input("Amount Paid", min_value=0.0, step=1.0, format="%.2f")

    if st.button("Process Payment"):
        payment_status = payment.make_payment(amount_paid)
        st.write("Payment Status:", payment_status)

if __name__ == "__main__":
    main()
