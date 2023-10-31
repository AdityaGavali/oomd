# from abc import ABC
# import time
# class Bill(ABC):
#     def __init__(self):
#         None

# class Payment(Bill):
#     def __init__(self):
#         None

# class Cash(Payment):
#     def __init__(self):
#         None
  


# class Credit_Card(Payment):
#     def __init__(self):
#         None

    

# class Online(Payment):
#     def __init_(slef):
#         None
# from abc import ABC

# class Bill(ABC):
#     def __init__(self, amount):
#         self.amount = amount

#     def calculate_total(self):
#         return self.amount

# class Payment(Bill):
#     def make_payment(self, amount_paid):
#         if amount_paid >= self.amount:
#             print("Payment successful!")
#         else:
#             print("Insufficient funds. Payment failed.")

# class Cash(Payment):
#     def __init__(self, amount):
#         super().__init__(amount)
#         self.payment_method = "Cash"

#     def make_payment(self, amount_paid):
#         if amount_paid >= self.amount:
#             print(f"Paid {self.amount} using {self.payment_method}")
#         else:
#             print("Insufficient cash. Payment failed.")

# class CreditCard(Payment):
#     def __init__(self, amount, card_number, expiry_date):
#         super().__init__(amount)
#         self.payment_method = "Credit Card"
#         self.card_number = card_number
#         self.expiry_date = expiry_date

#     def make_payment(self, amount_paid):
#         if amount_paid >= self.amount:
#             print(f"Paid {self.amount} using {self.payment_method} ending with {self.card_number[-4:]}")
#         else:
#             print("Credit card limit exceeded. Payment failed.")

# class Online(Payment):
#     def __init__(self, amount, email):
#         super().__init__(amount)
#         self.payment_method = "Online"
#         self.email = email

#     def make_payment(self, amount_paid):
#         if amount_paid >= self.amount:
#             print(f"Paid {self.amount} using {self.payment_method} to {self.email}")
#         else:
#             print("Insufficient funds in the online account. Payment failed.")

# # Example usage
# bill_amount = 100
# cash_payment = Cash(bill_amount)
# credit_card_payment = CreditCard(bill_amount, "1234567890123456", "12/25")
# online_payment = Online(bill_amount, "example@example.com")

# amount_paid = 100
# cash_payment.make_payment(amount_paid)
# credit_card_payment.make_payment(amount_paid)
# online_payment.make_payment(amount_paid)
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

# Example usage
bill_amount = 100
cash_payment = Cash(bill_amount)
credit_card_payment = CreditCard(bill_amount, "1234567890123456", "12/25")
online_payment = Online(bill_amount, "example@example.com")

amount_paid = 100

# Collect payment details
payment_details = []
payment_details.append(cash_payment.make_payment(amount_paid))
payment_details.append(credit_card_payment.make_payment(amount_paid))
payment_details.append(online_payment.make_payment(amount_paid))

# Write payment details to a file
with open("payment_details.txt", 'w') as file:
    for detail in payment_details:
        file.write(detail + "\n")
        
print("Payment details have been written to 'payment_details.txt' file.")
