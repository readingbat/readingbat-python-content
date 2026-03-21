# @desc The **or** operator is True when at least one side is True. Follow which branch runs for each combination.

def simple_choice2(sunny, raining):
    if (sunny or raining):
        return sunny
    return not raining


def main():
    print(simple_choice2(True, True))
    print(simple_choice2(True, False))
    print(simple_choice2(False, True))
    print(simple_choice2(False, False))


if __name__ == '__main__':
    main()
