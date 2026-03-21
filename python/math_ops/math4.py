# @desc Parentheses force the addition to happen before the multiplication.

def math4(a, b, c):
    return (a + b) * c


def main():
    print(math4(2, 3, 4))
    print(math4(1, 1, 1))
    print(math4(0, 5, 3))
    print(math4(10, 0, 5))
    print(math4(3, 7, 0))


if __name__ == '__main__':
    main()
