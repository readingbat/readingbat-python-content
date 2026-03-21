# @desc Multiplication is performed before addition unless you use parentheses.

def math1(x, y):
    return x + y * 2


def main():
    print(math1(3, 4))
    print(math1(1, 1))
    print(math1(0, 5))
    print(math1(10, 0))
    print(math1(2, 3))


if __name__ == '__main__':
    main()
