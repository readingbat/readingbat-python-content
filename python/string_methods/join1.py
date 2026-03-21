# @desc **.join()** places the separator string between each element of the list.

def join1(sep, words):
    return sep.join(words)


def main():
    print(join1('-', ['a', 'b', 'c']))
    print(join1(' ', ['hello', 'world']))
    print(join1('', ['a', 'b']))
    print(join1(',', ['x']))
    print(join1('--', []))


if __name__ == '__main__':
    main()
