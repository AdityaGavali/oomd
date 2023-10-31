import tkinter as tk
from tkinter import messagebox
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

def process_payment():
    amount = float(amount_entry.get())
    payment_type = payment_type_var.get()
    payment_status = ""

    if payment_type == "Cash":
        payment = Cash(amount)
    elif payment_type == "Credit Card":
        card_number = card_number_entry.get()
        expiry_date = expiry_date_entry.get()
        payment = CreditCard(amount, card_number, expiry_date)
    elif payment_type == "Online":
        email = email_entry.get()
        payment = Online(amount, email)

    amount_paid = float(amount_paid_entry.get())
    payment_status = payment.make_payment(amount_paid)
    payment_details_text.config(text=payment_status)

# Create the main window
root = tk.Tk()
root.title("Payment Processor")

# Payment Type
payment_type_var = tk.StringVar()
payment_type_var.set("Cash")
payment_type_label = tk.Label(root, text="Payment Type:")
payment_type_label.pack()
payment_type_menu = tk.OptionMenu(root, payment_type_var, "Cash", "Credit Card", "Online")
payment_type_menu.pack()

# Amount
amount_label = tk.Label(root, text="Bill Amount:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# Card Number (for Credit Card)
card_number_label = tk.Label(root, text="Card Number:")
card_number_label.pack()
card_number_entry = tk.Entry(root)
card_number_entry.pack()

# Expiry Date (for Credit Card)
expiry_date_label = tk.Label(root, text="Expiry Date:")
expiry_date_label.pack()
expiry_date_entry = tk.Entry(root)
expiry_date_entry.pack()

# Email (for Online Payment)
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Amount Paid
amount_paid_label = tk.Label(root, text="Amount Paid:")
amount_paid_label.pack()
amount_paid_entry = tk.Entry(root)
amount_paid_entry.pack()

# Process Payment Button
process_button = tk.Button(root, text="Process Payment", command=process_payment)
process_button.pack()

# Payment Details
payment_details_label = tk.Label(root, text="Payment Status:")
payment_details_label.pack()
payment_details_text = tk.Label(root, text="")
payment_details_text.pack()

# Run the application
root.mainloop()