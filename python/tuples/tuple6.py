# @desc Tuple unpacking assigns each element to a separate variable. **a, b = (1, 2)** sets a to 1 and b to 2.

def tuple6(t):
    a, b = t
    return a + b


def main():
    print(tuple6((3, 4)))
    print(tuple6((1, 1)))
    print(tuple6((0, 5)))
    print(tuple6((10, -3)))
    print(tuple6((-1, -1)))


if __name__ == '__main__':
    main()
