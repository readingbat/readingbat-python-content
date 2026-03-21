# @desc **len()** works on tuples just like it does on strings and lists.

def tuple2(t):
    return len(t)


def main():
    print(tuple2((1, 2, 3)))
    print(tuple2(()))
    print(tuple2(('a',)))
    print(tuple2((1, 2, 3, 4, 5)))
    print(tuple2(('hello', 'world')))


if __name__ == '__main__':
    main()
