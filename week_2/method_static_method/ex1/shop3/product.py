class Product:

    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category == other.category and
                self.unit_price == other.unit_price)


    def __str__(self):
        return f"Produkt: {self.name} _ Kategoria: {self.category} _ Cena {self.unit_price}/za sztukę"
