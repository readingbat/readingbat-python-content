# @desc **abs()** returns the distance from zero — it makes negative numbers positive.

def math5(x):
    return abs(x)


def main():
    print(math5(-5))
    print(math5(5))
    print(math5(0))
    print(math5(-100))
    print(math5(1))
    print(math5(-1))


if __name__ == '__main__':
    main()
