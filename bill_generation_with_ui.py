
class Bill:
    def __init__(self):
        self.items = []

    def make_payment(self, amount_paid):
        raise NotImplementedError("Subclasses must implement the make_payment method")

    def add_item(self, item_name, item_price):
        self.items.append({"name": item_name, "price": item_price})

    def calculate_total(self):
        return sum(item["price"] for item in self.items)
class CashBill(Bill):
    def make_payment(self, amount_paid):
        if amount_paid >= self.calculate_total():
            return "Cash payment successful!"
        else:
            return "Insufficient cash. Payment failed."

class CreditCardBill(Bill):
    def __init__(self, card_number, expiry_date):
        super().__init__()
        self.card_number = card_number
        self.expiry_date = expiry_date

    def make_payment(self, amount_paid):
        if amount_paid >= self.calculate_total():
            return f"Paid  using Credit Card ending with {self.card_number[-4:]}"
        else:
            return "Credit card limit exceeded. Payment failed."

class OnlineBill(Bill):
    def __init__(self, email):
        super().__init__()
        self.email = email

    def make_payment(self, amount_paid):
        if amount_paid >= self.calculate_total():
            return f"Paid  online by {self.email}"
        else:
            return "Insufficient funds in the online account. Payment failed."
