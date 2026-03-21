# @desc **max()** returns the largest value and **min()** returns the smallest.

def math6(a, b, c):
    return max(a, b, c) - min(a, b, c)


def main():
    print(math6(1, 5, 3))
    print(math6(10, 10, 10))
    print(math6(1, 2, 3))
    print(math6(-5, 0, 5))
    print(math6(100, 1, 50))


if __name__ == '__main__':
    main()
