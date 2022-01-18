from shop2.apple import Apple
from shop2.potato import Potato
from shop2.order import print_order, generate_order


def run_example():

    gold_apple = Apple("Jonagold", "big", 5)
    red_apple = Apple("Champion", "medium", 4.5)
    shine_apple = Apple("Globo", "small", 3.9)
    print(shine_apple.sort_name, shine_apple)

    old_potato = Potato("Old Potato", "big", 2.0)
    young_potato = Potato("Young Potato", "small", 3.45)
    print(old_potato.sort_name, old_potato)


    fisrt_order = generate_order()
    print_order(fisrt_order)
    second_order = generate_order()
    print_order(second_order)
    third_order = generate_order()
    print_order(third_order)


if __name__ == '__main__':
    run_example()
