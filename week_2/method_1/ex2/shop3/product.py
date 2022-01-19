class Product:

    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price


    def print_self(self):
        print(f"Produkt: {self.name} _ Kategoria: {self.category} _ Cena {self.unit_price}/ za sztukę")
