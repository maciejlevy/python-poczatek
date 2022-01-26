import random

from shop3.order_element import OrderElement
from shop3.product import Product


class Order:

    def __init__(self, first_name, last_name, order_elements=None):
        self.first_name = first_name
        self.last_name = last_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.summary_price = self.calculate_total_price()

    def calculate_total_price(self):
        summary_price = 0
        for element in self.order_elements:
            summary_price += element.calculate_price()
        return summary_price


    def __str__(self):
        line = "___" * 30
        info = "Klient który złożył zamówienie:"
        client= f"Imię: {self.first_name}         Nazwisko: {self.last_name}"
        summary_value = f"Wartosć całego zamówienia to: {self.summary_price}"
        order_detail= "Zamówienie:\n"
        for element in self.order_elements:
            order_detail += f"\t{element}\n"

        result = "\n".join([line, info, client, summary_value, order_detail, line])
        return result

    def __len__(self):
        return len(self.order_elements)


def generate_order():
    number_of_product = random.randint(1, 15)
    order_elements = []
    for product_number in range(number_of_product):
        product_name = f"Product - {product_number}"
        category = "Brak Przypisanej"
        unit_price = random.randint(1, 47)
        product = Product(product_name, category, unit_price)
        quantity = random.randint(1, 8)
        order_elements.append(OrderElement(product, quantity))

    order = Order("Maciej", "Lewandowski", order_elements=order_elements)
    return order
