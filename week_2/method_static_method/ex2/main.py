
from shop3.product import Product
from shop3.order import Order
from shop3.apple import Apple
from shop3.potato import Potato


def run_example():
    first_order = Order.generate_order(8)
    print(first_order)

    chocolate = Product(name="Czekolada", category="Słodycze", unit_price=3)
    first_order.add_product_to_order(chocolate, quantity=10)
    print(first_order)

    order_under_limit = Order.generate_order(5)
    order_under_limit.add_product_to_order(chocolate, quantity=2)
    print(order_under_limit)

if __name__ == '__main__':
    run_example()
