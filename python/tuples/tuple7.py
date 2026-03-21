# @desc **.count()** returns how many times a value appears in the tuple.

def tuple7(t, x):
    return t.count(x)


def main():
    print(tuple7((1, 2, 1, 3, 1), 1))
    print(tuple7((1, 2, 3), 4))
    print(tuple7(('a', 'b', 'a'), 'a'))
    print(tuple7((), 1))
    print(tuple7((5, 5, 5, 5), 5))


if __name__ == '__main__':
    main()
