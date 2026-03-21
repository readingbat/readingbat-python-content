# @desc **max()** and **min()** find the largest and smallest values in a tuple.

def tuple9(t):
    return max(t) - min(t)


def main():
    print(tuple9((1, 5, 3)))
    print(tuple9((10, 10)))
    print(tuple9((1, 2, 3, 4, 5)))
    print(tuple9((-5, 0, 5)))
    print(tuple9((100, 1)))


if __name__ == '__main__':
    main()
