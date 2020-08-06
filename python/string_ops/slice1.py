# @desc The first character in a string is at index 0.

def slice1(s):
    c = s[0]
    return c


def main():
    print(slice1('Car'))
    print(slice1('Truck'))
    print(slice1('55684'))
    print(slice1('Elephant'))
    print(slice1('Roses'))


if __name__ == '__main__':
    main()
