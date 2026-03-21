# @desc This is a polynomial — evaluate each term using order of operations, then add them together.

def math8(x):
    return x * x + 2 * x + 1


def main():
    print(math8(0))
    print(math8(1))
    print(math8(2))
    print(math8(3))
    print(math8(-1))
    print(math8(5))
    print(math8(10))


if __name__ == '__main__':
    main()
