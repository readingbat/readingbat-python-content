# @desc **round()** rounds to the nearest integer. Python uses "banker's rounding" — 0.5 rounds to the nearest even number.

def math7(x):
    return round(x)


def main():
    print(math7(3.7))
    print(math7(3.2))
    print(math7(3.5))
    print(math7(4.5))
    print(math7(-1.7))
    print(math7(0.0))


if __name__ == '__main__':
    main()
