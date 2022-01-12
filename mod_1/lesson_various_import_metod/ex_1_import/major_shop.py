from shop.order import make_new_order

def run_shop():
    print("Witamy w naszym sklepie")
    product_name = input("Wybierz jak towar chcesz kupić: jabłka, woda, chleb? ")
    quantity = int(input("Ile sztuk/kg chcesz kupić? "))

    result = make_new_order(product_name, quantity)
    if result is not None:
        total_price = result["total_price"]
        print(f"Koszt zakupu towaru w podanej ilości wyniesie: {total_price} PLN ")


if __name__ == '__main__':
    run_shop()
