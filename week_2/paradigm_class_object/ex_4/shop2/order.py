import random

from shop2.product import Product, print_product


class Order:

    def __init__(self, first_name, last_name, products=None,):
        self.first_name = first_name
        self.last_name = last_name
        if products is None:
            products = []
        self.products = products

        summary_price = 0
        for product in products:
            summary_price += product.unit_price
        self.summary_price = summary_price


def print_order(order):
    print("___" * 30)
    print(f"Klient który złożył zamówienie:")
    print(f"Imię: {order.first_name}         Nazwisko: {order.last_name}")

    print(f"Wartosć całego zamówienia to: {order.summary_price}")
    print(f"Zamówienie: ")
    for product in order.products:
        print("\t", end="")
        print_product(product)
    print("___" * 30)
    print()


def generate_order():
    number_of_product = random.randint(1, 15)
    products = []
    for product_number in range(number_of_product):
        product_name = f"Product - {product_number}"
        category = "Brak Przypisanej"
        unit_price = random.randint(1, 47)
        product = Product(product_name, category, unit_price)
        products.append(product)

    order = Order("Maciej", "Lewandowski", products=products)
    return order
