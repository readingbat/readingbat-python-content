# @desc The **%** operator is evaluated left to right, so compute **x % y** first, then apply **% z** to that result.

def math9(x, y, z):
    return x % y % z


def main():
    print(math9(17, 5, 3))
    print(math9(10, 3, 2))
    print(math9(100, 7, 3))
    print(math9(8, 3, 5))
    print(math9(20, 6, 3))


if __name__ == '__main__':
    main()
