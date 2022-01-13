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





def run_example():
    gold_apple = Apple("Jonagold", "big", 5.0)
    red_apple = Apple("Champion", "medium", 4.5)
    shine_apple = Apple("Globo", "small", 3.9)

    old_potato = Potato("Old Potato", "big", 2.0)
    young_potato = Potato("Young Potato", "small", 3.45)

    chocolate = Product("Chocolate", "Sweets", 4.20)
    lech_beer = Product("Lech", "Beer", 3.20)
    first_order = Order("Maciej", "Lewandowski", [chocolate])
    print_order(first_order)
    second_order = Order("Sandra", "Dąbkowska", [chocolate, lech_beer])
    print_order(second_order)


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