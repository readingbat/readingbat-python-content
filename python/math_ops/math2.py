# @desc The **//** operator divides and rounds down to the nearest whole number.

def math2(x, y):
    return x // y


def main():
    print(math2(7, 2))
    print(math2(10, 3))
    print(math2(9, 3))
    print(math2(1, 5))
    print(math2(15, 4))
    print(math2(100, 10))


if __name__ == '__main__':
    main()
