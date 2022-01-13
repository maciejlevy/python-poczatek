import random

class Product:

    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price


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


class Apple:

    def __init__(self, sort_name, size, price):
        self.sort_name = sort_name
        self.size = size
        self.price = price


class Potato:

    def __init__(self, sort_name, size, price):
        self.sort_name = sort_name
        self.size = size
        self.price = price


def print_product(product):
    print(f"Produkt: {product.name} _ Kategoria: {product.category} _ Cena {product.unit_price}/ za sztukę")

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


def run_example():
    fisrt_order = generate_order()
    print_order(fisrt_order)
    second_order = generate_order()
    print_order(second_order)
    third_order = generate_order()
    print_order(third_order)




if __name__ == '__main__':
    run_example()




# if __name__ == '__main__':
#     polish_apple = Apple()
#     cake_apple = Apple()
#
#     young_potato = Potato()
#     old_potato = Potato()
#
#     print("type(young_potato):", type(young_potato))
#     print("type(cake_apple):", type(cake_apple))
#
# all_orders = [Order(), Order(), Order(), Order(), Order()]
#
# products = {
#     "Jabłko": Product(),
#     "Rzodkiew": Product(),
#     "Czekolada": Product(),
#     "Napoje": Product()
# }
#
# print(all_orders)
# print(products)