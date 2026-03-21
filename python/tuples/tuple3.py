# @desc Slicing a tuple returns a new tuple — the start index is included, the end index is excluded.

def tuple3(t):
    return str(t[1:3])


def main():
    print(tuple3((1, 2, 3, 4, 5)))
    print(tuple3(('a', 'b', 'c', 'd')))
    print(tuple3((10, 20, 30)))
    print(tuple3((1, 2)))


if __name__ == '__main__':
    main()
