class Product:

    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price


def print_product(product):
    print(f"Produkt: {product.name} _ Kategoria: {product.category} _ Cena {product.unit_price}/ za sztukę")