# @desc **len()** returns the length of a string.

def strlen1(s):
    length = len(s)
    return length


def main():
    print(strlen1('Car'))
    print(strlen1(''))
    print(strlen1('5'))
    print(strlen1('Elephant'))
    print(strlen1('Roses'))


if __name__ == '__main__':
    main()
