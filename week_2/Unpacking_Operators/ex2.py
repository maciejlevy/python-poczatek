def print_values_and_names(**kwargs):
    values_and_names = "print_values_and_names("
    for argument_name, argument_value in kwargs.items():
        values_and_names += f"{argument_name} = {argument_value}"
    values_and_names += ")"
    print(values_and_names)


def run_example():
    print_values_and_names(Imie="Maciej ", Nazwisko="Lewandowski ", Wiek=26)

if __name__ == '__main__':
    run_example()
