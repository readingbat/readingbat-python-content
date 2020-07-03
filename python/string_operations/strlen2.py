def strlen2(s, t):
    length = len(s) + len(t)
    return length


def main():
    print(strlen2("Bike", "grass"))
    print(strlen2("", ""))
    print(strlen2("56", ""))
    print(strlen2("Cat", "Dog"))
    print(strlen2("Golf", "Ball"))


if __name__ == "__main__":
    main()
