# @desc **//** gives the quotient and **%** gives the remainder — together they break a division into its two parts.

def math10(x, y):
    return x // y + x % y


def main():
    print(math10(17, 5))
    print(math10(10, 3))
    print(math10(7, 2))
    print(math10(100, 10))
    print(math10(9, 4))
    print(math10(1, 1))


if __name__ == '__main__':
    main()
