class Apple:

    def __init__(self, sort_name, size, price):
        self.sort_name = sort_name
        self.size = size
        self.price = price

    def calculate_price(self, quantity):
        return quantity * self.price

    def __repr__(self):
        return f"Apple sort name: {self.sort_name}, size: {self.size}, price: {self.price}"