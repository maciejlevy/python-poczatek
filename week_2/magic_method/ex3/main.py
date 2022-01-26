
from shop3.order import generate_order
from shop3.apple import Apple
from shop3.potato import Potato


def run_example():
    first_order = generate_order()
    print(f"Liczba zamówionych pozycji: {len(first_order)}")
    second_order = generate_order()
    print(f"Liczba zamówionych pozycji: {len(second_order)}")

if __name__ == '__main__':
    run_example()
