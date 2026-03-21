# @desc **.index()** returns the position of the first occurrence of a value in the tuple.

def tuple8(t, x):
    return t.index(x)


def main():
    print(tuple8((10, 20, 30), 20))
    print(tuple8(('a', 'b', 'c'), 'c'))
    print(tuple8((1, 2, 3, 2), 2))
    print(tuple8((5,), 5))


if __name__ == '__main__':
    main()
