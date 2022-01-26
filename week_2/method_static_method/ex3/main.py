
from shop3.product import Product
from shop3.order import OrderElement
from shop3.tax_calculator import TaxCalculator
from shop3.apple import Apple
from shop3.potato import Potato


def run_example():
    chocolate = Product(name="Czekolada", category="Jedzenie", unit_price=3)d
    apple = Product(name= "Jabłka", category="Owoce i Warzywa", unit_price= 5)
    cola = Product(name="Coca-Cola", category="Napoje", unit_price=8.50)

    three_chocolate = OrderElement(chocolate, quantity=3)
    five_kg_apple = OrderElement(apple, quantity=5)
    cola_pack = OrderElement(cola, quantity=6)

    chocolate_tax = TaxCalculator.tax_for_order(three_chocolate)
    apple_tax = TaxCalculator.tax_for_order(five_kg_apple)
    cola_tax = TaxCalculator.tax_for_order(cola_pack)

    print(f"Cena netto czekolady: {three_chocolate.calculate_price()} + {chocolate_tax:.2f} podatku VAT")
    print(f"Cena netto jabłek: {five_kg_apple.calculate_price()} + {apple_tax:.2f} podatku VAT")
    print(f"Cena netto Coca-Coli: {cola_pack.calculate_price()}+ {cola_tax:.2f} Podatku VAT")


    # first_order = Order.generate_order(8)
    # print(first_order)
    #
    #
    # first_order.add_product_to_order(chocolate, quantity=10)
    # print(first_order)
    #
    # order_under_limit = Order.generate_order(5)
    # order_under_limit.add_product_to_order(chocolate, quantity=2)
    # print(order_under_limit)

if __name__ == '__main__':
    run_example()
