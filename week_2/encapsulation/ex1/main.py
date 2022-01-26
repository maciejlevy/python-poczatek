
from shop3.product import Product
from shop3.order import generate_order
from shop3.apple import Apple
from shop3.potato import Potato


def run_example():
    first_order = generate_order()
    print(first_order)

    cookie = Product(name="Czekolada", category="Słodycze", unit_price=3)
    first_order.add_product_to_order(cookie, quantity=10)
    print(first_order)

if __name__ == '__main__':
    run_example()
