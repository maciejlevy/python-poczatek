from shop3.product import Product
from shop3.order import Order
from shop3.discount_policy import loyal_customer_policy
from shop3.discount_policy import christmas_policy
from shop3.apple import Apple
from shop3.potato import Potato
import random
from shop3.order_element import OrderElement

def generate_orderd_elements():
    order_elements = []
    for product_number in range(5):
        name = f"Product - {product_number}"
        category = "Inne"
        unit_price = random.randint(1, 20)
        product = Product(name, category, unit_price)
        quantity = random.randint(1,15)
        order_elements.append(OrderElement(product, quantity))

    return order_elements

def get_order_price(order):
    return order.summary_price

def run_example():
    first_name = "Maciej"
    last_name = "Lewandowski"
    order_elements = generate_orderd_elements()
    standard_order = Order(first_name,last_name,order_elements)
    loyal_order = Order(first_name, last_name, order_elements, discount_policy=loyal_customer_policy)
    christmas_order = Order(first_name, last_name, order_elements, discount_policy=christmas_policy)

    print(standard_order)
    print(loyal_order)
    print(christmas_order)
    # orders = []
    # for _ in range(5):
    #     orders.append(Order.generate_order())
    #
    # orders.sort(key=get_order_price)
    # for order in orders:
    #     print(order)


if __name__ == '__main__':
    run_example()
