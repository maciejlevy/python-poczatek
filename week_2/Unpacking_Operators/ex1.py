def print_something(*args):
    result = ""
    for argument in args:
        result += str(argument)
        result += " - "
    return result[:-3]


def run_example():
    result = print_something("Jestem", 1, "na", 100, "na", "mecie")
    print(result)

if __name__ == '__main__':
    run_example()
