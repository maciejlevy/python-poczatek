from shop3.apple import Apple
from shop3.potato import Potato


def run_example():
    gold_apple = Apple("Jonagold", "big", 5)
    red_apple = Apple("Champion", "medium", 4.5)
    shine_apple = Apple("Globo", "small", 3.9)
    print(f"5 kg Jabłka Champion kosztuje: {red_apple.calculate_price(5)}")

    old_potato = Potato("Old Potato", "big", 2.0)
    young_potato = Potato("Young Potato", "small", 3.45)
    print(f"8 kg Old Potato kosztuje: {old_potato.calculate_price(8)}")


if __name__ == '__main__':
    run_example()
