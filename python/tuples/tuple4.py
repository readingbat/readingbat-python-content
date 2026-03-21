# @desc The **in** operator checks if a value exists anywhere in the tuple.

def tuple4(t, x):
    return x in t


def main():
    print(tuple4((1, 2, 3), 2))
    print(tuple4((1, 2, 3), 5))
    print(tuple4(('a', 'b'), 'a'))
    print(tuple4((), 'x'))
    print(tuple4((1, 1, 1), 1))


if __name__ == '__main__':
    main()
