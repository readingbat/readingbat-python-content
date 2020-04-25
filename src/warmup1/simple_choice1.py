def simple_choice2(sunny):
    if (not sunny):
        return sunny
    else:
        return not sunny


def main():
    print(simple_choice2(True))
    print(simple_choice2(False))


if __name__ == "__main__":
    main()
