
from shop3.order import generate_order
from shop3.apple import Apple
from shop3.potato import Potato


def run_example():
    first_order = generate_order()
    print(first_order)
    second_order = generate_order()
    print(second_order)

    gold_apple = Apple("Jonagold", "big", 5)
    red_apple = Apple("Champion", "medium", 4.5)
    shine_apple = Apple("Globo", "small", 3.9)
    print(gold_apple)
    print(red_apple)
    print(shine_apple)

    old_potato = Potato("Old Potato", "big", 2.0)
    young_potato = Potato("Young Potato", "small", 3.45)
    print(old_potato)
    print(young_potato)

if __name__ == '__main__':
    run_example()
