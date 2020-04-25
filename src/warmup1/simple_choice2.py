def simple_choice(sunny, raining):
    if (sunny or raining):
        return sunny
    return not raining


def main():
    print(simple_choice(True, True))
    print(simple_choice(True, False))
    print(simple_choice(False, True))
    print(simple_choice(False, False))


if __name__ == "__main__":
    main()
