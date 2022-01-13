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
        self.product_list = products
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

def run_example():
    gold_apple = Apple("Jonagold", "big", 5)
    red_apple = Apple("Champion", "medium", 4.5)
    shine_apple = Apple("Globo", "small", 3.9)

    old_potato = Potato("Old Potato", "big", 2.0)
    young_potato = Potato("Young Potato", "small", 3.45)

    chocolate = Product("Chocolate", "Sweets", 4.20)
    lech_beer = Product("Lech", "Beer", 3.20)

    print(gold_apple)
    print(red_apple)
    print(shine_apple)
    print(old_potato)
    print(young_potato)
    print(chocolate)
    print(lech_beer)

    first_order = Order("Maciej", "Lewandowski", [chocolate])
    print(first_order)

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